# GEARBOT - THE ADMIN BOT OF GEAR AI'S DISCORD SERVER

# FILE NAME: src/main.py

# IMPORING REQUIRED LIBRARIES
import discord
import os
import requests
import json
import random
from replit import db
from discord.ext.commands import Bot, has_permissions, CheckFailure
import asyncio
from . import desc, enc

# ALLOCATING A DISCORD CLIENT INSTANCE
client = Bot(command_prefix='$')

about = desc.about
sad_words = desc.sad_words
starter_encouragements = desc.starter_encouragements

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)


@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$help'):
    await message.channel.send(about)

  if message.content.startswith('$quote'):
    quote = get_quote()
    await message.channel.send(f"So you have asked for quote, here it is.\n```{quote}```")

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$enc_add"):
    encouraging_message = msg.split("$enc_add ",1)[1]
    enc.update_encouragements(encouraging_message)
    encouragements = db["encouragements"]
    await message.channel.send(f"New cheer message added.")

  if msg.startswith("$enc_delete"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
      stmt = msg.split("$enc_delete ",1)[1]
      enc.delete_encouragment(encouragements.index(stmt))
      encouragements = db["encouragements"]
    await message.channel.send(f"Cheer message deleted.")

  if msg.startswith("$enc_list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send("**ENCOURAGEMENT DATABASE**")
    await message.channel.send("-"*40)
    await message.channel.send("**Starter Encouragements**")
    for stmt in starter_encouragements:
      await message.channel.send(stmt)
    await message.channel.send("-"*40)
    await message.channel.send("**Add-On Encouragements**")
    for stmt in list(encouragements):
      await message.channel.send(stmt)
    
  if msg.startswith("$enc_toggle"):
    value = msg.split("$enc_toggle ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Cheer message service is now turned ON.")
    else:
      db["responding"] = False
      await message.channel.send("Cheer message service is now turned OFF.")

client.run(os.getenv("TOKEN"))
