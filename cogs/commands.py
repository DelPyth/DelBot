import discord
from discord.ext import commands

# I wouldn't worry if you don't have these, just make sure you have the newest version of PYTHON
# and you're good to go!
import re, time, math, json, string, random, asyncio, datetime, traceback

class Commands:
	"""Contains standard commands"""

	def __init__(self, bot):
		self.bot = bot

		#self.bot.remove_command('help')

		self.time = time.time()
		self.reptime = {}
		self.replies = {
			'\o': 'o/',
			'o/': '\o',
			'/)': '(\\',
			'(\\': '/)'
		}

	async def on_message(self, message):
		if message.author.bot:
			return

		if message.content in self.replies:
			ctx = await self.bot.get_context(message)
			await ctx.send(self.replies[message.content])

	@commands.command(name='8')
	async def ball(self, ctx, question):
		"""Classic Magic 8 Ball"""
		responses = (
			# yes
				'It is certain',
				'It is decidedly so',
				'Without a doubt',
				'Yes definitely',
				'You may rely on it',
				'As I see it, yes',
				'Most likely',
				'Outlook good',
				'Yes',
			# uncertain
				'Signs point to yes',
				'Reply hazy try again',
				'Ask again later',
				'Better not tell you now',
				'Cannot predict now',
				'Concentrate and ask again',
			# no
				"Don't count on it",
				'My reply is no',
				'My sources say no',
				'Outlook not so good',
				'Very doubtful'
		)
		await ctx.trigger_typing()
		await asyncio.sleep(3)
		await ctx.send(random.choice(responses))

	@commands.command()
	async def choose(self, ctx, *choices):
		"""Choose from a list."""
		items = [
			"Hmm... I'll pick...",
			"Tough decision... I'll go with",
			"Oh, uh...",
			"I'll take",
			"How about...",
			"Maybe...",
			"Let's go with"
		]
		await ctx.trigger_typing()
		await asyncio.sleep(1)
		await ctx.send(random.choice(items) + " " + random.choice(choices))

	@commands.command()
	async def coin(self, ctx):
		"""Flip a coin!"""
		await ctx.send("I got " + random.choice(['Heads', 'Tails']) + '!')

	@commands.command(hidden=True)
	async def info(self, ctx):
		"""Some info about the bot"""
		await ctx.send(f'```{self.bot.description}\n\nFramework: discord.py {discord.__version__}\nAuthor: Delta Pythagorean```')

	@commands.command(hidden=True)
	async def uptime(self, ctx):
		"""Check how long the bot's been online since last load time"""
		sec = time.time() - self.time
		seconds = math.floor(sec % 60)
		minutes = math.floor(sec/60 % 60)
		hours = math.floor(sec/60/60 % 24)
		days = math.floor(sec/60/60/24)
		await ctx.send('{}d {:02d}:{:02d}:{:02d}'.format(days, hours, minutes, seconds))

	@commands.command(hidden=True)
	async def source(self, ctx):
		"""Get the source to this bot!"""
		await ctx.send('`Coming soon...`')

	@client.command(pass_context=True)
	async def ping(ctx):
		"""This isn't a ping pong game... I wish it was..."""
		now = datetime.datetime.utcnow()
		delta = now-ctx.message.timestamp
		await client.say(f'Pong! {delta(microseconds=1)}ms')

def setup(bot):
	bot.add_cog(Commands(bot))
