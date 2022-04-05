import discord

from events.speaking import spoken_lines as lines
from utilities import custom_time as time
from events.timings import Queue as QueueFreq


async def farewell(channel: discord.channel, queues_total: int, finishing_time: str) -> None:
    if queues_total-1 == 0:
        await channel.send(lines.FAREWELL_NO_QUEUES)
    else:
        await channel.send(lines.FAREWELL.format(
            finishing_time=time.date_time(),
            queues_total=queues_total-1,
            beginning_time=finishing_time))


async def already_started(message: discord.message) -> discord.message:
    await message.add_reaction('❓')
    my_message = await message.reply(lines.ALREADY_STARTED)
    return my_message


async def greeting(message: discord.message, tag_name: str) -> discord.message:
    await message.add_reaction('👌')
    my_message = await message.channel.send(lines.GREETING.format(user_id=tag_name))
    await my_message.add_reaction('✅')
    await my_message.add_reaction('❌')
    return my_message


async def new_queue(channel: discord.channel, queue_number: int, queue_freq: QueueFreq, tag_name: str) -> discord.message:
    my_message = await channel.send(lines.QUEUE.format(
        queue_frequency_minutes=queue_freq.minutes,
        user_id=tag_name,
        started_queue_number=queue_number))
    await my_message.add_reaction('🍻')
    await my_message.add_reaction('❌')
    return my_message


async def print_queue_taken(message: discord.message, queue_number: int, queue_freq: QueueFreq) -> None:
    await message.edit(content=lines.TAKEN.format(
        queue_taken=queue_number,
        time=time.time(delta_minutes=queue_freq.minutes)))
