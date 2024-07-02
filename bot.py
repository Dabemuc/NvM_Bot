import discord
import importlib
import os
from dotenv import load_dotenv
from BotFeatures.Play.play import handle_play_command

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
import SQLiteDB.DBAPI as dbAPI  # Initialize db
voice_clients = {}    # Manage mulitple connected voice clients


@client.event
async def on_ready():
    print("Bot online, showing as {}".format(client.user))
    await client.change_presence(activity=discord.Game("Try '"+os.getenv("BOT_INVOKE_MSG")+" help'"))


@client.event
async def on_message(message):
    # dont process msg if bot is author
    if message.author == client.user:
        return
    
    # preprocess msg for command matching
    processed_msg_content = str(message.content).lower()

    # handle msg
    if processed_msg_content.__contains__(os.getenv('BOT_INVOKE_MSG')):
        print("Bot invoked with command:", processed_msg_content)
        if processed_msg_content.__contains__("play"):
            await handle_play_command(message, client, voice_clients, dbAPI)

        if processed_msg_content.__contains__("help"):
            await message.channel.send("To make the Bot play a Sound, type: "+os.getenv('BOT_INVOKE_MSG')+" play [sound]*\n"
                                       "List of sounds:\n" +
                                       dbAPI.getAllSounds())


client.run(os.getenv('DISCORD_DEVELOPER_TOKEN'))
