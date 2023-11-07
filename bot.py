import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)
bot.remove_command("help")

@bot.command()
async def role(ctx, target: discord.Member):
    author = target
    guild = bot.get_guild(1067554815690952835)
    role = guild.get_role(1067827586534744115)

    await author.add_roles(role)

@bot.event
async def on_ready():
    print("Бот готов!")

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Streaming(
            name="Helper 1.0.2", url="https://www.twitch.tv/twitch"
        ),
    )

bot.run('token')