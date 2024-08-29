# Importing our libraries for events. Since this is a tutorial, I am only writing the disnake library

import disnake
from disnake.ext import commands

# Create Events class for bot's events
class Events(commands.Cog):

	def __init__(self, bot): # Now in each function we create, we add self
		self.bot = bot

# To create an Event, we write this line.
	@commands.Cog.listener()
	async def on_ready(self): # You don't need anything for on_ready, but you should still specify self.
		print("Start!")


# Now we're loading the cogs
def setup(bot):
	bot.add_cog(Events(bot))