import discord
import json
from discord.ext import commands, tasks
import schedule
import time

config_file="config.json"
with open(config_file) as json_data:
    config = json.load(json_data)
token = config['token']

bot = commands.Bot("!")

target_channel_id = 740673234843730712
message_channel = None

async def called_every_friday():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    video_fp = open("resources/friday-vid-1.mp4", "rb")
    discord_file = discord.File(fp=video_fp)
    await message_channel.send("dingle", file=discord_file)

async def task():
    await called_every_friday()

#schedule.every(1).seconds.do(task)
@bot.event
async def on_ready():
    message_channel = bot.get_channel(target_channel_id)
    slow_count.start()

@tasks.loop(seconds=1)
async def slow_count():
    await message_channel.send("hello there")

@slow_count.after_loop
async def after_slow_count():
    print('done!')
    
#while True:
#    schedule.run_pending()
#    time.sleep(1)

bot.run(token)
