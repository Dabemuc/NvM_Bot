from discord import FFmpegPCMAudio
import asyncio


async def handle_play_command(message, client, voice_clients, dbAPI):
    mp3ToPlay = message.content.split()[2]
    await message.channel.send("Playing " + dbAPI.getFileName(mp3ToPlay))
    channel = message.author.voice.channel
    voice_clients[message.guild.id] = await channel.connect()
    path = "./SoundBoat sounds/{}".format(dbAPI.getFileName(mp3ToPlay))
    options = {'options': '-vn'}
    source = FFmpegPCMAudio(path, **options)
    voice_clients[message.guild.id].play(
        source,
        after= lambda e: asyncio.run_coroutine_threadsafe(
            await voice_clients[message.guild.id].disconnect(),
            client.loop
        )
    )