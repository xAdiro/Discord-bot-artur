import asyncio
from discord import message as discord_message
import speaking as speak
import custom_time as time
import events.timings as frequency


class Command:
    def __init__(self):
        self.game_master = None
        self.channel = None
        self.queue_number = 1
        self.previous_message = None
        self.time_started = None

    async def start(self, msg, started=False):
        if not started:
            self.previous_message = await speak.greeting(msg, msg.author.id)
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
                Command.__set_queue_freq(content)
        except ValueError:
            Command.__add_error_reaction(msg)
        else:
            await msg.add_reaction("👌")

    async def drink_queue(self):
        await speak.print_queue_taken(self.previous_message, self.queue_number)
        self.queue_number += 1
        await asyncio.sleep(frequency.Queue().seconds)

    async def start_new_queue(self):
        await self.previous_message.delete()
        new_message = await speak.new_queue(self.channel, self.queue_number, self.game_master.id)
        self.previous_message = new_message

    async def finish(self):
        await self.previous_message.delete()
        await speak.farewell(self.channel, self.queue_number, self.time_started)
        self.queue_number = 1

    def __add_queue(self, msg_content: str):
        value = msg_content.replace('$dodaj(', '').replace(')', '')
        value = int(value)
        self.queue_number += value

    @staticmethod
    def __set_queue_freq(msg_content: str):
        value = msg_content.replace('$czas_kolejki(', '').replace(')', '')
        value = int(value)
        frequency.QUEUE_TIME_SECONDS = value

    @staticmethod
    def __add_error_reaction(msg):
        msg.add_reaction("❓")
        print("Błąd w poleceniu")
