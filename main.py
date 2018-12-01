import discord
import requests
import os
import asyncio
import time
from discord.ext import commands
from keep_alive import keep_alive
bypass_list=["465328636703014923","380377019931820042","147551536036184064"]

description='A bot built for the Anime Toki Discord server.'
client=commands.Bot(command_prefix='+',description=description) 

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
  if message.content.upper().startswith("+LONGFORM"):
    time.sleep(1)
    userID=message.author.id
    await client.send_message(message.channel, "%s, I've got you!" % (userID))

#@client.event
#async def on_message(message):
#  userChannel=message.channel
#  if message.content.upper().startswith("+PING"):
#    await client.send_message(message.channel, "+Pong!")
#  if message.content.upper().startswith("+LONGFORM"):
#    time.sleep(1)
#    userID = message.author.id
#    await client.send_message(message.channel, "%s, I've got you!" % (userID))  
#  if message.content.upper().startswith("+say"):
#    userMsg=message.content.split()
#    output=' '
#    for word in userMsg[1:]:
#      output+=word
#      output+=' '
#
#    await client.send_message(userChannel,output)

@client.command()
async def ping():
  await client.say('Pong!')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
  print('Deleting messages.')
  channel=ctx.message.channel
  messages=[]
  async for message in client.logs_from(channel, limit=int(amount)):
    messages.append(message)
  await client.delete_messages(messages)
  await client.say('Messages removed.')

#@client.command(pass_context=True)
#async def kick(ctx,user=discord.Member,*,arg):
#  await client.kick(user)
#  reason=arg

# bot.command()
# async def anime():
#  query = ' '
#  query ($id: Int) { # Define which variables will be used in the query (id)
#  Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
#    id
#   title {
#     romaji
#     english
#     native
#   }
# }
#}

# Define our query variables and values that will be used in the query request

# url = 'https://graphql.anilist.co'

# Make the HTTP Api request
# response = requests.post(url, json={'query': query, 'variables': variables})

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)