import guilded
from guilded.ext import commands
from gpyConsole import ConsoleBot
from gpyConsole.context import Context

bot = ConsoleBot(
    command_prefix="!",
    features=guilded.ClientFeatures(official_markdown=True),
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_console_message(message: str):
    print(f"Received command: {message}")


@bot.console_command()
async def hey(
    ctx: Context,  # Modified Console Context with less features (.reply and .send are the same)
    channel: guilded.ChatChannel,
    user: guilded.User,
):  # Library automatically converts type annotations, just like in guilded.py
    # Missing converters: guilded.Role, guilded.Member, guilded.ChatMessage, guilded.Attachment
    await ctx.reply(f"Sending message to {user.name} (id: {user.id})")
    await channel.send(
        f"Hello from Console! I'm {bot.user.name}, and you are {user.mention}"
    )

@bot.command()
async def hi(
    ctx: commands.Context
):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(
    "gapi_g3ApoXCAoHXpEda7YvyU2KPHLepbBxHHIv0sdA7nnkJ5Gt353rFuDlWq8RdlYmer9C58jaTCXKjPjtcCcBLwgA=="
)
