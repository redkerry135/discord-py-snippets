import discord
from discord.ext import commands
import discord.utils

intents = discord.Intents.default()
intents.message_content = True
discord.AllowedMentions(everyone = False, replied_user = True)

bot = commands.Bot(command_prefix=['!', '.'], intents=intents) # add or change any prefixes you want


@bot.command()
async def avatar(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author
    embed = discord.Embed(title=f"{user.display_name}'s avatar:",
                          colour=0x00b0f4)   
    embed.set_image(url=f"{user.display_avatar.url}")
    await ctx.send(embed=embed)

@bot.command()
async def banner(ctx, user: discord.User = None):
    if user is None:
        user = ctx.author
    user = await bot.fetch_user(user.id)
    embed = discord.Embed(title=f"{user.display_name}'s banner:",
                          colour=0x00b0f4)   
    embed.set_image(url=f"{user.banner.url}")
    await ctx.send(embed=embed)


bot.run('token')