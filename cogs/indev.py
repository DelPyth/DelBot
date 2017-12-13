# THESE ARE COMMANDS THAT I HAVE DISCARDED, EITHER FOR ERRORS I CAN'T SOLVE MYSELF
# OR I WAS WANTING TO USE THEM, BUT GREW TIRED OF TRYING TO GET IT TO WORK

'''
def lyrics(artist, song):
	artist = artist.lower()
	song = song.lower()
	artist = re.sub('[^A-Za-z0-9]+', "", artist)
	song = re.sub('[^A-Za-z0-9]+', "", song)
	raw_html = urllib.urlopen("http://azlyrics.com/lyrics            /"+str(artist)+"/"+str(song)+".html")
	html_copy = str(raw_html.read())
	split = html_copy.split('<!-- Usage of http://azlyrics.com     content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->', 1)
	split_html = split[1]
	split = split_html.split('</div>', 1)
	lyrics = split[0]
	lyrics = re.sub('(<.*?>)', "", lyrics)

	return lyrics
'''

'''
@commands.command()
async def lyrics(self, ctx, artist, song):
	await ctx.send(f"```\n{lyrics(artist, song)}\n```")
'''

'''
# Disabled until updated

@commands.command(aliases=['def'])
async def define(self, ctx, *, query):
	# Define a word using Oxfords dictionary

	await ctx.trigger_typing()

	req = requests.get('https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + query.split('\n')[0].lower(), headers={'Accept': 'application/json', 'app_id': self.oxford[0], 'app_key': self.oxford[1]})

	try:
		info = json.loads(req.text)
	except:
		return await ctx.send("Couldn't process query.")

	result = info['results'][0]
	entry = result['lexicalEntries'][0]

	word = result['word']
	type = entry['lexicalCategory']
	desc = entry['entries'][0]['senses'][0]['definitions'][0]

	word = word[:1].upper() + word[1:]
	desc = desc[:1].upper() + desc[1:]

	embed = discord.Embed(title=f'{word} ({type})', description=f'```{desc}```')
	embed.set_footer(text='Oxford University Press', icon_url='https://i.imgur.com/7GMY4dP.png')

	await ctx.send(embed=embed)
'''
