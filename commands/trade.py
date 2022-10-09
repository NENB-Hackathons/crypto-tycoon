from main import *

@bot.command(aliases=['TRADE', 't', 'T'])
async def trade(ctx):
    user = getUser(ctx.message.author.id)
    if user is not False:
        ctx.send(f'{user.name}, your balance is: {user.balance}BSD. Input the user ID of who you want it sent to.')
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}')
        deleteMessage(msg)
    
