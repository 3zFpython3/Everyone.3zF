
#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

BLUE = Fore.BLUE + Style.BRIGHT
CYAN = Fore.CYAN
WHITE = Fore.WHITE
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

clear()

print(f"{BLUE}=" * 60)
print(f"{BLUE}            RYNDE BOT V7")
print(f"{BLUE}=" * 60)
print("")

TOKEN = input(f"{CYAN}[?]{WHITE} Token: ").strip()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    clear()
    print(f"""
{BLUE} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{BLUE}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{BLUE}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{BLUE}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{BLUE}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{BLUE} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print(f"{BLUE}=" * 60)
    print(f"{GREEN}[✓]{WHITE} {bot.user}")
    print(f"{GREEN}[✓]{WHITE} {len(bot.guilds)} Servers")
    print(f"{BLUE}=" * 60)
    print("")
    
    print(f"{CYAN}[?]{WHITE} Server:")
    print("")
    for i, guild in enumerate(bot.guilds, 1):
        print(f"  {BLUE}[{CYAN}{i}{BLUE}]{WHITE} {guild.name}")
    print("")
    print(f"{BLUE}=" * 60)
    print("")
    
    try:
        choice = int(input(f"{CYAN}[?]{WHITE} Number: ").strip())
        
        if 1 <= choice <= len(bot.guilds):
            guild = bot.guilds[choice - 1]
            clear()
            print(f"""
{BLUE} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{BLUE}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{BLUE}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{BLUE}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{BLUE}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{BLUE} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
            print(f"{BLUE}=" * 60)
            print(f"{GREEN}[✓]{WHITE} {guild.name}")
            print(f"{BLUE}=" * 60)
            print("")
            print(f"  {BLUE}[{CYAN}1{BLUE}]{WHITE} Create Rooms")
            print(f"  {BLUE}[{CYAN}2{BLUE}]{WHITE} Delete All")
            print(f"  {BLUE}[{CYAN}3{BLUE}]{WHITE} Spam All")
            print(f"  {BLUE}[{CYAN}4{BLUE}]{WHITE} Exit")
            print("")
            print(f"{BLUE}=" * 60)
            print("")
            
            while True:
                try:
                    cmd = input(f"{CYAN}[?]{WHITE} Option (1-4): ").strip()
                    
                    if cmd == "1":
                        await create_rooms(guild)
                    elif cmd == "2":
                        await delete_all(guild)
                    elif cmd == "3":
                        await spam_all(guild)
                    elif cmd == "4":
                        print(f"{YELLOW}[!]{WHITE} Exiting...")
                        await bot.close()
                        sys.exit()
                    else:
                        print(f"{RED}[!]{WHITE} Invalid!")
                        
                except KeyboardInterrupt:
                    print(f"\n{YELLOW}[!]{WHITE} Exiting...")
                    await bot.close()
                    sys.exit()
        else:
            print(f"{RED}[!]{WHITE} Invalid!")
            await bot.close()
            
    except ValueError:
        print(f"{RED}[!]{WHITE} Number!")
        await bot.close()

async def create_rooms(guild):
    clear()
    print(f"{BLUE}=" * 60)
    print(f"{BLUE}  [1] CREATE ROOMS")
    print(f"{BLUE}=" * 60)
    print("")
    
    name = input(f"{CYAN}[?]{WHITE} Name: ").strip()
    count = int(input(f"{CYAN}[?]{WHITE} Count: ").strip())
    
    print(f"\n{CYAN}[+]{WHITE} Creating {count} rooms...\n")
    
    # دفعة وحدة متوازية
    tasks = [guild.create_text_channel(name) for _ in range(count)]
    channels = await asyncio.gather(*tasks, return_exceptions=True)
    created = sum(1 for c in channels if not isinstance(c, Exception))
    
    print(f"{GREEN}[✓]{WHITE} {created} rooms created!")
    print("")
    input(f"{CYAN}[?]{WHITE} Enter...")
    await main_menu(guild)

async def delete_all(guild):
    clear()
    print(f"{BLUE}=" * 60)
    print(f"{BLUE}  [2] DELETE ALL")
    print(f"{BLUE}=" * 60)
    print("")
    
    confirm = input(f"{RED}[⚠]{WHITE} Delete ALL? (y/n): ").strip().lower()
    
    if confirm == "y":
        print(f"\n{CYAN}[+]{WHITE} Deleting all channels...\n")
        
        # دفعة وحدة متوازية
        tasks = [channel.delete() for channel in guild.channels]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        deleted = sum(1 for r in results if not isinstance(r, Exception))
        
        print(f"{GREEN}[✓]{WHITE} {deleted} channels deleted!")
    else:
        print(f"{YELLOW}[!]{WHITE} Cancelled!")
    
    print("")
    input(f"{CYAN}[?]{WHITE} Enter...")
    await main_menu(guild)

async def spam_all(guild):
    clear()
    print(f"{BLUE}=" * 60)
    print(f"{BLUE}  [3] SPAM ALL")
    print(f"{BLUE}=" * 60)
    print("")
    
    # جلب كل الرومات النصية
    text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
    
    if not text_channels:
        print(f"{RED}[!]{WHITE} No text channels found!")
        print("")
        input(f"{CYAN}[?]{WHITE} Enter...")
        await main_menu(guild)
        return
    
    print(f"{GREEN}[✓]{WHITE} Found {len(text_channels)} text channels")
    print("")
    
    msg = input(f"{CYAN}[?]{WHITE} Message: ").strip()
    count = int(input(f"{CYAN}[?]{WHITE} Times per channel: ").strip())
    
    print(f"\n{CYAN}[+]{WHITE} Sending {count} messages to {len(text_channels)} channels...\n")
    
    # دفعة وحدة متوازية لكل الرومات
    all_tasks = []
    for channel in text_channels:
        for i in range(count):
            all_tasks.append(channel.send(msg))
    
    results = await asyncio.gather(*all_tasks, return_exceptions=True)
    sent = sum(1 for r in results if not isinstance(r, Exception))
    
    print(f"{GREEN}[✓]{WHITE} Sent {sent} messages to {len(text_channels)} channels!")
    print("")
    input(f"{CYAN}[?]{WHITE} Enter...")
    await main_menu(guild)

async def main_menu(guild):
    clear()
    print(f"""
{BLUE} ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
{BLUE}██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
{BLUE}██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
{BLUE}██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
{BLUE}╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
{BLUE} ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print(f"{BLUE}=" * 60)
    print(f"{GREEN}[✓]{WHITE} {guild.name}")
    print(f"{BLUE}=" * 60)
    print("")
    print(f"  {BLUE}[{CYAN}1{BLUE}]{WHITE} Create Rooms")
    print(f"  {BLUE}[{CYAN}2{BLUE}]{WHITE} Delete All")
    print(f"  {BLUE}[{CYAN}3{BLUE}]{WHITE} Spam All")
    print(f"  {BLUE}[{CYAN}4{BLUE}]{WHITE} Exit")
    print("")
    print(f"{BLUE}=" * 60)
    print("")
    
    while True:
        try:
            cmd = input(f"{CYAN}[?]{WHITE} Option (1-4): ").strip()
            
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
                print(f"{YELLOW}[!]{WHITE} Exiting...")
                await bot.close()
                sys.exit()
            else:
                print(f"{RED}[!]{WHITE} Invalid!")
                
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[!]{WHITE} Exiting...")
            await bot.close()
            sys.exit()

try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print(f"{RED}[!]{WHITE} Invalid Token!")
except Exception as e:
    print(f"{RED}[!]{WHITE} Error: {e}")
