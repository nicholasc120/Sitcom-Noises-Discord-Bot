import random
from asyncio import sleep
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='$', activity=discord.Activity(
    type=discord.ActivityType.watching, name="How I Met Your Mother"))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Jefrrey sTeinfeld!')
    if message.content.startswith('$laugh'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("laugh.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$aww'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("aww.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$gasp'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("gasp.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$clap'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("Applause.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$thatswhatshesaid'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("thatswhatshesaid.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$bazinga'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("bazinga.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$howyoudoin'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("howyoudoin.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$challengeaccepted'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("challengeaccepted.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()
    if message.content.startswith('$dididothat'):
        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("dididothat.mp3"))
        while vc.is_playing():
            await sleep(1)
        await vc.disconnect()


def pickRandomNoise():
    noises = ["Applause.mp3", "norm.mp3", "seinfeld.mp3", "friends.mp3", "friends 2.mp3",
              "troy and abed in the morning.mp3", "family guy.mp3", "men.mp3"]
    return random.choice(noises)


@client.event
async def on_voice_state_update(member: discord.Member, before, after):
    path = pickRandomNoise()
    if not member.bot:
        if before.channel is None and after.channel is not None:
            channel = member.voice.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(path))
            while vc.is_playing():
                await sleep(1)
            await vc.disconnect()
        elif before.channel is not None and after.channel is None:
            path = "jazz.mp3"
            channel = before.channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio(path))
            while vc.is_playing():
                await sleep(1)
            await vc.disconnect()


client.run(os.getenv('TOKEN'))
