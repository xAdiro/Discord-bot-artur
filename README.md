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
After that you should be able to run `main.py` succesfully, after which you can start drinking event by typing `pijemy` (it's not case sensitive) 

## Default values and changing them
By default there is 15 minute interval set between each queue taken and 2 hours inactivity time before bot ends event. These can be changed in code in `/events/timings.py/` but queue interval can be also changed with command
### Commands
- $czas_kolejki(`time`) - which changes queue interval to `time` expressed in seconds
- $dodaj(`queues`) - adds `queues` number to current number of them
