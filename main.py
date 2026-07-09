#!/usr/bin/env python3

import discord
from discord.ext import commands
import asyncio
import os
import sys

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

clear()

print("=" * 50)
print("            RYNDE BOT V4")
print("=" * 50)
print("")

TOKEN = input("[?] Enter Bot Token: ").strip()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    clear()
    print("""
 ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print("=" * 50)
    print(f"[✓] Bot : {bot.user}")
    print(f"[✓] Servers : {len(bot.guilds)}")
    print("=" * 50)
    print("")
    
    # عرض السيرفرات
    print("[?] Select Server:")
    print("")
    for i, guild in enumerate(bot.guilds, 1):
        print(f"  [{i}] {guild.name}")
    print("")
    print("=" * 50)
    print("")
    
    # اختيار السيرفر
    try:
        choice = int(input("[?] Enter server number: ").strip())
        
        if 1 <= choice <= len(bot.guilds):
            guild = bot.guilds[choice - 1]
            clear()
            print("""
 ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
            print("=" * 50)
            print(f"[✓] Server : {guild.name}")
            print("=" * 50)
            print("")
            print("  [1] Create Rooms")
            print("  [2] Delete Rooms")
            print("  [3] Create + Spam")
            print("  [4] Nuke Rooms")
            print("  [5] Create Rooms Fast")
            print("  [6] Delete All Channels")
            print("  [7] Exit")
            print("")
            print("=" * 50)
            print("")
            
            # اختيار الأمر
            while True:
                try:
                    cmd = input("[?] Choose option (1-7): ").strip()
                    
                    if cmd == "1":
                        await create_rooms_terminal(guild)
                    elif cmd == "2":
                        await delete_rooms_terminal(guild)
                    elif cmd == "3":
                        await spam_rooms_terminal(guild)
                    elif cmd == "4":
                        await nuke_rooms_terminal(guild)
                    elif cmd == "5":
                        await fast_rooms_terminal(guild)
                    elif cmd == "6":
                        await delete_all_terminal(guild)
                    elif cmd == "7":
                        print("[!] Exiting...")
                        await bot.close()
                        sys.exit()
                    else:
                        print("[!] Invalid choice! Try again.")
                        
                except KeyboardInterrupt:
                    print("\n[!] Exiting...")
                    await bot.close()
                    sys.exit()
        else:
            print("[!] Invalid server number!")
            await bot.close()
            
    except ValueError:
        print("[!] Enter a number!")
        await bot.close()

# ============= FUNCTIONS =============

async def create_rooms_terminal(guild):
    clear()
    print("=" * 50)
    print("  [1] CREATE ROOMS")
    print("=" * 50)
    print("")
    
    name = input("[?] Room name: ").strip()
    count = int(input("[?] How many rooms: ").strip())
    
    print(f"[+] Creating {count} rooms...")
    created = 0
    for i in range(1, count + 1):
        try:
            await guild.create_text_channel(f"{name}-{i}")
            created += 1
            print(f"  [✓] Created {name}-{i}")
            await asyncio.sleep(0.3)
        except Exception as e:
            print(f"  [✗] Error: {e}")
    
    print("")
    print(f"[✓] Created {created} rooms!")
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def delete_rooms_terminal(guild):
    clear()
    print("=" * 50)
    print("  [2] DELETE ROOMS")
    print("=" * 50)
    print("")
    
    name = input("[?] Room name to delete: ").strip()
    
    print(f"[+] Deleting rooms with name '{name}'...")
    deleted = 0
    for channel in guild.channels:
        if name in channel.name and channel.name.startswith(name):
            try:
                await channel.delete()
                deleted += 1
                print(f"  [✓] Deleted {channel.name}")
                await asyncio.sleep(0.3)
            except:
                pass
    
    print("")
    print(f"[✓] Deleted {deleted} rooms!")
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def spam_rooms_terminal(guild):
    clear()
    print("=" * 50)
    print("  [3] CREATE + SPAM")
    print("=" * 50)
    print("")
    
    name = input("[?] Room name: ").strip()
    count = int(input("[?] How many rooms: ").strip())
    
    print(f"[+] Creating {count} rooms with spam...")
    for i in range(1, count + 1):
        try:
            channel = await guild.create_text_channel(f"{name}-{i}")
            print(f"  [✓] Created {name}-{i}")
            await asyncio.sleep(0.5)
            for j in range(3):
                await channel.send(f"SPAM {j+1}")
                await asyncio.sleep(0.2)
            print(f"  [✓] Spammed {name}-{i}")
        except Exception as e:
            print(f"  [✗] Error: {e}")
    
    print("")
    print(f"[✓] Created {count} rooms with spam!")
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def nuke_rooms_terminal(guild):
    clear()
    print("=" * 50)
    print("  [4] NUKE ROOMS")
    print("=" * 50)
    print("")
    
    name = input("[?] Room name to nuke: ").strip()
    
    print(f"[+] Nuking all '{name}' rooms...")
    deleted = 0
    for channel in guild.channels:
        if name in channel.name and channel.name.startswith(name):
            try:
                await channel.delete()
                deleted += 1
                print(f"  [✓] Nuked {channel.name}")
                await asyncio.sleep(0.2)
            except:
                pass
    
    print("")
    print(f"[✓] Nuked {deleted} rooms!")
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def fast_rooms_terminal(guild):
    clear()
    print("=" * 50)
    print("  [5] CREATE ROOMS FAST")
    print("=" * 50)
    print("")
    
    name = input("[?] Room name: ").strip()
    count = int(input("[?] How many rooms: ").strip())
    
    print(f"[+] Creating {count} rooms fast...")
    created = 0
    for i in range(1, count + 1):
        try:
            await guild.create_text_channel(f"{name}-{i}")
            created += 1
        except:
            pass
    
    print("")
    print(f"[✓] Created {created} rooms!")
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def delete_all_terminal(guild):
    clear()
    print("=" * 50)
    print("  [6] DELETE ALL CHANNELS")
    print("=" * 50)
    print("")
    
    confirm = input("[?] Delete ALL channels? (yes/no): ").strip().lower()
    
    if confirm == "yes":
        print("[+] Deleting all channels...")
        deleted = 0
        for channel in guild.channels:
            try:
                await channel.delete()
                deleted += 1
                print(f"  [✓] Deleted {channel.name}")
                await asyncio.sleep(0.2)
            except:
                pass
        print("")
        print(f"[✓] Deleted {deleted} channels!")
    else:
        print("[!] Cancelled!")
    
    print("")
    input("[?] Press Enter to continue...")
    await main_menu(guild)

async def main_menu(guild):
    clear()
    print("""
 ██████╗██╗   ██╗███╗   ██╗██████╗ ███████╗
██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝
██║     ██║   ██║██╔██╗ ██║██████╔╝███████╗
██║     ██║   ██║██║╚██╗██║██╔══██╗╚════██║
╚██████╗╚██████╔╝██║ ╚████║██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print("=" * 50)
    print(f"[✓] Server : {guild.name}")
    print("=" * 50)
    print("")
    print("  [1] Create Rooms")
    print("  [2] Delete Rooms")
    print("  [3] Create + Spam")
    print("  [4] Nuke Rooms")
    print("  [5] Create Rooms Fast")
    print("  [6] Delete All Channels")
    print("  [7] Exit")
    print("")
    print("=" * 50)
    print("")
    
    while True:
        try:
            cmd = input("[?] Choose option (1-7): ").strip()
            
            if cmd == "1":
                await create_rooms_terminal(guild)
                break
            elif cmd == "2":
                await delete_rooms_terminal(guild)
                break
            elif cmd == "3":
                await spam_rooms_terminal(guild)
                break
            elif cmd == "4":
                await nuke_rooms_terminal(guild)
                break
            elif cmd == "5":
                await fast_rooms_terminal(guild)
                break
            elif cmd == "6":
                await delete_all_terminal(guild)
                break
            elif cmd == "7":
                print("[!] Exiting...")
                await bot.close()
                sys.exit()
            else:
                print("[!] Invalid choice! Try again.")
                
        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            await bot.close()
            sys.exit()
        except ValueError:
            print("[!] Enter a number!")

# ============= RUN =============
try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print("[!] Invalid Token!")
except Exception as e:
    print(f"[!] Error: {e}")
