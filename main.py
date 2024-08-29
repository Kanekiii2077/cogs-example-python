# Import only OS and disnake(or discord.py)
import os

import disnake
from disnake.ext import commands

# 
bot = commands.Bot(command_prefix = "!", help_command = None,  intents = disnake.Intents.all())

# Next, we do a subload of the cogs

@bot.command()
async def load(ctx, extension):
	# Put your Discord ID here
	if ctx.author.id == ID:
		# And now we're making a function to load the cogs
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs.") # You can write anything you want here.
	else:
		ctx.send("You are not a bot developer!")

# It's exactly the same here, but instead of load, we write unload
@bot.command()
async def unload(ctx, extension):
	if ctx.author.id == ID:
		bot.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs.")
	else:
		ctx.send("You are not a bot developer!")

# Restart cogs
@bot.command()
async def reload(ctx, extension):
	if ctx.author.id == ID:
		# Here, instead of reload, we write unload and load
		bot.unload_extension(f"cogs.{extension}")
		bot.load_extension(f"cogs{extension}")
		await ctx.send("Cogs.")
	else:
		ctx.send("You are not a bot developer!")


# Indicate where the cogs are
for filename in os.listdir("./cogs"):
	# File check. If the file ends in .py, then we load this cog
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")


bot.run("YOUR TOKEN")


# Moving on to the cogs