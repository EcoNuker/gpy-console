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

client = guilded.Client(features=guilded.ClientFeatures(official_markdown = True))
client = Console(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.console_command()
async def hey(user: str):  # Library automatically converts type annotations, just like in guilded.py
    """
    Library can handle both synchronous or asynchronous functions
    """
    user = await client.fetch_user(user)
    print(f"Sending message to {user.name} id: = {user.id}")
    await user.send(f"Hello from Console Im {client.user.name}")


client.start_console()
client.run("gapi_token")
```
To execute the mentioned command run ``hey <valid_user_id>``.


## `🔗` Links

*No links currently*
