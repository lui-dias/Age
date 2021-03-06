from os import environ

from bot.classes import Mage, Warrior
from bot.commands.duel.command import Duel

from age import Bot
from dotenv import load_dotenv
from interactions import CommandContext, Option, OptionType, Member

load_dotenv()

bot        = Bot(token=environ['DISCORD_BOT_TOKEN'])
DEV_SERVER = int(environ['DEV_SERVER'])






@bot.event
async def on_ready():
    print('Ready')










@bot.command(
    scope=DEV_SERVER,
    options = [
        Option(
            name        = 'user',
            description = 'Duel',
            type        = OptionType.USER,
            required    = True,
        ),
    ])
async def duel(ctx: CommandContext, user: Member):
    """
    Duel with another player

    <----------------->

    
    """

    player1 = ctx.author.user.username
    player2 = user.user.username

    w = Warrior(
        id               = int(ctx.author.id),
        name             = player1,
        attack_damage    = 10,
        magic_power      = 0,
        armor            = 20,
        health           = 100,
        magic_resistance = 0,
    )
    m = Mage(
        id               = int(user.user.id),
        name             = player2,
        attack_damage    = 0,
        magic_power      = 100,
        armor            = 0,
        health           = 80,
        magic_resistance = 0,
    )

    await Duel(bot, w, m).start(ctx)



bot.start()