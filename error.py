import discord
from discord.utils import get
from discord.ext import commands 
from discord.ext.commands import CommandNotFound

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="ERROR!", description=":x:You need to pass in all the requirements to do this command!", color=discord.Color.red())
        await ctx.send(embed=embed)
      elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="ERROR!", description=":x:You do not have the permission to do this command!", color=discord.Color.red())
        await ctx.send(embed=embed)
      elif isinstance(error, CommandNotFound):
        embed = discord.Embed(title="ERROR!", description=":x:Command Not Found!", color=discord.Color.red())
        await ctx.send(embed=embed)
      elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Cooldown!", description=f"This command is on cooldown, try again after `{round(error.retry_after)}` seconds.")
        await ctx.send(embed=embed)
      else:
        channel = self.bot.get_channel(1175618939519250563)
        embed = discord.Embed(title="ERROR!", description=":x:Something went wrong!!\n\nYou may open a support forum in our support server!!", color=discord.Color.red())
        await ctx.send(embed=embed)
        embed2 = discord.Embed(title="Something went wrong!", description=f"Error: `{error}`", color=discord.Color.blue())
        embed2.set_footer(text=f"Done by: {ctx.author.name}#{ctx.author.discriminator} in {ctx.guild.name}")
        await channel.send(embed=embed2)


async def setup(bot):
  await bot.add_cog(error(bot))