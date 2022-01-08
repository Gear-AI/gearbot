# GEARBOT - THE ADMIN BOT OF GEAR AI'S DISCORD SERVER

# FILE NAME: main.py

# IMPORING REQUIRED LIBRARIES
import discord
import os
import requests
import json
import random
from replit import db

# ALLOCATING A DISCORD CLIENT INSTANCE
client = discord.Client()

about = '''Hi, I'm GearBot.
           I automate all the administrative actions in GearAI's discord server. 
           I could also convey you some useful information. I'm currently under development.\n
           **Available commands:** 
           ``` $hello - Just a dummy command.\n 
               $help - Command to display Usage Instructions.\n 
               $quote - Send an inspiring quote.```'''

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "anxious", "moody", "failure", "unworthy"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person.",
  "Nothing is impossible."
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

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
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

client.run(os.getenv("TOKEN"))
