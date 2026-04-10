import discord
from discord.ext import commands
import discord.utils

intents = discord.Intents.default()
intents.message_content = True
discord.AllowedMentions(everyone = False, replied_user = True)

bot = commands.Bot(command_prefix=['!', '.'], intents=intents) # add or change any prefixes you want


@bot.group(aliases=['colour']) # gotta accommodate the brits
async def color(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Color Help",
                      colour=0xdd8cff)
        embed.add_field(name=".color / .colour:",
                value="Commands to create and change the color of your user role. The role's name is your username at the time of role creation, and username changes do not carry across to the role.",
                inline=False)
        embed.add_field(name=".color set <hex color>",
                value="Set your color role with a given hex code.\n Example usage: `.color set #dd8cff`",
                inline=False)
        embed.add_field(name=".color change <hex color>",
                value="Change your current color role to a different color.\n Example usage: ``.color change #607bd1``",
                inline=False)

        await ctx.send(embed=embed)


@color.command()
async def set(ctx, color):
    await ctx.guild.create_role(name=ctx.message.author.name, colour=discord.Colour.from_str(color))
    await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name=ctx.message.author.name))
    await ctx.send("Role created") 

@color.command()
async def change(ctx, color):
    role = discord.utils.get(ctx.guild.roles, name=ctx.message.author.name)
    await role.edit(colour=discord.Colour.from_str(color))
    await ctx.send("Role color changed") 

@color.command()
async def delete(ctx, *, role):
    role = discord.utils.get(ctx.message.guild.roles, name=ctx.message.author.name)
    await role.delete()
    await ctx.send(f"{ctx.message.author.name}'s color role has been deleted.")


@color.error()
async def color(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == 'color':
            await ctx.send("Error: You must include a color in hex format!")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Error: I do not have permissions to manage roles!")


bot.run('token')
