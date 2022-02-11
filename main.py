import discord
from password import TOKEN
import events as ev


def main():
    client = discord.Client()

    events = ev.Events(client)
    client.run(TOKEN)


if __name__ == "__main__":
    main()
