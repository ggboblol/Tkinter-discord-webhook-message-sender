# Tkinter-discord-webhook-message-sender
This program sends your input message to discord through your webhook url

When during execution you can also change the url with out terminating the program.

To add more webhook urls modify the code the way you want and also taking help from [here](https://pypi.org/project/discord-webhook/)

# Requirements
This project works both in windows and linux

**For Windows(works better in virtual environment like pycharm):**
  1. pip install discord-webhooks
  2. pip install tkinter
 
**For linux(debian):**
  1. python3: `sudo apt install python3`
  2. discord_webhooks: `sudo pip3 install discord-webhooks`
  3. tkinter: `sudo pip3 install tkinter`
  
  **HOW TO GET YOUR DISCORD WEBHOOK URL(NEEDED):**

https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

# Procedure
  1. First download the repo using the command `git clone https://github.com/thinker010/Tkinter-discord-webhook-message-sender.git`(linux) or donwload the zip file directly(windows).
  2. Both the files `main.py` and `webhookurl.txt` need to be in same folder.
  3. Then add your discord webhook url to the `webhookurl.txt` file replacing the `YOUR WEBHOOK URL` text.(make sure there is no space or new line in the `webhookurl.txt` file after the url or it'll give error.)
  4. then if your in linux make it an executable file by typing in terminal `chmod +x main.py`.
  5. directly execute in windows and in linux type the command `sudo python3 main.py`.
  
  # Source
  https://pypi.org/project/discord-webhook/
  
  # More help or issue
[Click here](https://github.com/thinker010/Discord-raspberry-pi-startup-notifier/issues)
