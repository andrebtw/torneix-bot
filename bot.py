import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json
 
 
bot = commands.Bot(command_prefix = "t!")
 
@bot.event
async def on_ready():
	print ("Connected")

@bot.event
async def on_message(message):
	await bot.process_commands(message)
		
@bot.command(pass_context = True)
async def ping(ctx):
    resp = await bot.say('Ping :')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.say(f"{1000*diff.total_seconds():.1f}ms")
    print ("Ping")


#COLOR ROLES
#Black
@bot.command(pass_context=True)
async def black(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="BLACK")
	if "black" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : BLACK".format(ctx.message.author), color=0x000001)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : BLACK".format(ctx.message.author), color=0x000001)
		await bot.say(embed=embed)





#White
@bot.command(pass_context=True)
async def white(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="WHITE")
	if "white" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : WHITE".format(ctx.message.author), color=0xffffff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : WHITE".format(ctx.message.author), color=0xffffff)
		await bot.say(embed=embed)






#Blue
@bot.command(pass_context=True)
async def blue(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="BLUE")
	if "blue" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : BLUE".format(ctx.message.author), color=0x0000ff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : BLUE".format(ctx.message.author), color=0x0000ff)
		await bot.say(embed=embed)





#Cyan
@bot.command(pass_context=True)
async def cyan(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="CYAN")
	if "cyan" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : CYAN".format(ctx.message.author), color=0x00ffff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : CYAN".format(ctx.message.author), color=0x00ffff)
		await bot.say(embed=embed)






#Green
@bot.command(pass_context=True)
async def green(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="GREEN")
	if "green" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : GREEN".format(ctx.message.author), color=0x00ff00)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : GREEN".format(ctx.message.author), color=0x00ff00)
		await bot.say(embed=embed)








#Yellow
@bot.command(pass_context=True)
async def yellow(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="YELLOW")
	if "yellow" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : YELLOW".format(ctx.message.author), color=0xffff00)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : YELLOW".format(ctx.message.author), color=0xffff00)
		await bot.say(embed=embed)






#Orange
@bot.command(pass_context=True)
async def orange(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="ORANGE")
	if "orange" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : ORANGE".format(ctx.message.author), color=0xff6600)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : ORANGE".format(ctx.message.author), color=0xff6600)
		await bot.say(embed=embed)





#Red
@bot.command(pass_context=True)
async def red(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="RED")
	if "red" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : RED".format(ctx.message.author), color=0xff0000)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : RED".format(ctx.message.author), color=0xff0000)
		await bot.say(embed=embed)





#pink
@bot.command(pass_context=True)
async def pink(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="PINK")
	if "pink" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : PINK".format(ctx.message.author), color=0xfc2670)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : PINK".format(ctx.message.author), color=0xfc2670)
		await bot.say(embed=embed)

#purple
@bot.command(pass_context=True)
async def purple(ctx):
	user = ctx.message.author
	role = discord.utils.get(user.server.roles, name="PURPLE")
	if "pink" in [y.name.lower() for y in ctx.message.author.roles]:
		await bot.remove_roles(user,role)
		embed=discord.Embed(title="{}, COLOR REMOVED : PURPLE".format(ctx.message.author), color=0x8800ff)
		await bot.say(embed=embed)
	else :
		await bot.add_roles(user, role)
		embed=discord.Embed(title="{}, COLOR ADDED : PURPLE".format(ctx.message.author), color=0x8800ff)
		await bot.say(embed=embed)








		

       
bot.run(os.getenv("TOKEN"))

