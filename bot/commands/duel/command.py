from interactions import CommandContext
from asyncio import sleep
from age.bot import Bot
from age.utils import send_or_edit, get_message, find_skill_by_name, Locker
from age.entity import Entity
from .component import duel_component

class Duel:
    def __init__(self, bot: Bot, player1: Entity, player2: Entity):
        self.players          = [player1, player2]
        self.turn             = 0
        self.bot              = bot

    async def start(self, ctx: CommandContext):
        lock = Locker()


        async def attack(ctx: CommandContext, options: list):
            if int(ctx.author.id) == attacker.id:
                attack = await attacker.hit(defender, find_skill_by_name(attacker.skills, options[0]))

                await send_or_edit(
                    'attack_message',
                    ctx, self.bot,
                    f'**{attacker.name}** caused **{attack.damage}** damage'
                )

                await lock.release()
            else:
                m = await ctx.send(f'It is not your turn to attack, **{defender.name}**')
                await sleep(2.5)
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

            text = f"""
TURN **{self.turn+1}**

{f'**{player1.name}**:':30} {player1.health}/{player1.max_health}
{f'**{player2.name}**:':30} {player2.health}/{player2.max_health}

**Attacker**: {attacker.name}
            """

            await send_or_edit('component_message', ctx, self.bot, text, components=duel_component(attacker.skills))
            await lock.wait()
            
            self.turn += 1


        # I find out which player won and died
        winner   = player1 if not player1.is_dead else player2
        defeated = player1 if     player1.is_dead else player2

        await ctx.send(f'**{winner.name}** won the duel against **{defeated.name}**')

        # I delete the duel messages
        await get_message('attack_message').delete()
        await get_message('component_message').delete()
