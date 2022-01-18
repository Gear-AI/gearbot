# GEARBOT - THE ADMIN BOT OF GEAR AI'S DISCORD SERVER

# FILE NAME: src/desc.py

# FILE CONTAINING ALL THE DESCRIPTION VARIABLES FOR EASIER ACCESS

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

# PRE ASSIGNED ENCOURAGEMENT STATEMENT VARIABLES
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "anxious", "moody", "failure", "unworthy"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person.",
  "Nothing is impossible."
]