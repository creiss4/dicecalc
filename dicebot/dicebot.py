from typing import List
from sys import prefix
from discord import Intents
from discord.ext.commands import Bot, Command, when_mentioned_or
from pyparsing.exceptions import ParseException 
from discord.message import Message
from .parsemath import MathParser, DiceRolls

class Dicebot:

    token:str
    prefix:str
    invocation_count:int
    bot:Bot

    def __init__(self, token:str=None, prefix:str='d!'):
        self.token = token
        self.prefix = when_mentioned_or(prefix)

        self.invocation_count = 0
        bot:Bot = Bot(command_prefix=self.prefix, case_insensitive=True, intents=Intents().all())
        bot.event(self.on_ready)
        bot.event(self.on_message)
        bot.event(self.on_error)
        self.bot = bot

    def connect(self) -> None:
        self.bot.run(self.token)

    async def on_ready(self):
        pass

    def format_message(self, total: int, rolls: List[DiceRolls]):
        lines = [f'Total: {total}']

        for roll in rolls:
            results = ", ".join(list(map(str, roll.results)))
            lines.append(f'{roll.roll}: {results}')

        body = "\n".join(lines)

        if len(body) > 1900:
            body = body[:1900]

        return f'```\n{body}\n```'

    async def on_message(self, message: Message):
        """
        Input of "3d20 + 2d12"

        ```
        Total: 34
        3d20: 2, 5, 5
        2d12: 10, 12
        ```
        """
        if message.author.bot:
            return
        for prefix in self.prefix(self.bot, message):
            if not message.content.startswith(prefix): continue
            content = message.content.replace(prefix, "", 1)
            p = MathParser()
            try:
                value = p.eval(content)
                response = self.format_message(value, p.dice_roles)
                await message.channel.send(response)
            except ParseException as e:
                await message.channel.send("`Invalid entry. Try again.`")
            break


    async def on_error(self, event, *args, **kwargs):
        if (event == "on_message"):
            await args[0].channel.send("`Invalid entry. Try again.`")
        else:
            pass
        
