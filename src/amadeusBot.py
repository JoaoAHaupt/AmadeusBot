import discord
import random
from AmadeusBot.key import token
from AmadeusBot.src.mozartFacts import facts

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get("TOKEN")

@client.event
async def on_ready():
    print(f"{client.user} está online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("𝄞hello"):
        await message.channel.send(f"Hello {message.author}, I'm Amadeus Mozart HAHAHAHA")

    if message.content.startswith("𝄞help"):
        await message.channel.send(f"Hello {message.author}, I'm Amadeus Mozart HAHAHAHA")

    if message.content.startswith("𝄞love"):
        for i in range(0, 110, 10):
            await message.channel.send(f"{message.author} loves u {i}%")
         
    if message.content.startswith("𝄞facts"):
        randomNumber = random.randint(1, 10)

        await message.channel.send(facts[str(randomNumber)])

    
client.run(TOKEN)