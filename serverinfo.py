import discord
from discord.ext import commands

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command(description="Server Info", extras={'category': "Staff"})
    async def serverinfo(self, ctx: commands.Context):
        info_embed = discord.Embed(title=f"{ctx.guild.name}", description=f"Server Information.", color=discord.Color.blue())
        info_embed.set_thumbnail(url=ctx.guild.icon.url)
        info_embed.add_field(name="Server Name:", value=ctx.guild.name, inline=True)
        info_embed.add_field(name="Server ID:", value=ctx.guild.id, inline=True)
        info_embed.add_field(name="Server Owner:", value=ctx.guild.owner, inline=True)
        info_embed.add_field(name="Created At:", value=f"<t:{round(ctx.guild.created_at.timestamp())}:F>", inline=True)
        info_embed.add_field(name="Members:", value=ctx.guild.member_count, inline=True)
        info_embed.add_field(name="Roles:", value=len(ctx.guild.roles), inline=True)
        info_embed.add_field(name="Channels:", value=len(ctx.guild.channels), inline=True)
        info_embed.add_field(name="Verification Level:", value=ctx.guild.verification_level, inline=True)
        info_embed.add_field(name="Boosts:", value=ctx.guild.premium_subscription_count, inline=True)
        info_embed.add_field(name="Boost Level:", value=ctx.guild.premium_tier, inline=True)
        info_embed.add_field(name="Emojis:", value=len(ctx.guild.emojis), inline=True)
        
        info_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url) 

        await ctx.send(embed=info_embed)

async def setup(bot):
    await bot.add_cog(serverinfo(bot))