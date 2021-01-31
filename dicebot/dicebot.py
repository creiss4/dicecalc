from discord import Intents
from discord.ext.commands import Bot, Command

class Dicebot:

    token:str
    prefix:str
    invocation_count:int

    def __init__(self, token:str=None, prefix:str='d!'):
        self.token = token
        self.prefix = prefix
        self.invocation_count = 0

    def connect(self) -> None:
        intents = Intents().all()
        client:Bot = Bot(command_prefix=self.prefix, case_insensitive=True, intents=intents)
        client.event(self.on_ready)
        client.add_command(Command(self.foo, name='foo'))
        client.run(self.token)

    async def foo(self, ctx):
        self.invocation_count += 1
        await ctx.send("I'm ready!")

    async def on_ready(self):
        pass
