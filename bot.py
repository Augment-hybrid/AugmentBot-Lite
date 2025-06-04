"""
AugmentBot Lite - AI-Powered Discord Bot
Get yours: https://www.fiverr.com/yumemiru_/create-an-ai-powered-discord-bot-for-your-server-using-chatgpt
"""

import discord
import openai
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot is ready! Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask "):]
        await message.channel.send("💬 Thinking...")

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response.choices[0].message.content
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send(f"❌ Error: {e}")

client.run(DISCORD_TOKEN)
