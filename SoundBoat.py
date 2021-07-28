import discord
import importlib
from discord import FFmpegPCMAudio
import time

client = discord.Client()
dbAPI = importlib.import_module("SoundBoatDBAPI")


@client.event
async def on_ready():
    print("Bot online, showing as {}".format(client.user))
    await client.change_presence(activity=discord.Game("..."))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.__contains__("!sb"):
        if message.content.__contains__("play"):
            mp3ToPlay = message.content.split()[2]
            await message.channel.send("Playing " + dbAPI.getFileName(mp3ToPlay))
            channel = message.author.voice.channel
            vc = await channel.connect()
            source = FFmpegPCMAudio("./SoundBoat sounds/{}".format(dbAPI.getFileName(mp3ToPlay)))
            player = vc.play(source)
            while vc.is_playing():
                time.sleep(0.2)
            await vc.disconnect()

        if message.content.__contains__("help"):
            await message.channel.send("To make the SoundBoat play a Sound, type: *!sb play [sound]*\n"
                                       "List of sounds:\n" +
                                       dbAPI.getAllSounds())


client.run("ODY3NDI4MzUwODc2NTgxOTI5.YPg9mg.G4hv3iw1hdiYS0tGfvkpLNKkDVU")
