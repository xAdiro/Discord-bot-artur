import discord
from password import TOKEN
from events.events import Events


def main():
    client = discord.Client()
    Events(client)
    client.run(TOKEN)


if __name__ == "__main__":
    main()
