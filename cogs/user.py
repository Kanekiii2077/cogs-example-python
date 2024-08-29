# Now let's do commands. You can divide the commands by their functionality, moderator commands in one file, for normal members in another, and for games in another
# Importing our libraries, I'll try to make a command that will send a random number

import disnake
from disnake.ext import commands

from random import randint

# Create Events class for user commands

class UserCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	# To create a commands, we write the easy line
	@commands.command(
		# You can give the command name, description and alternate names
		name = "random",
		aliases = ["number", "rand_number"],
		brief = "This command will give you a random number between 1 and 100"
	)
	# And then we do the same as with a normal command
	async def random(self, ctx):
		embed = disnake.Embed(
			title= "Random number",
			description = f"Random number - {randint(0,100)}",
			color = 3447003
		)
		await ctx.send(embed=embed)

# Now we're loading the cogs
def setup(bot):
	bot.add_cog(UserCommands(bot))