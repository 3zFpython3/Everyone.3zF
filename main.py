#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import sys
import time

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
            await main_menu(guild)
        else:
            print(f"{DARK_BLUE}[!]{WHITE} Invalid!")
            await bot.close()
            
    except ValueError:
        print(f"{DARK_BLUE}[!]{WHITE} Number!")
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
    print(f"  {DARK_BLUE}[{CYAN}1{DARK_BLUE}]{WHITE} Create")
    print(f"  {DARK_BLUE}[{CYAN}2{DARK_BLUE}]{WHITE} Delete")
    print(f"  {DARK_BLUE}[{CYAN}3{DARK_BLUE}]{WHITE} Spam")
    print(f"  {DARK_BLUE}[{CYAN}4{DARK_BLUE}]{WHITE} DM")
    print(f"  {DARK_BLUE}[{CYAN}5{DARK_BLUE}]{WHITE} Webhook")
    print(f"  {DARK_BLUE}[{CYAN}6{DARK_BLUE}]{WHITE} Exit")
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
                print(f"{DARK_BLUE}[!]{WHITE} Exiting...")
                await bot.close()
                sys.exit()
            else:
                print(f"{DARK_BLUE}[!]{WHITE} Invalid!")
                
        except KeyboardInterrupt:
            print(f"\n{DARK_BLUE}[!]{WHITE} Exiting...")
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
    
    chunk = 1000
    created = 0
    total = count
    
    for i in range(0, count, chunk):
        batch = min(chunk, count - i)
        tasks = []
        for j in range(batch):
            tasks.append(guild.create_text_channel(name))
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for r in results:
            if not isinstance(r, Exception):
                print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Created: {name}")
                created += 1
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {created} rooms created!")
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
    
    confirm = input(f"{DARK_BLUE}[{RED}!{DARK_BLUE}]{WHITE} Delete ALL? (y/n): ").strip().lower()
    
    if confirm == "y":
        print(f"\n{DARK_BLUE}[+]{WHITE} Deleting all channels...\n")
        
        chunk = 200
        deleted = 0
        channels = list(guild.channels)
        total = len(channels)
        
        for i in range(0, len(channels), chunk):
            batch = channels[i:i+chunk]
            tasks = [c.delete() for c in batch]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for idx, r in enumerate(results):
                if not isinstance(r, Exception):
                    print(f"{DARK_BLUE}[{RED}-{DARK_BLUE}]{WHITE} Deleted: {batch[idx].name}")
                    deleted += 1
        
        print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {deleted} channels deleted!")
    else:
        print(f"{DARK_BLUE}[!]{WHITE} Cancelled!")
    
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
        print(f"{DARK_BLUE}[!]{WHITE} No channels!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {len(channels)} channels")
    print("")
    
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Times: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Spamming {count} messages to {len(channels)} channels...\n")
    
    total = len(channels) * count
    sent = 0
    tasks = []
    task_info = []
    
    for ch in channels:
        for i in range(count):
            tasks.append(ch.send(msg))
            task_info.append(f"{msg}")
    
    chunk = 1000
    
    for i in range(0, len(tasks), chunk):
        batch = tasks[i:i+chunk]
        info_batch = task_info[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for idx, r in enumerate(results):
            if not isinstance(r, Exception):
                print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Sent: {info_batch[idx]}")
                sent += 1
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {sent} messages sent!")
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
        print(f"{DARK_BLUE}[!]{WHITE} No members!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {len(members)} members")
    print("")
    
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Sending DM to {len(members)} members...\n")
    
    sent = 0
    chunk = 100
    total = len(members)
    
    for i in range(0, len(members), chunk):
        batch = members[i:i+chunk]
        tasks = []
        task_info = []
        for m in batch:
            try:
                dm = await m.create_dm()
                tasks.append(dm.send(msg))
                task_info.append(f"{msg}")
            except:
                pass
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for idx, r in enumerate(results):
                if not isinstance(r, Exception):
                    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Sent DM: {task_info[idx]}")
                    sent += 1
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {sent} DMs sent!")
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
        print(f"{DARK_BLUE}[!]{WHITE} No channels!")
        print("")
        input(f"{DARK_BLUE}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {len(channels)} channels")
    print("")
    
    name = input(f"{DARK_BLUE}[?]{WHITE} Webhook Name: ").strip()
    msg = input(f"{DARK_BLUE}[?]{WHITE} Message: ").strip()
    count = int(input(f"{DARK_BLUE}[?]{WHITE} Per channel: ").strip())
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Creating {count} webhooks in {len(channels)} channels...\n")
    
    # MAX SPEED - Create all webhooks at once
    all_tasks = []
    all_channels = []
    for ch in channels:
        for i in range(count):
            all_tasks.append(ch.create_webhook(name=name))
            all_channels.append(ch.name)
    
    chunk = 500
    created = 0
    total = len(all_tasks)
    all_webhooks = []
    
    for i in range(0, len(all_tasks), chunk):
        batch = all_tasks[i:i+chunk]
        channel_batch = all_channels[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for idx, r in enumerate(results):
            if not isinstance(r, Exception):
                print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Created: {channel_batch[idx]}")
                all_webhooks.append(r)
                created += 1
    
    print(f"\n{DARK_BLUE}[+]{WHITE} Spamming with {len(all_webhooks)} webhooks...\n")
    
    # MAX SPEED - Send all messages at once
    spam_tasks = []
    spam_info = []
    for idx, wh in enumerate(all_webhooks):
        for i in range(5):
            spam_tasks.append(wh.send(msg))
            spam_info.append(f"{msg}")
    
    chunk = 500
    sent = 0
    total_spam = len(spam_tasks)
    
    for i in range(0, len(spam_tasks), chunk):
        batch = spam_tasks[i:i+chunk]
        info_batch = spam_info[i:i+chunk]
        results = await asyncio.gather(*batch, return_exceptions=True)
        for idx, r in enumerate(results):
            if not isinstance(r, Exception):
                print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} Sent: {info_batch[idx]}")
                sent += 1
    
    print(f"\n{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {created} webhooks created!")
    print(f"{DARK_BLUE}[{GREEN}+{DARK_BLUE}]{WHITE} {sent} messages sent!")
    print("")
    input(f"{DARK_BLUE}[?]{WHITE} Enter...")
    await main_menu(guild)

try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print(f"{DARK_BLUE}[!]{WHITE} Invalid Token!")
except Exception as e:
    print(f"{DARK_BLUE}[!]{WHITE} Error: {e}")
