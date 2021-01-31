"""
Click documentation: https://click.palletsprojects.com/en/7.x/
"""
import click

from . import Dicebot

@click.command(name='dicebot')
@click.option('-t', '--token', help='Bot API token')
@click.option('-f', '--file-token', help='Path to bot API token file', type=click.Path(exists=True))
def dicebot(token:str=None, file_token:str=None):

  if not token and file_token:
    with open(file_token, 'r') as fd:
      token = fd.read().strip()

  # print(f'starting dicebot token={token}')

  bot:Dicebot = Dicebot(token=token)
  bot.connect()


if __name__ == "__main__":
  dicebot.main(prog_name='dicebot')
