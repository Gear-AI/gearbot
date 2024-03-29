# GEARBOT - THE ADMIN BOT OF GEAR AI'S DISCORD SERVER

# FILE NAME: src/enc.py

# FILE CONTAINING ALL THE ENCOURAGEMENT FEATURE METHODS

# IMPORTING REQUIRED LIBRARIES
from desc import *
from replit import db

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