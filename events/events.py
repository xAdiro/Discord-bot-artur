import asyncio
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
import discord
import speaking as speak
import custom_time as time
import events.timings as frequency
from commands import *


class Events:
    def __init__(self, client: discord.client.Client) -> None:
        self.client = client
        self.game_master = None
        self.channel = None
        self.started = False
        self.queue_number = 1
        self.previous_message = None
        self.time_started = None

        @self.client.event
        async def on_ready():
            print(f"You've been logged as {self.client.user}")

        @client.event
        async def on_message(message: discord.message) -> None:
            if message.author == self.client.user:
                return

            if command == Commands.START:
                if self.started:
                    await speak.already_started(message)
                else:
                    await start(message)

            if message.author != self.game_master: # ignore commands not from game master
                return


            command = Command(message)

            if command.cmd_type == Commands.ADD_QUEUE:
                self.queue_number += command.value
                print("Dodano kolejke aktualna kolejka " + str(self.queue_number))
                return

            if command.cmd_type == Commands.SET_QUEUE_FREQUENCY:
                frequency.QUEUE_TIME_SECONDS = command.value
                print(f"Ustawiono czas kolejki na: {command.value} sekund")
                return


        async def start(message: discord.message) -> None:
            self.previous_message = await speak.greeting(message, message.author.id)
            self.started = True
            self.channel = message.channel
            self.game_master = message.author
            self.time_started = time.full()

            await wait_for_reaction(message)

        async def start_new_queue(wait=False):
            if wait:
                await asyncio.sleep(frequency.Queue().seconds)  # 15 minutes

            await delete_previous_message()
            my_message = await speak.new_queue(self.channel, self.queue_number, self.game_master.id)
            self.previous_message = my_message
            await wait_for_reaction(my_message)

        async def finish():
            await delete_previous_message()
            await speak.farewell(self.channel, self.queue_number, self.time_started)
            self.queue_number = 1
            self.started = False

        async def delete_previous_message():
            await self.previous_message.delete()

        async def wait_for_reaction(message: discord.message):
            def check(reaction, user) -> bool:
                return user == self.game_master and str(reaction.emoji) in "✅🍻❌"

            try:
                reaction, user = await self.client.wait_for("reaction_add", check=check,
                                                            timeout=frequency.Timeout().seconds)  # 2 hours
            except asyncio.TimeoutError:
                await finish()
                return ""

            emoji = str(reaction.emoji)
            if emoji == "✅":
                await start_new_queue()
            elif emoji == "❌":
                await finish()
            elif emoji == "🍻":
                self.queue_number += 1
                await speak.print_queue_taken(message, self.queue_number - 1)
                await start_new_queue(wait=True)
