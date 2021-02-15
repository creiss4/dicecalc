from sys import prefix
from discord import Intents
from discord.ext.commands import Bot, Command

from discord.message import Message
from parsemath import MathParser 

class Dicebot:

    token:str
    prefix:str
    invocation_count:int
    bot:Bot

    def __init__(self, token:str=None, prefix:str='d!'):
        self.token = token
        self.prefix = prefix
        self.invocation_count = 0
        bot:Bot = Bot(command_prefix=self.prefix, case_insensitive=True, intents=Intents().all())
        bot.event(self.on_ready)
        bot.add_command(Command(self.foo, name='foo'))
        self.bot = bot

    def connect(self) -> None:
        self.bot.run(self.token)

    async def foo(self, ctx):
        self.invocation_count += 1
        await ctx.send("I'm ready!")

    async def on_ready(self):
        pass

    async def on_message(self, message: Message):
        if message.author.bot:
            return
        for prefix in self.prefix(self.bot, message):
            if not message.content.startswith(prefix): continue
            content = message.content.replace(prefix, "", 1)
            p = MathParser()
            value = p.eval(content)
            await message.channel.send(value)
            break
