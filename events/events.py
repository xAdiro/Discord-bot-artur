import asyncio
import discord
from commands import *


class Events:
    def __init__(self, client: discord.client.Client) -> None:
        self.client = client
        self.command = None
        self.started = False

        @self.client.event
        async def on_ready():
            print(f"You've been logged as {self.client.user}")

        @client.event
        async def on_message(msg: discord.message) -> None:
            if msg.author == self.client.user:
                return

            if msg.content.lower().startswith("pijemy"):
                if self.started:
                    await self.command.run(Commands.ALREADY_STARTED, msg)
                else:
                    self.started = True
                    self.command = Command(msg)
                    await self.command.run(Commands.START, msg)
                    await wait_for_reaction(msg)
                return

            # if msg.author != self.game_master: return  # ignore commands not from game master
            self.command.run(msg)

        async def wait_for_reaction(msg: discord.message):
            def check(reaction, user) -> bool:
                return user == self.command.game_master and str(reaction.emoji) in "✅🍻❌"

            try:
                reaction, user = await self.client.wait_for("reaction_add", check=check,
                                                            timeout=frequency.Timeout().seconds)  # 2 hours
            except asyncio.TimeoutError:
                await self.command.run(Commands.FINISH)
                return ""

            emoji = str(reaction.emoji)
            if emoji == "✅":
                await self.command.run(Commands.START_NEW_QUEUE, None)
            elif emoji == "❌":
                await self.command.run(Commands.FINISH, None)
            elif emoji == "🍻":
                await self.command.run(Commands.DRINK_QUEUE, None)
                await self.command.run(Commands.START_NEW_QUEUE, None)
            await wait_for_reaction(self.command.previous_message)
