import asyncio

import discord
import actions as action

TIMEOUT_TIME = 7200  # 2 hours
QUEUE_TIME = 900  # 15 minutes


class Events:
    started = False
    client = discord.client
    game_master = None
    channel = None
    queue_number = 1
    previous_message = None

    def __init__(self, client: discord.client.Client) -> None:
        self.client = client

        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')

        @client.event
        async def on_message(message: discord.message) -> None:
            if message.author == client.user:
                return

            if message.content.lower().startswith('pijemy'):
                if self.started:
                    await action.tell_already_started(message)
                else:
                    await start(message)

        async def start(message: discord.message) -> None:
            self.previous_message = await action.greeting(message, message.author.id)
            self.started = True
            self.channel = message.channel
            self.game_master = message.author
            await wait_for_reaction(message)

        async def start_new_queue(wait=False):
            if wait:
                await asyncio.sleep(QUEUE_TIME)  # 15 minutes

            await delete_previous_message()
            my_message = await action.new_queue(self.channel, self.queue_number, self.game_master.id)
            self.previous_message = my_message
            await wait_for_reaction(my_message)

        async def finish():
            await delete_previous_message()
            await action.finish(self.channel, self.queue_number)
            self.queue_number = 1
            self.started = False

        async def delete_previous_message():
            await self.previous_message.delete()

        async def wait_for_reaction(message: discord.message):
            def check(reaction, user):
                return user == self.game_master and str(reaction.emoji) in "✅🍻❌"

            try:
                reaction, user = await self.client.wait_for("reaction_add", check=check, timeout=TIMEOUT_TIME)  # 2 hours
            except asyncio.TimeoutError:
                # await message.channel.send(lines.TIMEOUT)
                await finish()
                return ""

            emoji = str(reaction.emoji)
            if emoji == "✅":
                await start_new_queue()
            elif emoji == "❌":
                await finish()
            elif emoji == "🍻":
                self.queue_number += 1
                await action.print_queue_taken(message, self.queue_number-1)
                await start_new_queue(wait=True)


