import subprocess, sys, random, colorama, threading, json, os, time
from colorama import Fore, init
from subprocess import Popen, CREATE_NEW_CONSOLE
from functions.ipfuctions import send, query


#Move functions?

clear = lambda: os.system("cls")

def iptools_setup():
    init(autoreset=True, convert=True)
    print(f"{Fore.GREEN}Available commands for iptools: \n"
          f"Sendp: Sends packet attack using given parms \n"
          f"Ipinfo: Sends ip to api to get info")
    while 1:
        cmd = input("< ")
        
        #Fix later
        if cmd.lower() == "back":
            from functions.commands import cmd
            cmd()
            
            
        #Gets info of ip
        if cmd.lower() == "ipinfo":
            init(autoreset=True, convert=True)
            config = input(f"{Fore.LIGHTBLUE_EX}[TOO LAZY TO FIX USE 'N'] Do you want to use load from config? (Y/N)")
            
            if config.lower() == "y":
                ip = config["Iptools"]["target"]
                query(ip)
            
            if config.lower() == "n":
                ip = input(f"{Fore.LIGHTBLUE_EX}Input the ip you want to check: ")
                print(f"{Fore.GREEN}[?]Sending request\n"
                      "Writing to output folder")
                query(ip)
        
        
        #Send packets
        if cmd.lower() == "sendp":
            clear()
            use_config = input(f"{Fore.YELLOW}[!] Would you like to load from config (Y/N) ")
            
    
            if use_config.lower() == "y":
                clear()
                print(f"{Fore.GREEN} Loading from config...")
                config = json.load(open("config.json"))
                target = config["Iptools"]["target"]
                ip_spoof = config["Iptools"]["IP_Spoof"]
                _output = config["Iptools"]["Show_Output"]
                count = config["Iptools"]["Packet_Count"]
                ping = config["Iptools"]["Ping_IP"]
            
                if _output.lower() == "false":
                    output = 0

                if _output.lower() == "true":
                    output = 1
                    
                if ping.lower() =="true":
                    Popen(f"ping {target} -t", creationflags=CREATE_NEW_CONSOLE)
                
                if ping.lower() == "false":
                    print(f"\n{Fore.RED}[!] Auto ping is disabled")
                    
                    
                
                print(f"{Fore.GREEN}[!] Sending packets to {target} with {count} packets...")
                from functions.commands import cmd
                threading.Thread(target=send, args=(target, output, int(count))).start()
                clear()
                cmd()
                
                
            if use_config.lower() == "n":
                target = input(str(f"{Fore.RED}[!] Input the target ip to attack: "))
                out = input(str(f"{Fore.RED}[!] Show output? (y/n) "))
                count = input(f"{Fore.RED}[!] Amount of packets to send per: ")
                ping = input(str(f"{Fore.RED}[!] Ping target? (y/n) "))
                
                if out.lower() == "y":
                    output = 1

                if out.lower() == "n":
                    output = 0
                    
                if ping.lower() =="y":
                    Popen(f"ping {target} -t", creationflags=CREATE_NEW_CONSOLE)
                
                if ping.lower() == "n":
                    print(f"\n{Fore.RED}[!] Disabled auto ping")
                    
                print(f"{Fore.GREEN}[!] Sending packets to {target} with {count} packets...")
                from functions.commands import cmd
                threading.Thread(target=send, args=(target, output, int(count))).start()
                clear()
                cmd()
            