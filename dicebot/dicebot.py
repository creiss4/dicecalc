from discord import Intents
from discord.ext.commands import Bot, Command

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
