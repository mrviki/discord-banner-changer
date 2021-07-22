import os
import discord
import random
from discord.ext import tasks

BOT_TOKEN = 'bot token'

client = discord.Client()

@client.event
async def on_ready():
    print("logged in: ", client.user)

@tasks.loop(minutes=1)
async def main():
    images = os.listdir('images')
    image = random.choice(images)
    with open(f'images/{image}', 'rb') as f:
        guild = client.get_guild(698247552352518256)
        await guild.edit(banner=f.read())

@main.before_loop
async def before_main():
    await client.wait_until_ready()


main.start()
client.run(BOT_TOKEN)
