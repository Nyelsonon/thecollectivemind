#imports
import discord
from discord.ext import commands
import pandas
import csv
import random
import simplyJSON as nt
import json
import os

#command prefix
client = commands.Bot(command_prefix='<')

@client.command(name="loginfo")
async def loginfo(context, *args):
    #remove unecessary symbols like , () and '
    convert = str(args)
    characters_to_remove = ",()'"
    convert1 = convert
    for character in characters_to_remove:
        convert1 = convert1.replace(character, "")

    #notify user
    mention = context.author.mention
    spareembed=discord.Embed(title="Log Submitted!", description='Log: "' + convert1 + '" - info logged by user ' + mention, color=0x000FF)
    await context.message.channel.send(embed=spareembed)

    #send to json using simplyJSON module
    nt.appendJSON("output.json",{mention:convert1})

@client.command(name="checklogs")
async def checklogs(context, lognum):
    #variables
    logger = 0
    logger_logger = 0

    #code for lognum = random
    if lognum == "random":
        #initializing JSON file
        with open('output.json', "r") as f:
            data = json.load(f)
            randlog = random.randint(1,len(data))

            #finding random log
            for key, value in data.items():
                logger_logger = logger_logger + 1
                if logger_logger == randlog:
                    chosen_row = value
                    chosen_author = key
                    #display for user
                    bembed = discord.Embed(title="Random Log:", description='"' + str(chosen_row) + '"  - Written by User: ' + str(chosen_author) + ", Log ID: " + str(logger_logger))
                    await context.message.channel.send(embed=bembed)
    try:
        lognum = int(lognum)
        with open('output.json', 'r') as f2:
            data = json.load(f2)

            if lognum > len(data):
                tryfly = len(data)
                toolongembed = discord.Embed(title="Log Not Found", description="Only " + str(tryfly) + " logs exist...")
                await context.message.channel.send(embed=toolongembed)
            else:
                for key, value in data.items():
                        logger = logger + 1
                        if logger == lognum:
                            chosen_row = value
                            chosen_author = key
                            #display for user
                            bembed = discord.Embed(title="Found Log:", description='"' + str(chosen_row) + '"  - Written by User: ' + str(chosen_author) + ", Log ID: " + str(logger))
                            await context.message.channel.send(embed=bembed)
    except:
        await context.message.channel.send("that parameter does not exist")




@client.command(name="invite")
async def invite(context):
    invembed = discord.Embed(title="Invite This Bot to Your Server With This Link!", description="https://discord.com/api/oauth2/authorize?client_id=811321292686360587&permissions=8&scope=bot")
    await context.message.channel.send(embed=invembed)


        



#bot token
client.run("token")
