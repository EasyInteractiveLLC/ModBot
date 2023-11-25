import discord
from discord.ext import commands
from cogs.utils.checks import load_env_vars, read_json, write_json, is_staff
from cogs.events import conn


class admincmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.X_train = None

    @commands.command(description="This is a test command")
    async def test(self, ctx: commands.Context):
        await ctx.send("This is a test command")


async def setup(bot):
    await bot.add_cog(admincmd(bot))
