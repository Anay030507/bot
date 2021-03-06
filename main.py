import discord
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from aiohttp import ClientSession
import aiohttp
import jishaku
import json
import sys
import os
import traceback

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = ";", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command(aliases=['srr'])
@commands.has_permissions(administrator=True)
async def selfroleskeroles(ctx):
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・MALE」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・FEMALE」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・18+」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・18-」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・PUBG」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・COD」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・AMONG US」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・SINGLE」", color=0x000000)
        except:
            pass
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╭ ── ──𒆕・MINGLE」", color=0x000000)
        except:
            pass
    else:
        em = discord.Embed(description=f"{ctx.author.mention} SELF ROLES BANA DIYE", color=0x00f7ff)
        return await ctx.send(embed=em)

@bot.command(aliases=['lr'])
@commands.has_permissions(administrator=True)
async def levelroles(ctx):
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 100」", color=0x003132)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 90」", color=0x004a4c)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 80」", color=0x006265)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 70」", color=0x007b7f)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 60」", color=0x009499)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 50」", color=0x00acb2)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 40」", color=0x00c5cc)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 30」", color=0x00dee5)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 20」", color=0x00f7ff)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 10」", color=0x19f7ff)
        except:
            continue
    for _i in range(1):
        try:
            await ctx.guild.create_role(name="╰─────•⫸ LEVEL 5」", color=0x33f8ff)
        except:
            continue
    else:
        em = discord.Embed(description=f"{ctx.author.mention} LEVEL ROLES BANA DIYE", color=0x00f7ff)
        return await ctx.send(embed=em)

@bot.command()
@commands.is_owner()
async def rules(ctx):
    try:
        em=discord.Embed(title='RULES', description="1. Respect is a priority on this server, treat others the way you’d want to be treated and no use of filthy words.\n2. Harassing, abusing, or using any type of hate speech towards another member is not permitted.\n3. Spamming(unless in spam) or excessively tagging other members is not allowed.\n4. Posting any NSFW content (which includes your avatar) will result in an instant kick, if you do not change it when you come back, you will be banned unless in NSFW.\n5. Do not sell or advertise any products on this discord and any kind of PROMOTION of anything or anyone will not be tolerated.", color=0x00f7ff)
        await ctx.send(embed=em)
    except: 
        pass

