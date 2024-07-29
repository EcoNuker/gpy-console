import guilded
from gpyConsole import ConsoleBot
from gpyConsole.context import Context

client = ConsoleBot(
    command_prefix="!",
    features=guilded.ClientFeatures(official_markdown=True),
)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.console_command()
async def hey(
    ctx: Context,  # Modified Console Context with less features (.reply and .send are the same)
    channel: guilded.ChatChannel,
    user: guilded.User,
):  # Library automatically converts type annotations, just like in guilded.py
    # Missing converters: guilded.Role, guilded.Member, guilded.ChatMessage
    await ctx.reply(f"Sending message to {user.name} (id: {user.id})")
    await channel.send(
        f"Hello from Console! I'm {client.user.name}, and you are {user.mention}"
    )


client.start_console()  # Starts console listener
client.run(
    "gapi_g3ApoXCAoHXpEda7YvyU2KPHLepbBxHHIv0sdA7nnkJ5Gt353rFuDlWq8RdlYmer9C58jaTCXKjPjtcCcBLwgA=="
)
