import subprocess, sys, ctypes, os
from functions.commands import cmd

#Variables
clear = lambda: os.system("cls")


#Setup
def setup():
    open("install.log", 'a').close()
    log = open("install.log", "w")
    requirements = open("requirements.txt").read().splitlines()
    ctypes.windll.kernel32.SetConsoleTitleW("Installing packages...")
    
    try:
        import pip
    except Exception:
        print("Pip isn't installed please download from https://www.python.org/")
        
    try:
        for package in requirements:
            print(f"[!] Attempting to install {package}...")
            install = subprocess.call([sys.executable, "-m", "pip", "install", package, "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
            print(f"[!] Successfully installed {package}")
            clear()
        os.system("cmd /C python setup.py --setup")
        quit(-1)
            
    except Exception as e:
        print(e)
        

#Update later
def pre_setup():
    for arg in sys.argv:
        #Calls setup if no args
        if len(sys.argv) == 1:
            setup()
            
        #Skips setup
        if arg == "--setup":
            cmd()

pre_setup()

