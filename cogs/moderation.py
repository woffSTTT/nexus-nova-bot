import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="Banna un utente")
    async def ban(self, ctx, member: discord.Member, reason: str = "Nessuna motivazione"):
        await member.ban(reason=reason)
        embed = discord.Embed(title="Utente Bannato", description=f"{member.mention} è stato bannato", color=discord.Color.red())
        embed.add_field(name="Motivo", value=reason)
        await ctx.respond(embed=embed)

    @commands.slash_command(name="kick", description="Espelli un utente")
    async def kick(self, ctx, member: discord.Member, reason: str = "Nessuna motivazione"):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Utente Espulso", description=f"{member.mention} è stato espulso", color=discord.Color.orange())
        embed.add_field(name="Motivo", value=reason)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
