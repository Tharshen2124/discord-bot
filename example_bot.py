import discord
import datetime
import config
from helper import welcomeMessage
from helper import startMessage

thumbsup = '👍'
thumbsdown = '👎'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
    if message.content.startswith('$create'):
        x = datetime.datetime.now()
        day = x.strftime("%d")
        month = x.strftime("%b")
        year = x.strftime("%Y")
        response  = await message.channel.send('who is coming for hackerspace on ' + day + " " + month + " " + year +" ?")
        coming    = await response.add_reaction(thumbsup)
        notcoming = await response.add_reaction(thumbsdown)

    @client.event
    async def on_reaction_add(reaction, user):
        if reaction.count > 1 and reaction.emoji == thumbsdown:
            
            await user.send(startMessage() + user.name + "! " + welcomeMessage())
            
        if reaction.count > 10 and reaction.emoji == thumbsup:
            await message.channel.send('SHEESHHHH we got a lot of people')

client.run(config.TOKEN)