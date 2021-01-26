#! python3
import tkinter as tk
from discord_webhook import DiscordWebhook

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def msgsend():
    file1 = open("webhookurl.txt", "r")
    xurl = file1.read()
    x1 = entry1.get()
    webhook = DiscordWebhook(url=xurl,content=x1)
    response = webhook.execute()
    file1.close()

button1 = tk.Button(text='send', command=msgsend)
canvas1.create_window(200, 180, window=button1)
root.mainloop()
