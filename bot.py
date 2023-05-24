import discord
# import responses
import main
from dotenv import load_dotenv
import os

load_dotenv('.env')

async def send_message(message,user_message, is_private):
    try:
        message = main.getHeadline(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
    def run_discord_bot():
        TOKEN = os.getenv('token')
        client = discord.Client(intents=Intents.default())

        @client.event
        async def on_ready():
            print(f"{client.user} is now running ")

        client.run(TOKEN)