TOKEN = ''
#Imports
import asyncio
import discord
from discord.ext import commands
#Instanz aufsetzen
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", help_command=None, intents=intents)

@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        while True:
            try:
                target = await bot.fetch_user(user_id)
                await target.send(args)
                #Feedback
                await ctx.channel.send("'" + args + "' sent to: " + target.name)
                await asyncio.sleep(1)
            except:
                await ctx.channel.send("Couldn't dm the given user.")
    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")
#Bot mit Schlüssel Starten
bot.run(TOKEN)
