# This example requires the 'message_content' intent.
import os
from dotenv import load_dotenv
import discord
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('why'):
        await message.channel.send('it was a little funny')

    if message.content.startswith('hateful'):
        await message.channel.send(r'https://cdn.discordapp.com/attachments/1029544303485268041/1029557278552105000/hqdefault.jpg')

    if message.content.startswith('Jor'):
        # STUFF BROKEN BELOW LOL
        # # me = client.get_user('184829294051196928')
        # # await me.send(r'https://cdn.discordapp.com/attachments/1029544303485268041/1029557278552105000/hqdefault.jpg')  # or whatever you want to send here
        #
        # # me = await client.get_user_info('184829294051196928')
        # # await client.send_message(me, r"https://cdn.discordapp.com/attachments/1029544303485268041/1029557278552105000/hqdefault.jpg!")
        # user = client.get_user(184829294051196928)
        # # await user.send('👀')
        # await client.send_message(user, r"https://cdn.discordapp.com/attachments/1029544303485268041/1029557278552105000/hqdefault.jpg!")
        await message.author.send(r'https://media.discordapp.net/attachments/935989994735169546/1027423675412123648/36f106124c5091548053978b9fa8a60b.gif')

client.run(TOKEN)