import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot Started')

@bot.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await message.channel.send('pong ~ Meow ><')

bot.run('NzY2ODM5MzQxNTY4NzUzNjk2.X4pMyg.n7CcjFzUeh3_He_hEJazOtz2w-4')