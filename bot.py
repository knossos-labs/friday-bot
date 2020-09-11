import argparse
import discord
import json
import logging
import random
import asyncio
from discord.ext import commands, tasks
from datetime import datetime

config_file="config.json"
with open(config_file) as json_data:
    config = json.load(json_data)
token = config['token']

bot = commands.Bot("!")

target_channel_id = 740673234843730712

rightnow = datetime.now()
print(rightnow.weekday())
print(rightnow.hour)
print(rightnow.minute)
print(rightnow.second)
shouldrun = False

@tasks.loop(hours=1)
async def called_every_friday():
    rightnow = datetime.now()
    print("entering hyperloop")
    shouldrun = rightnow.weekday() == 3 and rightnow.hour == 17
    print(shouldrun)
    if shouldrun:
        message_channel = bot.get_channel(target_channel_id)
        print(f"Got channel {message_channel}")
        video_fp = open("resources/friday-vid-1.mp4", "rb")
        discord_file = discord.File(fp=video_fp)
        await message_channel.send("You made it!", file=discord_file) and await asyncio.sleep(600000)

@called_every_friday.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")


called_every_friday.start()
bot.run(token)
