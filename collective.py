import discord
from discord.ext import commands
import pandas
import csv
import random

#command prefix
client = commands.Bot(command_prefix='<')

#variables and stuffs
#df = pandas.DataFrame({'a':['a','b']})
#df.to_csv('/Users/nealkotval/Desktop/collective bot/output.csv')

@client.command(name="hello")
async def hello(context):
    await context.message.channel.send("hey")

@client.command(name="loginfo")
async def loginfo(context, *args):
    convert = str(args)
    characters_to_remove = ",()'"
    convert1 = convert
    for character in characters_to_remove:
        convert1 = convert1.replace(character, "")
    print(convert1)
    mention = context.author.mention
    spareembed=discord.Embed(title="Log Submitted!", description='Log: "' + convert1 + '" - info logged by user ' + mention, color=0x000FF)
    await context.message.channel.send(embed=spareembed)
    df=pandas.read_csv('/Users/nealkotval/Desktop/collective bot/output.csv',index_col=0)
    df=df.append({'logs':convert1}, ignore_index=True)
    df.to_csv('/Users/nealkotval/Desktop/collective bot/output.csv')

@client.command(name="checklogs")
async def checklogs(context, lognum):

    
    with open('output.csv', 'r') as file:
        reader = csv.reader(file)
        a=0
        if lognum == "random":
            chosen_row = random.choice(list(reader))
            bembed = discord.Embed(title="Random Log:", description=str(chosen_row))
            await context.message.channel.send(embed=bembed)
                

        for row in reader:
            a=a+1
            bruh = str(a)
            bembed = discord.Embed(title="Log " + str(a) + ":", description=str(row))

            if lognum == "all":
                await context.message.channel.send(embed=bembed)
            
            if lognum == bruh:
                print(bruh)
                await context.message.channel.send(embed=bembed)
        try:
            lognum = int(lognum)
        except:
            print('not a num')
        else:
            print(len(list(reader)))
            file = open("output.csv")
            reader1 = csv.reader(file)
            lines = len(list(reader1))
            if lognum > lines:
                stringlen = str(lines)
                sparembed = discord.Embed(title="That log does not exist!", description="Only " + stringlen + " exist...")
                await context.message.channel.send(embed=sparembed)

@client.command(name="invite")
async def invite(context):
    invembed = discord.Embed(title="Invite This Bot to Your Server With This Link!", description="https://discord.com/api/oauth2/authorize?client_id=811321292686360587&permissions=8&scope=bot")
    await context.message.channel.send(embed=invembed)


        



#bot token
client.run("ODExMzIxMjkyNjg2MzYwNTg3.YCwf1Q.hYKrAFxFCtFefcsHiWu-ni-FsVY")
