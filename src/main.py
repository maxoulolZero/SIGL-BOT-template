import os

# --- Discord Imports --- #
from discord.ext import commands
from discord import Member

# --- Python Imports --- #
from dotenv import load_dotenv
import random

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

# --------------- #
# --- Warm Up --- #
# --------------- #
@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author)

# --------------------- #
# --- Adminisration --- #
# --------------------- #
@bot.command()
async def admin(ctx):
    await ctx.send("TODO Implement admin")

@bot.command()
async def mute(ctx):
    await ctx.send("TODO Implement mute")
    
@bot.command()
async def ban(ctx, member: Member):
    # The guild corresponds to server, the function below means we'll ban the member <member>
    await ctx.guild.ban(member, reason="Because.")

    # Log to the server that the member <member> has been banned
    await ctx.send(f"You've banned {member} !")

# ------------------------------ #
# --- It's All Fun And Games --- #
# ------------------------------ #
@bot.command()
async def xkcd(ctx):
    number = random.randint()
    await ctx.send("TODO Implement xkcd")

@bot.command()
async def poll(ctx):
    await ctx.send("TODO Implement poll")

@bot.command()
async def tictactoe(ctx):
    await ctx.send("TODO Implement tictactoe")

bot.run(TOKEN)  # Starts the bot