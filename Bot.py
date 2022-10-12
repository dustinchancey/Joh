# This example requires the 'message_content' intent.

import discord

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

    if message.content.startswith('why'):
        await message.channel.send('it was a little funny')

client.run('MTAyODkwMDc5Njk3ODQzODIwOA.GsQjjE.vBDd0rY-6bGq58cBf-9nN30dRJInE9lip09VX8')