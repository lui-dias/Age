from asyncio import get_event_loop

from age.entity import Skill


messages = {}

async def send_or_edit(id, ctx, bot, text=None, components=None):
    """ If the bot has already sent the message, edits the existing message, if not, sends the message """
    message = messages.get(id, None)

    if message:
        message = await message.edit(text, components=components)

        # Resolves error "HTTPClient not found!", when the message is edited several times
        message._client = bot._http
    else:
        messages[id] = await ctx.send(text, components=components)

def get_message(id):
    return messages[id]

def find_skill_by_name(skills: Skill, name: str):
    return next((s for s in skills if s.name == name), None)

class Locker:
    def __init__(self):
        self.lock = get_event_loop().create_future()

    async def wait(self):
        await self.lock

    async def release(self):
        self.lock.set_result(True)
        self.lock = get_event_loop().create_future()


