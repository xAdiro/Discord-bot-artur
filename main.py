import discord
from password import TOKEN
import events.events as ev


def main():
    client = discord.Client()

    ev.Events(client)
    client.run(TOKEN)


if __name__ == "__main__":
    main()
