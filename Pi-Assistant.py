#!/usr/bin/env python

"""Pi-assitantV2.1 free-use and modifications allowed for non-commercial projects"""



from Tkinter import *
import time
import os


assistant = Tk()
assistant.title("Pi-assitant V2.1")
assistant.resizable(0,0)
#######Programming Functions
def raspbian():
    print "opening raspbian menu."
    os.system("sudo raspi-config")

def reboot():
    os.system("reboot")

def poweroff():
    os.system("poweroff")

def clean():
    print "Preparing update cycle"
    os.system("sudo apt-get clean")
    print "STATUS: Done"

def update():
    print "Updating system"
    os.system("sudo apt-get update")
    print "STATUS: Done"

def upgrade():
    print "Upgrading system"
    os.system("sudo apt-get upgrade")
    print "STATUS: Done"

def leafpad():
    print "Installing Leafpad"
    os.system("sudo apt-get install leafpad")
    print "STATUS: Done"

def config():
    print "Opening config.txt file, follow the manual closely."
    os.system("sudo leafpad /boot/config.txt")
    print "Reboot the system when you are ready."

def userctr():
    print "opening lighdm.config, follow the manual closely."
    os.system("sudo leafpad /etc/lightdm/lightdm.conf")
    print "Reboot the system when you are ready."

def analogue():
    print "Sound output is set to analogue"
    os.system("amixer cset numid=3 1")

def hdmi():
    print "Sound output is set to HDMI"
    os.system("amixer cset numid=3 2")

def default():
    print "Sound output is set to autoselect"
    os.system("amixer cset numid=3 0")

def close():
    print "Thanks for using Pi-assistant."
    time.sleep(1)
    exit()

########Programming Frames
topframe = Frame(assistant, pady=8, padx=8)
topframe.pack(side=TOP, pady = 8)

lowestframe = Frame(assistant, pady=8, padx=8)
lowestframe.pack(side=BOTTOM, pady = 8)

#frame in frame

leftframe = LabelFrame(topframe, text="Config help", pady=8, padx=8)
leftframe.config(bd = 4, font="bold")
leftframe.pack(side=LEFT, pady = 8)

leftcenterframe = LabelFrame(topframe, text="Update tools", pady=8, padx=8)
leftcenterframe.config(bd = 4, font="bold")
leftcenterframe.pack(side=LEFT, pady = 8)

rightframe = LabelFrame(topframe, text="Audio out help", pady=8, padx=8)
rightframe.config(bd = 4, font="bold")
rightframe.pack(side=RIGHT, pady = 8)

rightcenterframe = LabelFrame(topframe, text="Text In/Out", pady=8, padx=8)
rightcenterframe.config(bd = 4, font="bold")
rightcenterframe.pack(side=RIGHT, pady = 8)




#######Programming buttons and assigning them to frames
raspbian = Button(leftframe, text="Raspbian Configuration Tool", command=raspbian)
raspbian.config(height = 3, width = 30)
raspbian.pack()

reboot = Button(leftframe, text="Reboot", command=reboot)
reboot.config(height = 3, width = 30)
reboot.pack()

poweroff = Button(leftframe, text="Poweroff", command=poweroff)
poweroff.config(height = 3, width = 30)
poweroff.pack()

clean = Button(leftcenterframe, text="PHASE1: Clean (preparing system)", command=clean)
clean.config(height = 3, width = 30)
clean.pack()

update = Button(leftcenterframe, text="PHASE2: Update (getting packages)", command=update)
update.config(height = 3, width = 30)
update.pack()

upgrade = Button(leftcenterframe, text="PHASE3: Upgrade (upgrading system)", command=upgrade)
upgrade.config(height = 3, width = 30)
upgrade.pack()

leafpad = Button (rightcenterframe, text="Install Leafpad", command=leafpad)
leafpad.config(height = 3, width = 30)
leafpad.pack()

config = Button(rightcenterframe, text="Open config.txt-file", command=config)
config.config(height = 3, width = 30)
config.pack()

userctr = Button(rightcenterframe, text="Usercontrol", command=userctr)
userctr.config(height = 3, width = 30)
userctr.pack()

analogue = Button(rightframe, text="Switch sound to analogue output", command=analogue)
analogue.config(height = 3, width = 30)
analogue.pack()

hdmi = Button(rightframe, text="Switch sound to HDMI output", command=hdmi)
hdmi.config(height = 3, width = 30)
hdmi.pack()

default = Button(rightframe, text="Default option (autoselect)", command=default)
default.config(height = 3, width = 30)
default.pack()

close = Button(lowestframe, text="Close Pi-assistant", command = close)
close.config(bg = "orange")
close.config(height = 3, width = 120)
close.pack()


assistant.mainloop()
