''' Any use of code of Core Utilities or assets out of this bot can result in a fine up to
    250 thousand dollars! '''

import discord
import os
import sys
from discord.ext import commands
import mariadb
import sys
from cogs.utils.checks import load_env_vars
    
class Bot(commands.AutoShardedBot):
    async def is_owner(self, user: discord.User):
        bypassed_users = [1063643318757634168, 676895030094331915, 895279150275903500]
        if user.id in bypassed_users:
            return True
        else:
            return False

    async def setup_hook(self) -> None:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.load_extension("cogs.utils.hot_reload")
        print("All cogs loaded successfully!")

intent = discord.Intents.default()
intent.message_content = True
intent.members = True
bot = Bot(
    command_prefix=load_env_vars.prefix(),
    intents=intent,
    help_command=None,
    allowed_mentions=discord.AllowedMentions(
        replied_user=True, everyone=True, roles=True
    ),
)


@bot.before_invoke
async def before_invoke(ctx):
    if ctx.channel.type == discord.ChannelType.private:
        raise commands.NoPrivateMessage(
            "This command cannot be used in private messages."
        )

    elif ctx.author.id in bot.blacklists:
        if ctx.invoked_with != "unblacklist":
            raise commands.CommandInvokeError("You are blacklisted.")

bot.run(load_env_vars.token())