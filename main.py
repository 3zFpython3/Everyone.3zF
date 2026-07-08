#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os

os.system('clear')

print("========================================")
print("            RYNDE BOT SETUP")
print("========================================")
print("")

TOKEN = input("Enter Bot Token: ").strip()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    os.system('clear')
    print("""
 ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print("========================================")
    print(f"Bot Ready : {bot.user}")
    print(f"Servers : {len(bot.guilds)}")
    print("========================================")
    print("")
    print("Select Server:")
    print("")
    for i, guild in enumerate(bot.guilds, 1):
        print(f" [{i}] {guild.name}")
    print("")
    print("========================================")
    print("")
    
    def check(m):
        return m.author == bot.user
    
    try:
        msg = await bot.wait_for("message", timeout=60.0, check=check)
        choice = int(msg.content)
        
        if 1 <= choice <= len(bot.guilds):
            guild = bot.guilds[choice - 1]
            os.system('clear')
            print("""
 ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
            print("========================================")
            print(f"Server : {guild.name}")
            print("========================================")
            print("")
            print(" [1] Create Rooms")
            print(" [2] Delete Rooms")
            print(" [3] Create Rooms + Spam")
            print(" [4] Nuke Rooms")
            print(" [5] Create Rooms Fast")
            print(" [6] Delete All Channels")
            print(" [7] Exit")
            print("========================================")
            
    except:
        print("Timeout or invalid input!")

@bot.command(name="1")
@commands.has_permissions(administrator=True)
async def cmd1(ctx):
    await ctx.send("Enter room name:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg1 = await bot.wait_for("message", timeout=30.0, check=check)
        name = msg1.content.strip()
        
        await ctx.send("How many rooms:")
        msg2 = await bot.wait_for("message", timeout=30.0, check=check)
        count = int(msg2.content)
        
        await ctx.send(f"Creating {count} rooms...")
        for i in range(1, count + 1):
            try:
                await ctx.guild.create_text_channel(f"{name}_{i}")
                await asyncio.sleep(0.3)
            except:
                pass
        await ctx.send(f"Created {count} rooms!")
        
    except:
        await ctx.send("Timeout or invalid input!")

@bot.command(name="2")
@commands.has_permissions(administrator=True)
async def cmd2(ctx):
    await ctx.send("Enter room name to delete:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        name = msg.content.strip()
        
        await ctx.send(f"Deleting rooms with name {name}...")
        d = 0
        for channel in ctx.guild.channels:
            if name in channel.name and channel.name.startswith(name):
                try:
                    await channel.delete()
                    d += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
        await ctx.send(f"Deleted {d} rooms!")
        
    except:
        await ctx.send("Timeout!")

@bot.command(name="3")
@commands.has_permissions(administrator=True)
async def cmd3(ctx):
    await ctx.send("Enter room name:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg1 = await bot.wait_for("message", timeout=30.0, check=check)
        name = msg1.content.strip()
        
        await ctx.send("How many rooms:")
        msg2 = await bot.wait_for("message", timeout=30.0, check=check)
        count = int(msg2.content)
        
        await ctx.send(f"Creating {count} rooms with spam...")
        for i in range(1, count + 1):
            try:
                channel = await ctx.guild.create_text_channel(f"{name}_{i}")
                await asyncio.sleep(0.5)
                for j in range(3):
                    await channel.send(f"SPAM {j+1}")
                    await asyncio.sleep(0.2)
            except:
                pass
        await ctx.send(f"Created {count} rooms with spam!")
        
    except:
        await ctx.send("Timeout or invalid input!")

@bot.command(name="4")
@commands.has_permissions(administrator=True)
async def cmd4(ctx):
    await ctx.send("Enter room name to nuke:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        name = msg.content.strip()
        
        await ctx.send(f"Nuking all {name} rooms...")
        d = 0
        for channel in ctx.guild.channels:
            if name in channel.name and channel.name.startswith(name):
                try:
                    await channel.delete()
                    d += 1
                    await asyncio.sleep(0.2)
                except:
                    pass
        await ctx.send(f"Nuked {d} rooms!")
        
    except:
        await ctx.send("Timeout!")

@bot.command(name="5")
@commands.has_permissions(administrator=True)
async def cmd5(ctx):
    await ctx.send("Enter room name:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg1 = await bot.wait_for("message", timeout=30.0, check=check)
        name = msg1.content.strip()
        
        await ctx.send("How many rooms:")
        msg2 = await bot.wait_for("message", timeout=30.0, check=check)
        count = int(msg2.content)
        
        await ctx.send(f"Creating {count} rooms fast...")
        for i in range(1, count + 1):
            try:
                await ctx.guild.create_text_channel(f"{name}_{i}")
            except:
                pass
        await ctx.send(f"Created {count} rooms!")
        
    except:
        await ctx.send("Timeout or invalid input!")

@bot.command(name="6")
@commands.has_permissions(administrator=True)
async def cmd6(ctx):
    await ctx.send("Delete all channels? Type yes to confirm:")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        if msg.content.lower() == "yes":
            await ctx.send("Deleting all channels...")
            d = 0
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    d += 1
                    await asyncio.sleep(0.2)
                except:
                    pass
            await ctx.send(f"Deleted {d} channels!")
        else:
            await ctx.send("Cancelled!")
            
    except:
        await ctx.send("Timeout!")

@bot.command(name="help")
async def help_cmd(ctx):
    await ctx.send("""
Commands:
!1 - Create rooms (asks for name + count)
!2 - Delete rooms by name
!3 - Create rooms + spam
!4 - Nuke rooms by name
!5 - Create rooms fast
!6 - Delete all channels (asks for confirmation)
""")

bot.run(TOKEN)
