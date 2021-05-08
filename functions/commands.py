import colorama, ctypes, os, threading, time
from functions.iptools import iptools_setup
from functions.tasks import kill
from colorama import Fore, init
from pypresence import Presence

clear = lambda: os.system("cls")
tasks = []

def cmd():
      try:
            RPC = Presence("838621119799099433")
            RPC.connect()
            RPC.update(state="In commands module", details="About to input a command", large_image="pcfire", large_text="Made by Jaylen!", start=time.time(),
                  buttons=[{"label": "Download", "url": "https://google.com"}])
      except Exception as e:
            print(e)
      ctypes.windll.kernel32.SetConsoleTitleW(f"Commands [BETA] Active Threads: {threading.activeCount()}")
      init(autoreset=True, convert=True)
      clear()
      print(f"{Fore.BLUE}[?] Available modules\n"
            f"iptools: Get info about ip and stuff ")
      
      while 1:
            module = input("< ")
            
            if module.lower() == "iptools":
                  tasks.append("Iptools")
                  clear()
                  iptools_setup()
                  
            if module.lower() == "tasks":
                  show_tasks = ", ".join(tasks)
                  print(f"{Fore.LIGHTBLUE_EX}Active tasks: {show_tasks}")
                  
            if module.lower() == "geoip":
                  pass
                  
            #BETA      
            if module.lower() == "kill":
                  kill()
                  
            else:
                  print(f"{Fore.RED}[!] Not a command")