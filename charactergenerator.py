# Write your Halloween story here as a multi-line quote

import random
# okay i like this whole MadLibs idea but i just realized this is how people make character generators so im gonna do that
character = """
This character is a %s'%s" %s %s %s.  They have %s skin, %s %s %s hair and %s eyes.  They have a %s personality, and they enjoy %s.  They work as %s.
"""
# this is honestly as random as it gets my guy
# imagine a demon as your realtor
# modify the parameters in the function so that they are appropriate for your story
def character_prompt(heightfeet= [4, 5, 6, 7] , heightinch= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], species=["human", "elf", "demon", "harpy", "ghost", "werewolf", "vampire", "selkie", "satyr"],gender=["cis boy", "cis girl", "trans boy", "trans girl", "enby", "demiboy", "demigirl", "genderfluid"], build= ["scrawny", "slim", "stocky", "chubby", "muscular"], skintone= ["pale", "peach", "tan", "olive toned", "dark"], hairlength= ["long", "shoulder length", "short", "pixiecut", "undercut"], hair= ["curly", "wavy", "coily", "straight"], color= ["brown", "black", "grey", "red", "orange", "yellow", "green", "cyan", "blue", "indigo", "lavender", "violet", "magenta", "pink"], personality= ["brave", "hasty", "timid", "lively", "comical", "temperamental", "jolly", "melancholy", "cynical", "haughty"], interests= ["drawing", "writing", "playing sports", "playing videogames", "blogging", "hiking", "jogging", "studying", "napping", "dabbling in the occult", "painting"], job= ["an idolgirl", "a ghosthunter", "a baker", "a traffic cop", "a fashion blogger", "a valet", "a teacher", "a merchant", "a scientist", "a street performer", "a barista", "a photographer", "a realtor", "a banker"]):
	# Modify the tuple after %s to contain the parameters you want to insert
	print(character % (random.choice(heightfeet), random.choice(heightinch), random.choice(build), random.choice(gender), random.choice(species), random.choice(skintone), random.choice(hairlength), random.choice(hair),random.choice(color), random.choice(color), random.choice(personality), random.choice(interests), random.choice(job)))

# Try calling this function with different sets of arguments
print("How many characters would you like to generate?")
num = int(input())
# you could probably generate some really excessive number of characters with this (like 100 or beyond) but maybe dont bc that seems like the type of thing that would crash it.
for x in range(num):
	character_prompt()