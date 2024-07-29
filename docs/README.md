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