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
    "gapi_token"
)
```
To execute the mentioned command run ``hey <valid_channel_id> <valid_user_id>``.


## `🔗` Links

*No links currently*
