from gpyConsole import console_commands
from guilded.ext import commands


class ExampleCog(console_commands.ConsoleCog):
    def __init__(self, bot: console_commands.ConsoleBot):
        self.bot = bot

    @console_commands.console_command()
    async def hello(self, ctx: console_commands.Context):
        return await ctx.reply("Hello from cog!")

    @commands.command()
    async def wow(self, ctx: commands.Context):
        await ctx.send("Wow! Cog worked!")


def setup(bot: console_commands.ConsoleBot):
    bot.add_cog(ExampleCog(bot))
