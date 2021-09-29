import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 244523000886460426# Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author)

bot.run(TOKEN)  # Starts the bot