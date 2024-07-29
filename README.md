# `⌨️` Guilded.py console
>[!NOTE]
> Guilded.py console is a fork of [Discord.py Console](https://github.com/Mihitoko/discord.py-Console/) and uses its source code.

Guilded.py console is a CLI for your Guilded.py bot, with Guilded.py console you can run commands right from your console!


## `📥` Installation

### `🪟` Windows
`py -3 -m pip install gpy-console`

### `🍎` Linux/macOS
`python3 -m pip install gpy-console`


## `⚙️` Example

The implementation is similar to the regular commands in guilded.py.
Just implement the gpy-console like this:

```python
import guilded
from gpyConsole import ConsoleClient
from gpyConsole.context import Context

client = ConsoleClient(
    features=guilded.ClientFeatures(official_markdown=True),
)


@client.event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not bot._console_running:
        bot.start_console()


@client.console_command()
async def hey(
    ctx: Context,  # Modified Console Context with less features (.reply and .send are the same)
    channel: guilded.ChatChannel,
    user: guilded.User,
):  # Library automatically converts type annotations, just like in guilded.py
    # Missing converters: guilded.Role, guilded.Member, guilded.ChatMessage, guilded.Attachments
    await ctx.reply(f"Sending message to {user.name} (id: {user.id})")
    await channel.send(
        f"Hello from Console! I'm {client.user.name}, and you are {user.mention}"
    )

client.run(
    "gapi_token"
)
```
To execute the mentioned command run ``hey <valid_channel_id> <valid_user_id>``.


## `🔗` Links

*No links currently*

# gpyConsole: things to know

The console has to be started manually. Try something like this:
```python
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not bot._console_running:
        bot.start_console()
```

### Missing Converters
Any converter that relies on the local server will not be available. This includes:
- guilded.Role
- guilded.Member
- guilded.ChatMessage
- guilded.Attachment

### New Events
New events were added that are accessible like any other guilded.py event.
- `on_console_command_completion`
- `on_console_command`
- `on_console_command_error`
- `on_console_message`

### Console Cogs
All cogs should be replaced with a ConsoleCog; it implements guilded.py's Cog feature so it will work the same.

### You can stop the console

```python
if bot._console_running:
    bot.stop_console()
```