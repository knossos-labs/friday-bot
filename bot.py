import argparse
import discord
import json
import logging
import random
from discord.ext import commands, tasks

config_file="config.json"
with open(config_file) as json_data:
    config = json.load(json_data)
token = config['token']

bot = commands.Bot("!")

target_channel_id = 740673234843730712

@tasks.loop(hours=168)
async def called_once_a_week():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("dingle")

@called_once_a_week.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_week.start()
bot.run(token)
