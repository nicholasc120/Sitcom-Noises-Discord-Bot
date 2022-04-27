import random
import discord
from asyncio import sleep
import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


def pickRandomNoise():
    noises = ["Applause.mp3", "norm.mp3", "seinfeld.mp3", "friends.mp3"]
    return random.choice(noises)


@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    path = pickRandomNoise()
    if before.channel is None and after.channel is not None:
        channel = member.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(path))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()

client.run(os.getenv('TOKEN'))
