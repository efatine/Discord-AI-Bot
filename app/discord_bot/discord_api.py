from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)
    
    async def on_message(self, message):
        print("Message received: ", message.content, "by: ", message.author)
        if (message.author == self.user): # Prevent bot from replying to itself
            return 
        
        command = None # Declare empty variables for the mean time
        user_message = None # Declare empty variables for the mean time

        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0] # Split only the first word in the message
                user_message = message.content.replace(text, '')
                print(command, user_message)
            
        if command == 'ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt=user_message)
            user_mention = message.author.mention
            await message.channel.send(f"{user_mention} {bot_response}") # Wait for the message to completely send

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)