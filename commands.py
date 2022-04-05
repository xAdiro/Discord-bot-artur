from email import message
import asyncio
from enum import Enum
from discord import message as discord_message
import speaking as speak
import custom_time as time
import events.timings as frequency


class Commands(Enum):
    ADD_QUEUE = 1
    SET_QUEUE_FREQUENCY = 2
    START = 3
    START_NEW_QUEUE = 4
    ALREADY_STARTED = 5
    FINISH = 6
    DRINK_QUEUE = 7


class Command:
    def __init__(self, msg: discord_message):
        self.__content = msg.content.lower()
        self.value = self.__get_value(self.__content)

        self.game_master = None
        self.cmd_type = None
        self.channel = None
        self.queue_number = 1
        self.previous_message = None
        self.time_started = None

        self.__set_type()

    async def run(self, command: Commands, msg: discord_message):
        if command == Commands.START:
            self.previous_message = await speak.greeting(msg, msg.author.id)
            self.channel = msg.channel
            self.game_master = msg.author
            self.time_started = time.date_time()

        elif command == Commands.SET_QUEUE_FREQUENCY:
            frequency.QUEUE_TIME_SECONDS = command.value
            print(f"Ustawiono czas kolejki na: {command.value} sekund")

        elif command == Commands.ADD_QUEUE:
            self.queue_number += command.value
            print("Dodano kolejke aktualna kolejka " + str(self.queue_number))

        elif command == Commands.DRINK_QUEUE:
            await speak.print_queue_taken(self.previous_message, self.queue_number)
            self.queue_number += 1
            await asyncio.sleep(frequency.Queue().seconds)

        elif command == Commands.ALREADY_STARTED:
            await speak.already_started(msg)
            
        elif command == Commands.START_NEW_QUEUE:
            # await asyncio.sleep(frequency.Queue().seconds)
            await self.previous_message.delete()
            new_message = await speak.new_queue(self.channel, self.queue_number, self.game_master.id)
            self.previous_message = new_message
            
        elif command == Commands.FINISH:
            await self.previous_message.delete()
            await speak.farewell(self.channel, self.queue_number, self.time_started)
            self.queue_number = 1
        else:
            await self.run(self.cmd_type, None)

    def set_new(self, msg: discord_message):
        self.__content = msg.content
        self.__set_type()

    def __get_value(self, msg: str) -> float:
        try:
            new_time = int(msg.replace('$czas_kolejki(', '').replace(')', ''))
        except Exception:
            new_time = None
        return new_time

    def __set_type(self):
        if self.__content.startswith('$dodaj('):
            self.cmd_type = Commands.ADD_QUEUE

        elif self.__content.startswith('$czas_kolejki('):
            self.cmd_type = Commands.SET_QUEUE_FREQUENCY

        elif self.__content.startswith('pijemy'):
            self.cmd_type = Commands.START
