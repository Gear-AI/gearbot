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

# PRE ASSIGNED ENCOURAGEMENT STATEMENT VARIABLES
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "anxious", "moody", "failure", "unworthy"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person.",
  "Nothing is impossible."
]

# VARIABLE TO PRINT FOR COMMAND: $help
about =("Hi, I'm GearBot.\n"
        "I automate all the administrative actions in GearAI's discord server.\n"
        "I could also convey you some useful information. I'm currently under development.\n"

        "**Available commands:**\n"
        "**General commmands:**\n"

        "```"
        "$helloworld - Just a simple way to ping me.\n"
        "$help - Command to display Usage Instructions.\n"
        "$quote - Send an inspiring quote.\n"
        "```"

        "Talk with a negative word and I'll cheer you up.\n"
        "**Encouragement Database commands:**\n"

        "```"

        "$enc_toggle - Toggle to turn ON or turn OFF the cheer message functionality\n"
        "Accepted values - boolean: true, false\n"
        "Example - $enc_toggle true\n\n"

        "$enc_add - Command to add a custom cheer message to the database\n"
        "Accepted values - string (without single or double quotes)\n"
        "Example - $enc_add Cheer up\n\n"
        
        "$enc_delete - Command to delete a custom cheer message from the database\n"
        "Accepted values - int (index of the message which should be deleted)\n"
        "Example - $enc_delete 2\n\n"

        "$enc_list - Command to show the list of cheer messages added to the database\n"
        "```")

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

  if message.content.startswith('$admin') and if discord.discord.Member.roles("Admin")
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$enc_add"):
    encouraging_message = msg.split("$enc_add ",1)[1]
    update_encouragements(encouraging_message)
    encouragements = db["encouragements"]
    await message.channel.send(f"New cheer message added.\n**Updated database: **{list(encouragements)}")

  if msg.startswith("$enc_delete"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$enc_delete",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(f"Cheer message deleted.\n**Updated database: **{list(encouragements)}")

  if msg.startswith("$enc_list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$enc_toggle"):
    value = msg.split("$enc_toggle ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Cheer message service is now turned ON.")
    else:
      db["responding"] = False
      await message.channel.send("Cheer message service is now turned OFF.")

client.run(os.getenv("TOKEN"))
