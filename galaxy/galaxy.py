from redbot.core import commands, checks
import discord

class Galaxy(commands.Cog):
    """Custom cog intended for use on the Galaxy discord server."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(autohelp=True)
    async def faq(self, ctx):
        """Posts answers to frequently asked questions."""

    @faq.command(name="test")
    @checks.admin()
    async def faq_test(self, ctx, member: discord.Member = None):
        """Testing FAQ"""
        embed=discord.Embed(title="Test Embed", color=await self.bot.get_embed_color(None), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer in faucibus odio, at mollis metus.")
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url_as(format="png", size=512))
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="dps")
    async def faq_dps(self, ctx, member: discord.Member = None):
        """DPS Calculations/Inaccuracy"""
        embed=discord.Embed(title="DPS Calculations", color=await self.bot.get_embed_color(None), description="The ``/info`` command (and by extention ``/shipinfo`` from Odin) misreports DPS, due to it calculating DPS disregarding the turret's type (kinetic, laser), causing it to assume the target ship is both hulled and has shield simultaneously. It also ignores turret overrides, custom reloads, and custom damage values. If you'd like to check ship stats accurately, you can either use the ``/ship`` command in this channel or you can use the [Galaxy Info Website](https://galaxy.wingysam.xyz/ships). Alternatively, to check turret stats, you can use the [Galaxy Info Turrets Page](https://galaxy.wingysam.xyz/turrets).")
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="links")
    async def faq_links(self, ctx, member: discord.Member = None):
        """Posts important links, primarily invite links."""
        embed=discord.Embed(title="Important Links", color=await self.bot.get_embed_color(None))
        embed.add_field(name="Galaxy", value="[Galaxy Discord](https://discord.com/invite/robloxgalaxy)\n[Galaxy Support](https://discord.com/invite/ShWshkhYhZ)")
        embed.add_field(name="Galaxypedia", value="[Galaxypedia Website](https://robloxgalaxy.wiki/wiki/Main_Page)\n[Galaxypedia Discord](https://discord.robloxgalaxy.wiki/)")
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="ropro")
    async def faq_ropro(self, ctx, member: discord.Member = None):
        """Posts a link to RoPro"""
        embed=discord.Embed(title="RoPro", url="https://ropro.io", color=await self.bot.get_embed_color(None), description="""[RoPro](https://ropro.io) is a browser extension that tracks ROBLOX playtime, enhances your profile, and provides other useful utilities. **Please keep in mind that RoPro only tracks playtime from AFTER you install the extension.**""")
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="polaris_ranks")
    async def faq_polaris_ranks(self, ctx, member: discord.Member = None):
        """Lists required levels for certain roles."""
        embed=discord.Embed(title="Polaris Ranks", color=await self.bot.get_embed_color(None))
        embed.add_field(name="Picture Perms", value="Level 7", inline=False)
        embed.add_field(name="Suggestions", value="Level 9", inline=False)
        embed.add_field(name="DJ", value="Level 11", inline=False)
        embed.add_field(name="Reaction Perms", value="Level 30", inline=False)
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="polaris_switch")
    @checks.admin()
    async def faq_polaris_switch(self, ctx, member: discord.Member = None):
        """Posts an embed on the switch to the Polaris bot."""
        embed=discord.Embed(title="Polaris FAQ", color=await self.bot.get_embed_color(None), description="As you probably know, we've decided to switch to the Polaris bot for leveling/xp, as opposed to Tatsu.\nThere are many reasons for this, which will be explained below.")
        embed.add_field(name="Problems with Tatsu", value="1: Tatsu does not provide nearly as much configuration potential as Polaris does. An example of this is Polaris' customizable Level Curve.\n\n2: Tatsu does not have channel/role modifiers.\n\n3: Tatsu does not have actual levels, instead it has unconfigurable \"Global XP\", which gives \"Global Levels\". You cannot do anything with Global XP aside from blacklisting channels where people can gain it, like a bot-commands channel or something like that.\n\n4: Tatsu's leaderboard sucks, and only shows the top 10 on the web version.\n\n5: Tatsu has no XP management commands.\n\n6: Tatsu has TONS of bloat/useless commands, making the bot harder to configure.", inline=False)
        embed.add_field(name="Polaris' Features", value="1: Polaris allows you to customize the level curve of your server, and provides presets to make the transition easier.\n\n2: Polaris has XP management commands.\n\n3: Polaris has way more configuration in terms of Reward Roles.\n\n4: Polaris allows you to customize the level-up message shown whenever people achieve the next level.\n\n5: Polaris has both role and channel modifiers.\n\n6: Polaris' leaderboard is excellent, showing the top 1,000 ranked users on the same webpage, and allowing you to see your own stats, progress towards your next reward role, and all 350 levels and your progress towards them.\n\n7: Polaris is **just** a leveling bot. You don't have to deal with any of the bloat of multi-purpose bots like Tatsu or MEE6, you only get what you actually need.", inline=False)
        embed.add_field(name="Conclusion",value="With all of that said, you're probably wondering why we're putting so much effort into transferring peoples' data to the new bot.\n\nWell, Tatsu has been going since 2020, and I don't particularly favor the idea of clearing everyone's XP, especially when people have built up reward roles from Tatsu already, like Picture Perms, Suggestions access, and DJ.\n\nWith all this in mind, I hope this isn't too much of an inconvenience for you all, as I tried to make the process as seamless as possible without having to update all 10,000 people in the server.", inline=False)
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="npc_intervals")
    async def faq_npc_intervals(self, ctx, member: discord.Member = None):
        """Posts an embed containing NPC spawn intervals."""
        embed=discord.Embed(title="NPC Spawn Intervals", color=await self.bot.get_embed_color(None), description="*Disclaimer: Spawn times may be different if EventID is active!*")
        embed.add_field(name="Every 6.7 Minutes", value="[Dragoon](https://robloxgalaxy.wiki/wiki/Dragoon) *(80% Chance)*")
        embed.add_field(name="Every 8.4 Minutes", value="[Swarmer](https://robloxgalaxy.wiki/wiki/Swarmer) *(33% Chance)*")
        embed.add_field(name="Every 10 Minutes", value="[Jormungand](https://robloxgalaxy.wiki/wiki/Jormungand) *(75% Chance)*")
        embed.add_field(name="Every 12.5 Minutes", value="[Bruiser](https://robloxgalaxy.wiki/wiki/Bruiser) *(50% Chance)*")
        embed.add_field(name="Every 16.7 Minutes", value="[Outrider](https://robloxgalaxy.wiki/wiki/Outrider) *(50% Chance)*")
        embed.add_field(name="Every 28.5 Minutes", value="[Punisher](https://robloxgalaxy.wiki/wiki/Punisher)")
        embed.add_field(name="Every 60 Minutes", value="[X-0](https://robloxgalaxy.wiki/wiki/X-0) *(45% Chance)*\n[Decimator](https://robloxgalaxy.wiki/wiki/Decimator)")
        embed.add_field(name="Every 70 Minutes", value="[Galleon](https://robloxgalaxy.wiki/wiki/Galleon)")
        embed.add_field(name="Every 120 Minutes", value="[Kodiak](https://robloxgalaxy.wiki/wiki/Kodiak)")
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
        else:
            await ctx.channel.send(embed=embed)
        await ctx.message.delete()

    @faq.command(name="linked_role")
    async def faq_linked_role(self, ctx, member: discord.Member = None):
        """Posts an embed containing FAQ about Linked Role. (WIP)"""
        color=await self.bot.get_embed_color(None)
        embed=discord.Embed(title="Linked Role", color=color, description="**Before reading this, please make sure your Discord client is updated! On Mobile, you can do this by going to your app store of choice and updating Discord manually. On PC/MacOS/Linux you can do this by clicking the green update button in the top right.**")
        embed_desktop=discord.Embed(title="PC / MacOS / Linux (WIP)", color=color, description="WIP")
        embed_mobile=discord.Embed(title="Mobile (WIP)", color=color, description="WIP")
        if member:
            await ctx.channel.send(embed=embed, content=member.mention)
            await ctx.channel.send(embed=embed_desktop)
            await ctx.channel.send(embed=embed_mobile)
        else:
            await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed_desktop)
            await ctx.channel.send(embed=embed_mobile)
        await ctx.message.delete()


    @faq_test.error
    @faq_npc_intervals.error
    @faq_links.error
    @faq_dps.error
    @faq_ropro.error
    @faq_polaris_ranks.error
    @faq_polaris_switch.error
    async def faq_handler(self, ctx, error):
        """Error Handler for FAQ."""
        if isinstance(error, discord.NotFound):
            return