import discord
from discord.ext import commands

staff_roles = ["Core Team", "Moderator"] 

class rules(commands.Cog):
  def __init__(self, bot):
      self.bot = bot 

  @commands.hybrid_command(description="Set Rules")
  async def rules(self, ctx, *, rules = None):
      if any(role.name in staff_roles for role in ctx.author.roles):
        if rules is None:
          await ctx.send("Please put in the rules for your server!")
        else:
          embed = discord.Embed(title=f"Server Rules", description=rules, color=discord.Color.blue())
          await ctx.send(embed=embed)
      else:
        await ctx.send("You don't have permission to use this command.")

async def setup(bot):
  await bot.add_cog(rules(bot))