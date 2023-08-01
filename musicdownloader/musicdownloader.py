import asyncio
import re
import discord
from os import path, makedirs, sep
from yt_dlp import YoutubeDL
from redbot.core import commands, checks, Config, data_manager

class MusicDownloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=475728338)
        self.config.register_global(
            save_directory = str(data_manager.cog_data_path()) + f"{sep}MusicDownloader"
        )

    @commands.command()
    async def change_data_path(self, ctx: commands.Context, data_path: str = None):
        """This command changes the data path this cog outputs to."""
        old_path = await self.config.save_directory()
        if path.isdir(data_path):
            await self.config.save_directory.set(data_path)
            embed=discord.Embed(color=await self.bot.get_embed_color(None), description=f"The save directory has been set to `{data_path}`.\n It was previously set to `{old_path}`.")
            await ctx.send(embed=embed)
        elif path.isfile(data_path):
            await ctx.send("The path you've provided leads to a file, not a directory!")
        elif path.exists(data_path) is False:
            await ctx.send("The path you've provided doesn't exist!")

    @commands.command(aliases=["dl"])
    async def download(self, ctx: commands.Context, url: str, subfolder: str = None):
        """This command downloads a YouTube Video as an MP3 to the local music directory."""
        def youtube_download(self, url: str, path: str, message: discord.Message):
            """This function does the actual downloading of the YouTube Video."""
            class Logger:
                def debug(self, msg):
                    if msg.startswith('[debug] '):
                        pass
                    else:
                        self.info(msg)
                def info(self, msg):
                    pass
                def warning(self, msg):
                    pass
                def error(self, msg):
                    print(msg)
                    message.edit(msg)
            def hook(d):
                if d['status'] == 'finished':
                    message.edit('Done!')
            ydl_opts = {
            'logger': Logger(),
            'progress_hooks': [hook],
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a',}],
            'paths': [{'home': path}]
            }
            with YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download(url)
        data_path = await self.config.save_directory()
        if subfolder:
            data_path = path.join(data_path, subfolder)
            illegal_chars = r'<>:"/\|?*'
            if any(char in illegal_chars for char in subfolder):
                pattern = "[" + re.escape(illegal_chars) + "]"
                modified_subfolder = re.sub(pattern, r'__**\g<0>**__', subfolder)
                await ctx.send(f"Your subfolder contains illegal characters: `{modified_subfolder}`")
                return
            elif path.isfile(data_path):
                await ctx.send("Your 'subfolder' is a file, not a directory!")
                return
            elif path.exists(data_path) is False:
                message = await ctx.send("Your subfolder does not exist yet, would you like to continue? It will be automatically created.")
                def check(message):
                    return message.author == ctx.author and message.content.lower() in ['yes', 'ye', 'y']
                try:
                    await self.bot.wait_for('message', check=check, timeout=60) # Timeout after 60 seconds
                except asyncio.TimeoutError:
                    await message.edit("You took too long to respond.")
                else:
                    await message.edit("Confirmed!")
                    try:
                        makedirs(data_path)
                    except OSError as e:
                        await message.edit(f"Encountered an error attempting to create the subfolder!\n`{e}`")
                    msg = message.edit
        else:
            msg = ctx.send
        message = await msg("YouTube Downloader started!")
        youtube_download(self, url, data_path, message)
