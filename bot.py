import discord
import asyncio
import aiohttp
from discord.ext import commands
from discord.voice_client import VoiceClient


TOKEN = 'NDUzNDUyNzY1MTc2MjY2NzYz.DffG_Q.JNMoUyDe8FgopkUtv1LOEIANX5M'
BOT_PREFIX = ("%")
startup_extensions = ['Music']

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command(name = 'execute_order_66',
                description = 'haha',
                brief = 'haha',
                pass_context = True)
async def execute_order_66(context):
    msg = "Did you ever hear the tragedy of Darth Plageuis The Wise, " 
    msg += context.message.author.mention + "?\n"
    msg += "I thought not. It's not a story the Jedi would tell you." \
           " It\'s a Sith legend. Darth Plageuis was a Dark Lord of" \
           " the Sith, so powerful and so wise he could use the Force" \
           " to influence the midichlorians to create life... He had" \
           " such a knowledge of the dark side, he could even keep the" \
           " ones he cared about from dying."

    await client.say(msg)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='%help'))
    print('Logged in as ' + client.user.name)



if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension,exc))

client.run(TOKEN)

