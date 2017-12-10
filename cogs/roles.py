import discord
from discord.ext import commands

# I wouldn't worry if you don't have these, just make sure you have the newest version of PYTHON
# and you're good to go!
import re, time, math, json, string, random, asyncio, datetime, traceback

class Roles:
	"""Contains role add and remove commands"""

	"""
		This contains all the role adds and role removes for MY server.
		You must edit all the commands to your own usage.
		DO NOT USE THE SAME FUNCTION NAME, NOR THE SAME ROLE NAMES (Unless you want to)
	"""

	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author.bot:
			return

	@commands.command(hidden=True, name='tf2+')
	async def tfp(self, ctx):
		"""Add yourself to the TF2 Group."""
		role = discord.utils.get(ctx.guild.roles, name="TF2")
		await ctx.author.add_roles(role)
		await ctx.send('Added to the TF2 group!')

	@commands.command(hidden=True, name='tf2-')
	async def tfm(self, ctx):
		"""Remove yourself from the TF2 Group."""
		role = discord.utils.get(ctx.guild.roles, name="TF2")
		await ctx.author.remove_roles(role)
		await ctx.send('Removed from the TF2 group.')

	@commands.command(hidden=True, name='wg+')
	async def wgp(self, ctx):
		"""Add yourself to the Wargamers Group."""
		role = discord.utils.get(ctx.guild.roles, name="Wargamers")
		await ctx.author.add_roles(role)
		await ctx.send('Added to the Wargamer group!')

	@commands.command(hidden=True, name='wg-')
	async def wgm(self, ctx):
		"""Remove yourself from the Wargamers Group."""
		role = discord.utils.get(ctx.guild.roles, name="Wargamers")
		await ctx.author.remove_roles(role)
		await ctx.send('Removed from the Wargamer group.')

	@commands.command(hidden=True, name='unturn+')
	async def utp(self, ctx):
		"""Add yourself to the Unturned Group."""
		role = discord.utils.get(ctx.guild.roles, name="Unturned")
		await ctx.author.add_roles(role)
		await ctx.send('Added to the Unturned group!')

	@commands.command(hidden=True, name='unturn-')
	async def utm(self, ctx):
		"""Remove yourself from the Unturned Group."""
		role = discord.utils.get(ctx.guild.roles, name="Unturned")
		await ctx.author.remove_roles(role)
		await ctx.send('Removed from the Unturned group.')

	@commands.command(hidden=True, name='terr+')
	async def terrp(self, ctx):
		"""Add yourself to the Terraria Group."""
		role = discord.utils.get(ctx.guild.roles, name="Terraria")
		await ctx.author.add_roles(role)
		await ctx.send('Added to the Terraria group!')

	@commands.command(hidden=True, name='terr-')
	async def terrm(self, ctx):
		"""Remove yourself from the Terraria Group."""
		role = discord.utils.get(ctx.guild.roles, name="Terraria")
		await ctx.author.remove_roles(role)
		await ctx.send('Removed from the Terraria group.')

	@commands.command(hidden=True, name='pd2+')
	async def pd2p(self, ctx):
		"""Add yourself to the Payday 2 Group."""
		role = discord.utils.get(ctx.guild.roles, name="PAYDAY 2")
		await ctx.author.add_roles(role)
		await ctx.send('Added to the Payday 2 group!')

	@commands.command(hidden=True, name='pd2-')
	async def pd2m(self, ctx):
		"""Remove yourself from the Payday 2 Group."""
		role = discord.utils.get(ctx.guild.roles, name="PAYDAY 2")
		await ctx.author.remove_roles(role)
		await ctx.send('Removed from the Payday 2 group.')

	@commands.command(hidden=True, name='lewd+')
	async def lewdp(self, ctx):
		"""Get lewd permissions."""
		role = discord.utils.get(ctx.guild.roles, name="Lewd")
		await ctx.author.add_roles(role)

	@commands.command(hidden=True, name='lewd-')
	async def lewdm(self, ctx):
		"""Remove lewd permissions."""
		role = discord.utils.get(ctx.guild.roles, name="Lewd")
		await ctx.author.remove_roles(role)

def setup(bot):
	bot.add_cog(Roles(bot))
