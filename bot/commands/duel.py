from interactions import CommandContext, Message
from asyncio import get_event_loop, sleep
from age.bot import Bot
from age.components import Grid
from age.entity import Entity

class Duel:
    def __init__(self, bot: Bot, interface: Grid, player1: Entity, player2: Entity):
        self.players          = [player1, player2]
        self.turn             = 0
        self.bot              = bot

        # Components interface
        self.interface        = interface

        # I use this to save the sent message and then edit it
        self.component_message: Message = None
        self.attack_message   : Message = None

        # I create a future that serves to wait for the attack function to finish
        self.loop = get_event_loop()
        self.fut = self.loop.create_future()

    async def start(self, ctx: CommandContext):



        async def attack(ctx: CommandContext, options: list):
            if int(ctx.author.id) == attacker.id:
                # { skill name: skill instance }
                skills = {i().name:i() for i in attacker.skills}

                attack = await attacker.hit(defender, skills[options[0]])



                # If the bot has already sent the message, edits the existing message, if not, sends the message

                if self.attack_message:
                    self.attack_message = await self.attack_message.edit(f'**{attacker.name}** caused **{attack.damage}** damage')

                    # Resolves error "HTTPClient not found!", when the message is edited several times
                    self.attack_message._client = self.bot._http
                else:
                    self.attack_message = await ctx.send(f'**{attacker.name}** caused **{attack.damage}** damage')
                self.turn += 1

                # It says that the attack function has finished, so the while can continue
                self.fut.set_result(True)
            else:
                m = await ctx.send(f'It is not your turn to attack, **{defender.name}**')
                await sleep(2)
                await m.delete()




        # I set the event name to the same id I set in the select in duel_component,
        # so when the user selects the item in the select, the attack function is called
        self.bot.add_event(attack, f'duel__select')

        player1, player2 = self.players

        while not any(player.is_dead for player in self.players):
            """
            Run this code to understand how I select who to attack and who to defend
            
            a = [1, 2]

            for i in range(100):
                print(a[i % len(a)])
            
            """
            attacker = self.players[self.turn % 2]
            defender = self.players[(self.turn + 1) % 2]


            skills = [s().name for s in attacker.skills]

            # Create the interface select containing the skill names
            interface = self.interface(skills)

            # I saved the text in a variable so I could add the padding to the text
            n1 = f'**{player1.name}:**'
            n2 = f'**{player2.name}:**'

            text = f"""
TURN **{self.turn+1}**

{n1:30} {player1.health}/{player1.max_health}
{n2:30} {player2.health}/{player2.max_health}

**Attacker**: {attacker.name}
            """


            # If the bot has already sent the message, edits the existing message, if not, sends the message


            if self.component_message:
                self.component_message = await self.component_message.edit(text, components=interface)

                # Resolves error "HTTPClient not found!", when the message is edited several times
                self.component_message._client = self.bot._http
            else:
                self.component_message = await ctx.send(text, components=interface)


            # Checks if the clicked component is the select
            # If it is, the code continues, if not, it waits for the select to be clicked
            def check(c_ctx: CommandContext):
                return c_ctx.data.custom_id == 'duel__select'

            # Waits check to be true
            await self.bot.wait_for_component(self.interface(skills), check=check)


            # I wait for the attack function to finish
            await self.fut
            # I reset the future
            self.fut = self.loop.create_future()


        # I find out which player won and died
        winner   = player1 if not player1.is_dead else player2
        defeated = player1 if     player1.is_dead else player2

        # I delete the duel messages
        await self.attack_message.delete()
        await self.component_message.delete()

        await ctx.send(f'**{winner.name}** won the duel against **{defeated.name}**')