@bot.command(aliases=['sr'])
@commands.is_owner()
async def selfrole(ctx):
    try:
        em=discord.Embed(title='SELF ROLES', color=0x00f7ff)
        em.set_image(url="https://images-ext-2.discordapp.net/external/2oWIWctzv5IZ7webJCz-Q8q9iG9OgpnbHEVk1jQwhTg/https/media.discordapp.net/attachments/725721224927510609/756156973392724008/GLITCHO_GIF_20200620_092543.gif")
        await ctx.send(embed=em)
    except:
        pass
    try:
        em=discord.Embed(title='<a:loading:817132096052658206>   亗╎GENDER╎亗   <a:loading:817132096052658206>', description='<a:vshield:817132104575877141> REACT HERE TO CLAIM YOUR ROLE <a:vshield:817132104575877141>\n\n<a:rainbow_arrow:817132104512700516> <a:male:817132119854809150>┃ MALE\n\n<a:rainbow_arrow:817132104512700516> <a:female:817132127052890172>┃ FEMALE', color=0x00f7ff)       
        em.set_footer(text=f'{ctx.guild.name}', icon_url=f'{ctx.guild.icon_url}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed=em)
    except:
        pass
    try:
        em=discord.Embed(title='<a:loading:817132096052658206>   亗╎AGE╎亗   <a:loading:817132096052658206>', description='<a:vshield:817132104575877141> REACT HERE TO CLAIM YOUR ROLE <a:vshield:817132104575877141>\n\n<a:rainbow_arrow:817132104512700516> <a:18:817132104567095351>┃ 18+\n\n<a:rainbow_arrow:817132104512700516> <a:18:817132103074185277>┃ 18-', color=0x00f7ff)       
        em.set_footer(text=f'{ctx.guild.name}', icon_url=f'{ctx.guild.icon_url}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed=em)
    except:
        pass
    try:
        em=discord.Embed(title='<a:loading:817132096052658206>   亗╎GENDER╎亗   <a:loading:817132096052658206>', description='<a:vshield:817132104575877141> REACT HERE TO CLAIM YOUR ROLE <a:vshield:817132104575877141>\n\n<a:rainbow_arrow:817132104512700516> <a:pubg:817132112431022192>┃ PUBG\n\n<a:rainbow_arrow:817132104512700516> <a:cod:817132113731387442>┃ COD\n\n<a:rainbow_arrow:817132104512700516> <a:among_us:817132115723419688>┃ AMONG US', color=0x00f7ff)       
        em.set_footer(text=f'{ctx.guild.name}', icon_url=f'{ctx.guild.icon_url}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed=em)
    except:
        pass
    try:
        em=discord.Embed(title='<a:loading:817132096052658206>   亗╎AGE╎亗   <a:loading:817132096052658206>', description='<a:vshield:817132104575877141> REACT HERE TO CLAIM YOUR ROLE <a:vshield:817132104575877141>\n\n<a:rainbow_arrow:817132104512700516> <a:single:817132102852018186>┃ SINGLE\n\n<a:rainbow_arrow:817132104512700516> <a:mingle:817132117641003059>┃ MINGLE', color=0x00f7ff)       
        em.set_footer(text=f'{ctx.guild.name}', icon_url=f'{ctx.guild.icon_url}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        await ctx.send(embed=em)
    except:
        pass
@bot.command()
async def icon(ctx):
    try:
        em=discord.Embed(title="SERVER ICON")
        em.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=em)
    except:
        pass

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role(ctx, user: discord.Member, role: discord.Role):
    try:
        await user.add_roles(role)
        em=discord.Embed(description=f"<:success:817151821070991432> Successfully Given {role.mention} to {user.mention}", color=0x00f7ff)
        await ctx.send(embed=em)
    except:
        pass

@bot.command(aliases=["av"], brief="Avatar")
@commands.guild_only()
async def avatar(ctx, member: discord.Member = None):
        
    member = (
        member or ctx.author
    )  

    pfp = member.avatar_url_as(static_format="png")  # Gets the avatar url

    embed = discord.Embed(title=str(member), color=0x00f7ff)  # Creates the embed
    embed.set_image(url=pfp)  # Puts the avatar in the embed
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def roleall(ctx, role: discord.Role):
    for member in ctx.guild.members:
        try:
            await member.add_roles(role)
        except:
            continue

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, *,role):
        try:
            await ctx.guild.create_role(name=f"{role}", color=0x000000)
            em = discord.Embed(description=f"<:success:817151821070991432> Successfully created {role}", color=0x00f7ff)
            return await ctx.channel.send(embed=em)
        except:
            pass

@bot.command()
@commands.has_permissions(manage_roles=True)
async def delrole(ctx, *,msg):
    for _i in range(1):
        try:
            await ctx.guild.delete_role(name=f"{msg}")
            em = discord.Embed(description=f"<:success:817151821070991432> Successfully deleted {msg}", color=0x00f7ff)
            return await ctx.channel.send(embed=em)
        except:
            pass

@bot.command()
@commands.has_permissions(manage_channels=True)
async def delchannel(ctx):
    for _i in range(1):
        try:
            await ctx.guild.delete_channel
            em = discord.Embed(description=f"<:success:817151821070991432> Successfully deleted", color=0x00f7ff)
            return await ctx.channel.send(embed=em)
        except:
            pass

@bot.command()
async def nsfw(self, ctx):
    if ctx.channel.is_nsfw() == False:
        embed = discord.Embed(title="<:9830_no:748426943766069308> You can't use NSFW commands in non NSFW channels!", color=discord.Color.red())

        await ctx.send(embed=embed)

    else:
        r = requests.get("https://waifu.pics/api/nsfw")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

@bot.command()
async def lewdneko(self, ctx):
    if ctx.channel.is_nsfw() == False:
        embed = discord.Embed(
            title="<:9830_no:748426943766069308> You can't use NSFW commands in non NSFW channels!",color=discord.Color.red())

        await ctx.send(embed=embed)
    else:
        r = requests.get("https://waifu.pics/api/lewdneko")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def addchannel(ctx, *,msg):
    for _i in range(1):
        try:
            await ctx.guild.create_channel(name=f"{msg}")
            em = discord.Embed(description=f"<:success:817151821070991432> Successfully created {msg}", color=0x00f7ff)
            return await ctx.channel.send(embed=em)
        except:
            pass

@bot.command(aliases=["mc"])
async def membercount(ctx):
    try:
        guild=ctx.guild
        em=discord.Embed(title='Members', discreption=f"{guild.member_count}", color=0x00f7ff)
        await ctx.send(embed=em)
    except:
        pass

@role.error
async def role_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(description=f"<:fail:817177131750260736> Mention a member to assign the role give", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> You do not have permission to assign any role to anyone", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.BotMissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> I don't have permission to manage roles any one", color=0xff0000)
        await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    em = discord.Embed(description=f"<:success:817151821070991432> Successfully Muted {member} with the reason **`{reason}`**", color=0x00f7ff)
    await ctx.channel.send(embed=em)
    await member.send(f'YOU HAVE BEEN MUTED FROM {ctx.guild.name} FOR THE REASON **{reason}**')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    em = discord.Embed(description=f"<:success:817151821070991432> Successfully Unmuted {member}", color=0x00f7ff)
    await ctx.channel.send(embed=em)
    await member.send(f'YOU HAVE BEEN UNMUTED FROM {ctx.guild.name}')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    em = discord.Embed(description=f"<:success:817151821070991432> Successfully Banned {member} with the reason **`{reason}`**", color=0x00f7ff)
    await ctx.channel.send(embed=em)
    await member.send(f'YOU HAVE BEEN BANNED FROM {ctx.guild.name} FOR THE REASON **{reason}**')

@rules.error
async def rules_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> You do not own this bot", color=0xff0000)
        await ctx.send(embed=em)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(description=f"<:fail:817177131750260736> Mention a member to ban", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> You do not have permission to ban anyone", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.BotMissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> I don't have permission to ban any one", color=0xff0000)
        await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    em = discord.Embed(description=f"<:success:817151821070991432> Successfully Kicked {member} with the reason **`{reason}`**", color=0x00f7ff)
    await ctx.channel.send(embed=em)
    await member.send(f'YOU HAVE BEEN KICKED FROM {ctx.guild.name} FOR THE REASON **{reason}**')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(description=f"<:fail:817177131750260736> Mention a member to kick", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> You do not have permission to kick anyone", color=0xff0000)
        await ctx.send(embed=em)
    if isinstance(error, commands.BotMissingPermissions):
        em = discord.Embed(description=f"<:fail:817177131750260736> I don't have permission to kick any one", color=0xff0000)
        await ctx.send(embed=em)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int = None):
    if id == None:
        await ctx.send('Oopsies but you need an ID!')

    else:
        if len(str(id)) == 18:
            user = await bot.fetch_user(id)
            
            await ctx.guild.unban(user)
            await ctx.send(f'<:success:817151821070991432> Unbanned **{id}**! Welcome back buddy!')

        else:
            await ctx.send(f'Oops! **{id}** doesn\'t seem like a valid ID! Try again!')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx,user: discord.Member,*,args):
    if args != None:
        try:
            await user.send(f'You have been warned from {ctx.guild.name} for {args}')
            em = discord.Embed(description=f"<:success:817151821070991432> {user} Has been warned", color=0x00f7ff)
            await ctx.send(embed=em)
        except:
            em = discord.Embed(description=f"<:fail:817177131750260736> {user} has his dm's off", color=0xff0000)
            await ctx.send(embed=em)

@bot.command()
async def echo(ctx, *,msg):
    try:
        em = discord.Embed(description=f"{msg}", color=0x00f7ff)
        return await msg.channel.send(embed=em)
    except:
        pass

@bot.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention, color=0x00f7ff)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=True)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@bot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount):
        try:
           await message.delete()
        except:
            pass
bot.load_extension('jishaku')
bot.run('ODE3MTIzNjY0MjA5NTEwNDMx.YEE7tg.53IpJqb8isyk-QK0bJ55hMDMKxo')