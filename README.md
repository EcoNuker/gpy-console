# guilded.py-console
guilded.py console is a command line tool that allows you to control your bot and execute commands,  
so you can **use your Bot in the terminal/console** and run Guilded commands as usual.


### Installation
----------

#### Windows
`py -3 -m pip install discord.py-Console`

#### Linux/macOS
`python3 -m pip install discord.py-Console`


### Usage and Example
----------

The implementation is similar to the regular commands in guilded.py.
Just implement the guilded.py-console like this:

```python
import discord
from gpyConsole import Console

client = guilded.Client(features=guilded.Features(official_markdown = True))
my_console = Console(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@my_console.command()
async def hey(user: str):  # Library automatically converts type annotations, just like in guilded.py
    """
    Library can handle both synchronous or asynchronous functions
    """
    user = await client.fetch_user(user)
    print(f"Sending message to {user.name} id: = {user.id}")
    await user.send(f"Hello from Console Im {client.user.name}")


my_console.start() # Starts console listener
client.run("gapi_token")
```
To execute the mentioned command run ``hey <valid_user_id>``.


### Links and Infos
This is a fork of discord.py-Console.

TODO: Add error handling
