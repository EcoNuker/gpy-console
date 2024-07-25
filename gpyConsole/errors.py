__all__ = ("CommandNotFound", "CommandError", "ExtensionError")


class CommandNotFound(Exception):
    def __init__(self, command_name):
        self.name = command_name

    def __str__(self):
        return f"Command with name {self.name} not found"


class CommandError(Exception):
    r"""The base exception type for all command related errors.

    This inherits from :exc:`Exception`.

    This exception and exceptions inherited from it are handled
    in a special way as they are caught and passed into a special event
    from :class:`Console`\, :func:`on_console_command_error`.
    """

    def __init__(self, message=None, *args):
        if message is not None:
            # clean-up @everyone and @here mentions
            m = message.replace("@everyone", "@\u200beveryone").replace(
                "@here", "@\u200bhere"
            )
            super().__init__(m, *args)
        else:
            super().__init__(*args)


class ExtensionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
