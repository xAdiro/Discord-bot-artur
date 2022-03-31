from email import message
from enum import Enum
from sys import flags
from discord import message as discord_message


class Command:
    def __init__(self, message: discord_message):
        self.__content = message.content.lower()
        self.value = self.__get_value(self.__content)
        self.cmd_type = None

        if self.__content.startswith('$dodaj('):
            self.cmd_type = Commands.ADD_QUEUE

        if self.__content.startswith('$czas_kolejki('):
            self.cmd_type = Commands.SET_QUEUE_FREQUENCY

        if self.__content.startswith('pijemy'):
            self.cmd_type = Commands.START

    def __get_value(self, message: str) -> float:
        try:
            new_time = int(message.replace('$czas_kolejki(', '').replace(')', ''))
        except Exception:
            new_time = None
        return new_time


class Commands(Enum):
    ADD_QUEUE = 1
    SET_QUEUE_FREQUENCY = 2
    START = 3
