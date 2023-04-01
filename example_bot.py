import discord
import datetime

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
        coming    = await response.add_reaction('👍')
        notcoming = await response.add_reaction('👎')

    @client.event
    async def on_reaction_add(reaction, user):
        if reaction.count > 1 and reaction.emoji == "👎":
            await message.channel.send('bruh...')
        if reaction.count > 1 and reaction.emoji == "👍":
            await message.channel.send('SHEESHHHH we got a lot of people')

client.run('MTA5MTY2OTA3MjA1NzQ4NzQxMQ.G49IUX.kDWfQxERhPdCB3Ksql7x1W89hPXZbe62aAmGEs')