# Bot Artur
Artur is a discord party bot which task is to notify everyone regularly when there is a time for to drink their favourite bevarage. The project started as a joke but is now fully functional and I personally host it on one of my raspberry pis for private usage. Because of its origin it's only good to use at one server at a time(per account) as it wasn't anticipated for it to be used globally.

## Technologies used:
- Python 3
- Discord.py API

## Setting up
Firstly you need to [create your bot](https://docs.discord.red/en/stable/bot_application_guide.html) and [invite it to the server](https://docs.discordbotstudio.org/setting-up-dbs/inviting-a-bot-to-your-server)

In order for script to work you have to provide acces token to your bot account. You should put `password.py` in main folder and create string constant TOKEN containing your acces token like so:

###### /password.py: 
```python
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' 
```
Also you need to install discord api with:
```bash
pip install discord
```
After that you should be able to run `main.py` succesfully.
