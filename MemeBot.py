import discord
import os
import requests
import json

TOKEN = "OTk1OTEwMjE1Mzk0NDEwNTU2.GuPGaY.orokgQ0zOgAKLThRD_7nZA6dvfVDVpd7y4eXQk"
client = discord.Client()


def get_meme():
    response = requests.get("https://generatorfun.com/")
    json_data = json.loads(response.text)
    meme = json_data[0]['q'] + " -" + json_data[0]['a']
    return meme



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('I WANT A MEME'):
        meme = get_meme()
        await message.channel.send(meme)

client.run(os.getenv(TOKEN))
