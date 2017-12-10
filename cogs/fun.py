import discord
from discord.ext import commands

# I wouldn't worry if you don't have these, just make sure you have the newest version of PYTHON
# and you're good to go!
import re, time, math, json, string, random, asyncio, datetime, traceback

class Fun:
	"""Have some fun with friends!"""

	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		ctx = await self.bot.get_context(message)
		if message.author.bot:
			return

	@commands.command(hidden=True)
	async def shrug(self, ctx):
		"""¯\_(ツ)_/¯"""
		await ctx.message.delete()
		await ctx.send('¯\_(ツ)_/¯')

	@commands.command(hidden=True)
	async def tableflip(self, ctx):
		"""(╯°□°）╯︵ ┻━┻"""
		await ctx.message.delete()
		await ctx.send('(╯°□°）╯︵ ┻━┻')

	@commands.command(hidden=True)
	async def unflip(self, ctx):
		"""┬─┬﻿ ノ( ゜-゜ノ)"""
		await ctx.message.delete()
		await ctx.send('┬─┬﻿ ノ( ゜-゜ノ)')

	@commands.command(hidden=True)
	async def hello(self, ctx):
		"""Feeling lonely? Get the bot to say hello!"""
		await ctx.send(f'Hello {ctx.author.mention}!')

	@commands.command()
	async def muffin(self, ctx, user: discord.Member = None):
		"""Give yourself/someone else a muffin!"""
		await ctx.message.delete()
		if not user:
			await ctx.send(f"*Shoves muffin into {ctx.author.mention}\'s mouth*")
		else:
			await ctx.send(f"*Shoves muffin into {user.mention}\'s mouth*")

	@commands.command()
	async def cake(self, ctx, user: discord.Member = None):
		"""Give yourself/someone else a cake!"""
		await ctx.message.delete()
		if not user:
			await ctx.send(f"*Throws Cake at {ctx.author.mention}*")
		else:
			await ctx.send(f"*Throws Cake at {user.mention}*")

	@commands.command()
	async def boop(self, ctx, user: discord.Member = None):
		"""Boop yourself/someone else!"""
		await ctx.message.delete()
		if not user:
			await ctx.send(f"*Boops you*")
		else:
			await ctx.send(f"*Boops {user.mention}*")

	@commands.command()
	async def nom(self, ctx, user: discord.Member = None):
		"""Nom yourself/someone else!"""
		await ctx.message.delete()
		if not user:
			await ctx.send(f"*Noms you*")
		else:
			await ctx.send(f"*Noms {user.mention}*")

	@commands.command()
	async def quote(self, ctx, user: discord.Member, message = None):
		"""Quote a person lol"""
		if message == None:
			return
		await ctx.message.delete()
		await ctx.send(f"\"{message}\"\n- {user.mention}\n\t\t2017")

	@commands.command()
	async def mew(self, ctx):
		"""Derp o3o"""
		await ctx.send(f"https://goo.gl/mdSwEN")

	@commands.command()
	async def flop(self, ctx):
		"""Flop"""
		await ctx.message.delete()
		await ctx.send(f"*{ctx.author.mention} Flops*")

	@commands.command()
	async def kiss(self, ctx, user: discord.Member = None):
		"""Kiss someone you like~ D'aww~ <3"""
		items = [
			"Oh stop, you flatter me!",
			"Hehe >w<",
			"O-oh my...~ *Blushes*",
			"W-well I...",
			"M-meep!",
			"W-wha-? Was there mistletoe nearby?"
		]
		await ctx.message.delete()
		if user != None:
			await ctx.send(f"*{ctx.author.mention} kisses {user.mention}*\nD'aww~")
		else:
			await ctx.send(random.choice(items))

	@commands.command(hidden=True)
	async def nini(self, ctx):
		"""Say good night to someone <3"""
		await ctx.send(f"Nini {ctx.author.mention}")

	@commands.command()
	async def flip(self, ctx, user: discord.Member = None):
		"""Rage flip someone!"""
		await ctx.message.delete()
		if not user:
			await ctx.send(f"(╯°□°）╯︵ {ctx.author.mention}")
		else:
			await ctx.send(f"(╯°□°）╯︵ {user.mention}")

	@commands.command()
	async def server(self, ctx):
		"""Show some info about the server you're viewing."""

		statuses = {
			discord.Status.online: 0,
			discord.Status.idle: 0,
			discord.Status.dnd: 0,
			discord.Status.offline: 0
		}
		for member in ctx.guild.members:
			for status in statuses:
				if member.status is status:
					statuses[status] += 1

		att = {}
		att['Online'] = f'{sum(member.status is not discord.Status.offline for member in ctx.guild.members)}/{len(ctx.guild.members)}'
		att['Owner'] = ctx.guild.owner.display_name
		#att['Emojis'] = len(ctx.guild.emojis)
		att['Text channels'] = len(ctx.guild.text_channels)
		att['Voice channels'] = len(ctx.guild.voice_channels)
		att['Region'] = str(ctx.guild.region)
		att['Created at'] = str(ctx.guild.created_at).split(' ')[0]

		e = discord.Embed(title=ctx.guild.name, description='\n'.join(f'**{a}**: {b}' for a, b in att.items()))
		e.set_thumbnail(url=ctx.guild.icon_url)
		e.add_field(name='Status', value='\n'.join(str(status) for status in statuses))
		e.add_field(name='Amount', value='\n'.join(str(count) for status, count in statuses.items()))
		await ctx.send(embed=e)

def setup(bot):
	bot.add_cog(Fun(bot))
