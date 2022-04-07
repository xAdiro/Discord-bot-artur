import asyncio

from discord import message as discord_message

from events.speaking import speaking as speak
from utilities import custom_time as time
from events.timings import Queue as QueueFreq


class Command:
    def __init__(self):
        self.game_master = None
        self.channel = None
        self.queue_number = 1
        self.previous_message = None
        self.time_started = None
        self.queue_freq = QueueFreq()

    async def start(self, msg: discord_message, started=False):
        if not started:
            self.previous_message = await speak.greeting(msg, msg.author.id, self.queue_freq)
            self.channel = msg.channel
            self.game_master = msg.author
            self.time_started = time.date_time()
        else:
            await speak.already_started(msg)

    async def run(self, msg: discord_message):
        if msg.author != self.game_master: return

        content = msg.content
        try:
            if content.startswith('$dodaj('):
                self.__add_queue(content)
            elif content.startswith('$czas_kolejki('):
                self.__set_queue_freq(content)
            else:
                return
        except ValueError:
            Command.__add_error_reaction(msg)
        else:
            await msg.add_reaction("👌")

    async def drink_queue(self):
        await speak.print_queue_taken(self.previous_message, self.queue_number, self.queue_freq)
        self.queue_number += 1
        await asyncio.sleep(self.queue_freq.seconds)

    async def start_new_queue(self):
        await self.previous_message.delete()
        new_message = await speak.new_queue(
            self.channel, self.queue_number, self.queue_freq, self.game_master.id)
        self.previous_message = new_message

    async def finish(self):
        if self.previous_message is not None: await self.previous_message.delete()
        await speak.farewell(self.channel, self.queue_number, self.time_started)
        self.queue_number = 1

    def __add_queue(self, msg_content: str):
        value = msg_content.replace('$dodaj(', '').replace(')', '')
        value = int(value)
        self.queue_number += value

    def __set_queue_freq(self, msg_content: str):
        value = msg_content.replace('$czas_kolejki(', '').replace(')', '')
        value = int(value)
        self.queue_freq.seconds = value

    @staticmethod
    def __add_error_reaction(msg):
        msg.add_reaction("❓")
        print("Błąd w poleceniu")
