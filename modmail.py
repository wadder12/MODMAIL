import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


intents = nextcord.Intents.all()
intents.guild_messages = True
bot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} is online.')

if __name__ == '__main__':
    bot.load_extension('cogs.waddermodmail')  # Assuming the ModMail cog is in a file named "modmail.py"
    bot.run(TOKEN)

