import discord
import asyncio
import json
from discord.ext import commands 
from discord.ext.commands import CommandNotFound
from cogs.utils.checks import  *


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_group(description="View Commands")
    async def help(self, ctx):
      if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Core Utilities Commands", description=f"```fix\nBot Prefix: m.```", color=discord.Color.blue())
        embed.add_field(name="Moderation:", value=f"`m.help moderation`")
        embed.add_field(name="Warn:", value=f"`m.help warn`")
        embed.add_field(name="Other:", value=f"`m.help other`")
        embed.set_footer(text="Core Utilities Command Panel")
        await ctx.send(embed=embed)

    @help.command(description="Moderation Panel")
    async def moderation(self, ctx):
      embed = discord.Embed(title="Moderation Commands:", description=f"`m.kick @person [reason for kicked]` - kick someone\n\n`m.ban @person [reason for banned]` - ban someone\n\n`m.unban name#id` - unban someone\n\n`m.unmute @person` - unmute someone\n\n`m.mute @person [amount d,h,m,s ex: 5s] [reason]` - time mute someone\n\n`m.clear [amount]` - purges messages, default is 20\n\n`m.give @person @role` - give someone a role\n\n`m.remove @person @role` - remove a role from someone\n\n`m.nick @person [nickname]` - Nickname someone\n\n`m.reset_nick @person` - reset the nickname for the user\n\n`m.sendvm [command]` - this will send a verification message with the command of your choice\n\n`m.verify` - this is the stock verification command\n\n`m.rules [Rules]` - This will create an embed for your server rules!", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

    @help.command(description="Warn Panel")
    async def warn(self, ctx):
      embed = discord.Embed(title="Warn Commands:", description=f"`m.warn @person [reason they were warned]` - warn someone\n\n`m.warnings @person` - get the warnings for someone\n\n`m.delwarn @person` - Deletes all warns for the person you mentioned", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

    @help.command(description="Other Commands")
    async def other(self, ctx):
      embed = discord.Embed(title="Member Commands:", description=f"`m.afk [AFK Note]` - sets you as afk\n\n`m.userinfo @person` - Get Information On Any User.", color=discord.Color.blue())
      embed.set_footer(text="All commands have a cooldown")
      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(help(bot))
