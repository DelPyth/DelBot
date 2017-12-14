"""
	=========================================================================
	Title:							DelBot
	=========================================================================
	Descrition:						DelBot is a friendly, fun bot made just
									for enjoyment. Whether it's kissing a
									friend, or shoving a muffin into their
									mouth!
	=========================================================================
	PYTHON Version:					3.6.3
	Language Used:					English
	Used Platform(s):				Windows
	Author:							Delta
	Contact information:			octalblockmc@gmail.com
	=========================================================================
"""

import os, sys
import discord
import json
from discord.ext import commands

# You can change the prefix if you do choose to
# Just make sure that it makes sense
bot = commands.Bot(command_prefix='.', description="Delta's Bot")

bot.description = '"Just a Hero for Fun" - Saitama'

bot.owner_id = # <YOUR_USER_ID_HERE> Usually 18 characters, all numbers

bot.info = {}

# This changes the bot's nickname, not username, on all servers that it's linked to apon running.
bot.info['nick'] = 'DelBot'

# This is just for fun for some of the servers I'm on.
bot.info['status'] = 'With Ponies!'

# These are all your "mods" to the bot. To add one, specify the location like you would for a file
# except, change the `\` to a `.`
extensions = (
	'cogs.commands',
	'cogs.fun',
	'cogs.admin',
	'cogs.roles'
)

@bot.event
async def on_ready():
	await bot.user.edit(username=bot.info['nick'])
	await bot.change_presence(game=discord.Game(name=bot.info['status']))

	# The following is for WINDOWS ONLY.
	# If you are running OSX or LINUX
	# You must change them accordingly.
	# It won't break the bot, but it is useful to have a cleared screen off all "debris"
	os.system("cls")

	# The following block of commands show information about "your" bot
	# It will also show any extentions it has loaded.
	# If you don't see an extention that you wanted to load, please make sure you specified the paths correctly,
	# and you have saved both this file and your extention.
	if __name__ == '__main__':
		print(f'Logged in as: {bot.user.name} (ID: {bot.user.id})\nDiscord.py Version: {discord.__version__}\n')
		print(f'Your Python Version: {__version__}\n')
		for extension in extensions:
			print(f'Loading extension: "{extension}"')
			bot.load_extension(extension)

	# The following is purely cosmetic.
	# but is is useful to know what servers your bot is logged into.
	print(f'\nConnected to {len(bot.guilds)} servers:')
	print('=================================================================')
	print('\n'.join(f'{guild.name}:\n\t{guild.id}' for guild in bot.guilds))
	print('=================================================================')

# The following function (Non-callable by user, but the bot will call it on an error thrown)
# will throw the error into chat instead of your console, any errors that are PYTHON related
# are thrown to the console, syntax errors, modules not existing, etc etc
@bot.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.CommandNotFound):
		return

	# if isinstance(error, commands.CommandInvokeError):
	#	return print(error)

	errors = {
		commands.DisabledCommand: 'Command has been disabled.',
		commands.MissingPermissions: 'Invoker is missing permissions to run this command.',
		commands.BotMissingPermissions: 'Bot is missing permissions to run this command.'
	}

	for type, text in errors.items():
		if isinstance(error, type):
			return await ctx.send(errors[type])

	# argument error
	if isinstance(error, commands.UserInputError):
		bot.formatter.context = ctx
		bot.formatter.command = ctx.command
		return await ctx.send(f'Invalid argument(s) provided.\n```{bot.formatter.get_command_signature()}```')

	await ctx.send(f'An error occured in `{ctx.command.name}` invoked by {ctx.message.author}:\n```{error}```')
	#traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)

# overwrite discord.Embed with a monkey patched class that automatically sets the color attribute
# This is just cosmetic, but you can change the color yourself.
# Just change the hex number it what ever color you'd like.
# Remember, it must be in Hexidecimal form.
class Embed(discord.Embed):
	def __init__(self, color=0x4245ff, **attrs):
		attrs['color'] = color
		super().__init__(**attrs)

discord.Embed = Embed

# This is where your bot token is located.
# if you don't know your token, go to: https://discordapp.com/developers/applications/me
# choose the bot you want to use (Or create one)
# and copy and paste your token into the file.
"""
	==========================================================================
	DO NOT GIVE YOUR TOKEN TO ANYONE ELSE BESIDES PEOPLE YOU **REALLY** TRUST!
	==========================================================================
"""
with open("cfg/token.txt", "r") as file:
	bot.run(file.read())
