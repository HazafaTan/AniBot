import discord 
from dotenv import load_dotenv
from discord.ext import commands
import os

    

load_dotenv()
TOKEN = os.environ.get("TOKEN")

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
#client = commands.Bot(command_prefix = '.', intents = intents)


bot = commands.AutoShardedBot(
    command_prefix= '.',
    case_insensitive = True,
    intents = intents,
    use_slash_commands = True
 )


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print('Dev has been loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print('Dev has been unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:3]}')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server')




bot.run(TOKEN)






