import abc

from . import ConsoleBot, ConsoleClient

from typing import Union


class ConsoleMessageable(metaclass=abc.ABCMeta):
    """An ABC for models that messages can be sent to.

    The following implement this ABC:

        * :class:`.ext.commands.Context`
    """

    def __init__(self, *, client: Union[ConsoleClient, ConsoleBot]):
        self.client = client
        self.server: None = None
        self.channel: None = None

    async def send(
        self,
        content: str,
    ) -> str:
        """|coro|

        Send a message to the console.

        Parameters
        -----------
        content: :class:`str`
            The text content to send with the message.
        """
        out = self.client.out
        out.write(content + "\n")
        out.flush()  # Ensure the message is written to the console immediately
        return content
