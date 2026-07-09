#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import sys

# ========== COLORS ==========
BLUE = '\033[94m'
DARK_BLUE = '\033[34m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

clear()

print(f"{DARK_BLUE}{BOLD}=" * 60)
print(f"{DARK_BLUE}{BOLD}            RYNDE BOT")
print(f"{DARK_BLUE}{BOLD}=" * 60)
print("")

TOKEN = input(f"{DARK_BLUE}[?]{WHITE} Token: ").strip()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    clear()
    print(f"""
{DARK_BLUE}{BOLD} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{DARK_BLUE}{BOLD}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{DARK_BLUE}{BOLD}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{DARK_BLUE}{BOLD}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{DARK_BLUE}{BOLD}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{DARK_BLUE}{BOLD} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {bot.user}")
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {len(bot.guilds)} Servers")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    print(f"{DARK_BLUE}{BOLD}╔════════════════════════════════════════════════╗")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}              RYNDE BOT v8                     {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         {bot.user}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         Server: {bot.guilds[0].name}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         ID: {bot.guilds[0].id}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         Developer: 3zF                      {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}╚════════════════════════════════════════════════╝")
    print("")
    
    print(f"{DARK_BLUE}[?]{WHITE} Select Server:")
    print("")
    for i, guild in enumerate(bot.guilds, 1):
        print(f"  {DARK_BLUE}[{CYAN}{i}{DARK_BLUE}]{WHITE} {guild.name}")
    print("")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    try:
        choice = int(input(f"{DARK_BLUE}[?]{WHITE} Number: ").strip())
        
        if 1 <= choice <= len(bot.guilds):
            guild = bot.guilds[choice - 1]
            clear()
            print(f"""
{DARK_BLUE}{BOLD} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{DARK_BLUE}{BOLD}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{DARK_BLUE}{BOLD}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{DARK_BLUE}{BOLD}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{DARK_BLUE}{BOLD}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{DARK_BLUE}{BOLD} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
            print(f"{DARK_BLUE}{BOLD}=" * 60)
            print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {guild.name}")
            print(f"{DARK_BLUE}{BOLD}=" * 60)
            print("")
            print(f"{DARK_BLUE}{BOLD}╔════════════════════════════════════════════════╗")
            print(f"{DARK_BLUE}{BOLD}║{WHITE}              RYNDE BOT v8                     {DARK_BLUE}{BOLD}║")
            print(f"{DARK_BLUE}{BOLD}║{WHITE}         {bot.user}              {DARK_BLUE}{BOLD}║")
            print(f"{DARK_BLUE}{BOLD}║{WHITE}         Server: {guild.name}              {DARK_BLUE}{BOLD}║")
            print(f"{DARK_BLUE}{BOLD}║{WHITE}         ID: {guild.id}              {DARK_BLUE}{BOLD}║")
            print(f"{DARK_BLUE}{BOLD}║{WHITE}         Developer: 3zF                      {DARK_BLUE}{BOLD}║")
            print(f"{DARK_BLUE}{BOLD}╚════════════════════════════════════════════════╝")
            print("")
            print(f"  {DARK_BLUE}[{CYAN}1{DARK_BLUE}]{WHITE} Create Rooms")
            print(f"  {DARK_BLUE}[{CYAN}2{DARK_BLUE}]{WHITE} Delete All")
            print(f"  {DARK_BLUE}[{CYAN}3{DARK_BLUE}]{WHITE} Spam All")
            print(f"  {DARK_BLUE}[{CYAN}4{DARK_BLUE}]{WHITE} Exit")
            print("")
            print(f"{DARK_BLUE}{BOLD}=" * 60)
            print("")
            
            while True:
                try:
                    cmd = input(f"{DARK_BLUE}[?]{WHITE} Option (1-4): ").strip()
                    
                    if cmd == "1":
                        await create_rooms(guild)
                    elif cmd == "2":
                        await delete_all(guild)
                    elif cmd == "3":
                        await spam_all(guild)
                    elif cmd == "4":
                        print(f"{DARK_BLUE}[!]{WHITE} Exiting...")
                        await bot.close()
                        sys.exit()
                    else:
                        print(f"{DARK_BLUE}[!]{WHITE} Invalid!")
                        
                except KeyboardInterrupt:
                    print(f"\n{DARK_BLUE}[!]{WHITE} Exiting...")
                    await bot.close()
                    sys.exit()
        else:
            print(f"{DARK_BLUE}[!]{WHITE} Invalid!")
            await bot.close()
            
    except ValueError:
        print(f"{DARK_BLUE}[!]{WHITE} Number!")
        await bot.close()

async def create_rooms(guild):
    clear()
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print(f"{DARK_BLUE}{BOLD}  [1] CREATE ROOMS")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    name = input(f"{DARK_BLUE}[?]{WHITE} Name: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Count: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Creating {count} rooms...\n")
    
    chunk_size = 50
    created = 0
    
    for i in range(0, count, chunk_size):
        chunk = min(chunk_size, count - i)
        tasks = [guild.create_text_channel(name) for _ in range(chunk)]
        channels = await asyncio.gather(*tasks, return_exceptions=True)
        created += sum(1 for c in channels if not isinstance(c, Exception))
        print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {created}/{count}")
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {created} rooms created!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def delete_all(guild):
    clear()
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print(f"{DARK_BLUE}{BOLD}  [2] DELETE ALL")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    confirm = input(f"{DARK_BLUE}[{RED}!{DARK_BLUE}]{WHITE} Delete ALL? (y/n): ").strip().lower()
    
    if confirm == "y":
        print(f"\n{DARK_BLUE}[+]{WHITE} Deleting all channels...\n")
        
        chunk_size = 50
        deleted = 0
        channels = list(guild.channels)
        
        for i in range(0, len(channels), chunk_size):
            chunk = channels[i:i+chunk_size]
            tasks = [c.delete() for c in chunk]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            deleted += sum(1 for r in results if not isinstance(r, Exception))
            print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {deleted}/{len(channels)}")
        
        print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {deleted} channels deleted!")
    else:
        print(f"{DARK_BLUE}[!]{WHITE} Cancelled!")
    
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def spam_all(guild):
    clear()
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print(f"{DARK_BLUE}{BOLD}  [3] SPAM ALL")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    
    if not text_channels:
        print(f"{DARK_BLUE}[!]{WHITE} No text channels!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {len(text_channels)} channels")
    print("")
    
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Times: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Sending {count} messages to {len(text_channels)} channels...\n")
    
    all_tasks = []
    for channel in text_channels:
        for i in range(count):
            all_tasks.append(channel.send(msg))
    
    chunk_size = 100
    sent = 0
    
    for i in range(0, len(all_tasks), chunk_size):
        chunk = all_tasks[i:i+chunk_size]
        results = await asyncio.gather(*chunk, return_exceptions=True)
        sent += sum(1 for r in results if not isinstance(r, Exception))
        print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {sent}/{len(all_tasks)}")
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Sent {sent} messages!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def main_menu(guild):
    clear()
    print(f"""
{DARK_BLUE}{BOLD} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{DARK_BLUE}{BOLD}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{DARK_BLUE}{BOLD}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{DARK_BLUE}{BOLD}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{DARK_BLUE}{BOLD}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{DARK_BLUE}{BOLD} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {guild.name}")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    print(f"{DARK_BLUE}{BOLD}╔════════════════════════════════════════════════╗")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}              RYNDE BOT v8                     {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         {bot.user}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         Server: {guild.name}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         ID: {guild.id}              {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}║{WHITE}         Developer: 3zF                      {DARK_BLUE}{BOLD}║")
    print(f"{DARK_BLUE}{BOLD}╚════════════════════════════════════════════════╝")
    print("")
    print(f"  {DARK_BLUE}[{CYAN}1{DARK_BLUE}]{WHITE} Create Rooms")
    print(f"  {DARK_BLUE}[{CYAN}2{DARK_BLUE}]{WHITE} Delete All")
    print(f"  {DARK_BLUE}[{CYAN}3{DARK_BLUE}]{WHITE} Spam All")
    print(f"  {DARK_BLUE}[{CYAN}4{DARK_BLUE}]{WHITE} Exit")
    print("")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    while True:
        try:
            cmd = input(f"{DARK_BLUE}[?]{WHITE} Option (1-4): ").strip()
            
            if cmd == "1":
                await create_rooms(guild)
                break
            elif cmd == "2":
                await delete_all(guild)
                break
            elif cmd == "3":
                await spam_all(guild)
                break
            elif cmd == "4":
                print(f"{DARK_BLUE}[!]{WHITE} Exiting...")
                await bot.close()
                sys.exit()
            else:
                print(f"{DARK_BLUE}[!]{WHITE} Invalid!")
                
        except KeyboardInterrupt:
            print(f"\n{DARK_BLUE}[!]{WHITE} Exiting...")
            await bot.close()
            sys.exit()

try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print(f"{DARK_BLUE}[!]{WHITE} Invalid Token!")
except Exception as e:
    print(f"{DARK_BLUE}[!]{WHITE} Error: {e}")
