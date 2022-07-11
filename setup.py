# Generally this is only the startup file, don't mix
# project logic with startup here. This will be changed later on.

import discord


TOKEN = 'Bot Token'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Give me a Meme'):
        # meme = get_meme()
        await message.channel.send('Sorry I am too busy right now :/')

client.run(TOKEN)
