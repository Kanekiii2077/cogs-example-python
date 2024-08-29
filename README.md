# cogs-example-python
In this repository, I will show an example of cogs in python

Create a file “main.py” (or other name), then create a folder “Cogs” in which will be our commands and events.

In the “main.py” file  import only OS and disnake(or discord.py). give prefix, write intents, remove help command if necessary. Next, we do a subload of the cogs

```
@bot.command()
async def load(ctx, extension):
	# Put your Discord ID here
	if ctx.author.id == ID:
		# And now we're making a function to load the cogs
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs.") # You can write anything you want here.
	else:
		ctx.send("You are not a bot developer!")
```

It's exactly the same here, but instead of load, we write unload

```
@bot.command()
async def unload(ctx, extension):
	if ctx.author.id == ID:
		bot.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs.")
	else:
		ctx.send("You are not a bot developer!")
```

Restart cogs

```
@bot.command()
async def reload(ctx, extension):
	if ctx.author.id == ID:
		# Here, instead of reload, we write unload and load
		bot.unload_extension(f"cogs.{extension}")
		bot.load_extension(f"cogs{extension}")
		await ctx.send("Cogs.")
	else:
		ctx.send("You are not a bot developer!")
```

Indicate where the cogs are

```
for filename in os.listdir("./cogs"):
```

File check. If the file ends in .py, then we load this cog

 ```
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")
```

Writing a token for our bot and moving on to the cogs

```
bot.run("YOUR TOKEN")
```

### Cogs\evemts.py

Importing our libraries for events. Since this is a tutorial, I am only writing the disnake library

```
import disnake
from disnake.ext import commands
```

Create Events class for bot's events
```
class Events(commands.Cog):

	def __init__(self, bot): # Now in each function we create, we add self
		self.bot = bot
```

To create an Event, we write this line.
```
 @commands.Cog.listener()
	async def on_ready(self): # You don't need anything for on_ready, but you should still specify self.
		print("Start!")
```

Now we're loading the cogs

```
def setup(bot):
	bot.add_cog(Events(bot))
```

### Cogs\user.py

Now let's do commands. You can divide the commands by their functionality, moderator commands in one file, for normal members in another, and for games in another
Importing our libraries, I'll try to make a command that will send a random number

```
import disnake
from disnake.ext import commands

from random import randint
```

Create Events class for user commands

```
class UserCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
```

To create a commands, we write the easy line
```
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
```

Now we're loading the cogs

```
def setup(bot):
	bot.add_cog(UserCommands(bot))
```


### That`s it, Bye!
