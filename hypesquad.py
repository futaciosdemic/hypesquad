import discord
from discord.ext import commands

intents = discord.Intents.default()

client = commands.Bot(command_prefix='!', intents=intents) # this is the prefix u can change it whenever u want(u can also change the client)

@client.command()
async def hypesquad(ctx, hypesquad=None):
    answers = ["bravery", "brilliance", "balance", "briliance"]
    await ctx.message.delete()
    nr = 0
    if hypesquad not in answers:
        return
    if hypesquad == "bravery":
        nr = 1
    elif hypesquad == "brilliance" or hypesquad == "briliance":
        nr = 2
    elif hypesquad == "balance":
        nr = 3
    x = requests.post(
        f"https://discord.com/api/v9/hypesquad/online",
        json={"house_id": nr},
        headers={"authorization": tokens[0]},  # Change index as needed
    )
    status = x.status_code
    if status == 204:
        return
    else:
        await ctx.send("`API denied request... please wait`")
