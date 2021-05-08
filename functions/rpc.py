from pypresence import Presence 
import time

state = "Test"
details = "FUCK SLUGO"
large_image = "pcfire"
large_text = "RETARD"
Buton1Label = "FUCK SLUGO"
Buton1Url = "https://pornhub.com"
start = time.time()


while True:
    client_id = "838621119799099433"
    RPC = Presence(client_id)

    RPC.connect() # Start the handshake loop

    RPC.update(state="TEST", details="FUCK SLUGO", large_image="pcfire", start=time.time()) 
    RPC.update(state=state, details=details, large_image=large_image, large_text=large_text,
               buttons=[{"label": Buton1Label, "url": Buton1Url}]) 


    #RPC.update()