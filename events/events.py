import discord
from commands import *
from events.timings import Timeout


class Events:
    def __init__(self, client: discord.client.Client) -> None:
        self.client = client
        self.command = Command()
        self.started = False

        @self.client.event
        async def on_ready():
            print(f"You've been logged as {self.client.user}")

        @client.event
        async def on_message(msg: discord.message) -> None:
            if msg.author == self.client.user: return

            if msg.content.lower().startswith("pijemy"):
                await self.command.start(msg, self.started)
                if not self.started: await wait_for_reaction(msg)
            else:
                await self.command.run(msg)

        async def wait_for_reaction(msg: discord.message):
            def check(reaction, user) -> bool:
                return user == self.command.game_master and str(reaction.emoji) in "✅🍻❌"

            try:
                reaction, user = await self.client.wait_for(
                    "reaction_add",
                    check=check,
                    timeout=Timeout.seconds()
                )
            except asyncio.TimeoutError:
                await self.command.finish()
                return

            emoji = str(reaction.emoji)
            if emoji == "✅":
                await self.command.start_new_queue()
            elif emoji == "❌":
                await self.command.finish()
            elif emoji == "🍻":
                await self.command.drink_queue()
                await self.command.start_new_queue()
            await wait_for_reaction(self.command.previous_message)
