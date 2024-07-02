import discord
import importlib
import os
from dotenv import load_dotenv
from SoundBoatFeatures.SoundBoatPlay import handle_play_command

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
dbAPI = importlib.import_module("SoundBoatDBAPI")   # Initialize db
voice_clients = {}    # Manage mulitple connected voice clients


@client.event
async def on_ready():
    print("Bot online, showing as {}".format(client.user))
    await client.change_presence(activity=discord.Game(os.getenv('BOT_ACTIVITY_STATUS')))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.__contains__(os.getenv('BOT_INVOKE_MSG')):
        if message.content.__contains__("play"):
            await handle_play_command(message, client, voice_clients, dbAPI)

        if message.content.__contains__("help"):
            await message.channel.send("To make the SoundBoat play a Sound, type: *!sb play [sound]*\n"
                                       "List of sounds:\n" +
                                       dbAPI.getAllSounds())


client.run(os.getenv('DISCORD_DEVELOPER_TOKEN'))
