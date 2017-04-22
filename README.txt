VERSION: 2.1

###########################################################################
###########################################################################
###############                  INSTALLING                 ###############
###########################################################################
PLEASE NOTE:
- Follow these steps closely, they make scripts executable and will prevent visitors from tinkering with your files!
- Use the following line of code: (next line)
/usr/bin/python %f

1) After downloading copy the folder to a USB memory stick
2) Insert the USB memory stick in your Raspberry Pi and copy the Pi-Assistant folder to your desktop.
3) Open the copied folder, right click the "pi-assistant.py" file
4) Click the "Open with" tab, in the dropdown menu that appears click "Customize"
5) Click the tab "Custom command line"
6) Type this in the top-field: /usr/bin/python %f
7) Tick the first checkbox ("Execute in terminal emulator")
8) Give this configuration a name in the bottom field. e.g. Python execute
9) Click OK
10) Now you're back in the 'File Properties' menu, just click OK
11) Now the file-association is set and you can double-click the .py file to run each script.

12) Now you're back in the window with the File Properties:
13) Click the tab that says 'Permissions'.
14) Set all permissions to:
	View content: Anyone
	Change content: Only owner
	Execute: Nobody
15) Click 'OK'

16) Now we need to change the access permissions to that script, this will prevent undesired tampering with the Pi-Assistant.py-script.
17) Right click the Pi-Assistant folder.
18) Click 'Properties'
19) Click the tab that says 'Permissions'
20) Set all permissions to 'Only owner':
	View content: Only owner
	Change content: Only owner
	Execute: Only owner

21) Click 'OK'
If you followed these steps closely, you've now correctly configured the needed environmentals and all permissions.






###########################################################################
###########################################################################
###############                  FUNCTION                   ###############
###########################################################################
Description of all buttons:

Name: 		Raspbian Configuration Tool
Actions: 	Opens the Raspberry Pi's built in Configuration Menu.
Needs Sudo?: 	YES
Terminalcode: 	sudo raspi-config

Name: 		Reboot
Actions: 	Reboots the Raspberry Pi
Needs Sudo?: 	NO
Terminalcode: 	reboot

Name: 		Poweroff
Actions: 	Immediately closes all active programs and shuts the Raspberry Pi down.
Needs Sudo?: 	NO
Terminalcode: 	poweroff

Name: 		PHASE1: Clean (preparing system)
Actions: 	Prepares your system for new updates
Needs Sudo?: 	YES
Terminalcode: 	sudo apt-get clean

Name: 		PHASE2: Update(getting packages)
Actions: 	Downloads all packages, the user may be prompted when downloading new files.
Needs Sudo?: 	YES
Terminalcode: 	sudo apt-get upgrade

Name: 		PHASE3: Upgrade (upgrading system)
Actions: 	Installs all packages, the user may be prompted when downloading new files.
Needs Sudo?: 	YES
Terminalcode: 	sudo apt-get upgrade

Name: 		Install Leafpad
Actions: 	Installs the ASCII-text editor Leafpad. Pi-assistant uses this editor as it's a simpler tool than the nano-editor. (Please note that Leafpad is allready installed on your system. Only install it again if your system gives a related error.)
Needs Sudo?: 	YES
Terminalcode: 	sudo apt-get install leafpad

Name: 		Open config.txt-file
Actions: 	Opens the config.txt-file as sudo-user with write permissions.
Needs Sudo?: 	YES
Terminalcode: 	sudo leafpad /boot/config.txt

Name: 		Usercontrol
Actions: 	Opens the lightdm.conf-file as sudo-user with write permissions, don't mess around with this one!
Needs Sudo?: 	YES
Terminalcode: 	sudo leafpad /etc/lightdm/lightdm.conf

Name: 		Switch sound to analogue output
Actions: 	Forces the 3.5mm audiojack as output for sound.
Needs Sudo?: 	NO
Terminalcode: 	amixer cset numid=3 1

Name: 		Switch sound to HDMI output
Actions: 	Forces the HDMI as output for sound (you won't hear anything if the speakers on/connected to your HDMI-interface isn't properly configured)
Needs Sudo?: 	NO
Terminalcode: 	amixer cset numid=3 2

Name: 		Default option (autoselect)
Actions: 	Restore the sound output to its default setting, which is autoselect.
Needs Sudo?: 	NO
Terminalcode: 	amixer cset numid=3 0


Name: 		Close Pi-assitant
Actions: 	Closes the Pi-assitant
Needs Sudo?: 	NO
Terminalcode: 	exit()




###########################################################################
###########################################################################
###############                   CHANGELOG                 ###############
###########################################################################

FROM V1.0 to V2.0
- Adding an entire clickable GUI
- Adding the audio functionality
- Adding Leafpad installation
	* Please note that Leafpad is part of the Raspbian package.
	* (Only needed in situations where the Leafpad program is corrupted or missing on the system).

###########################################################################

FROM V2.0 to V2.1
- GUI improvements:
	* GUI now has a horizontal orientation whereas V2.O had a vertical orientation.
	* Buttons are now stored in 4 vertical LabelFrames, according to function.
	* Each LabelFrame has its own descriptive label.


###########################################################################
###########################################################################
###############                KNOWN ISSUES                 ###############
###########################################################################

Complexer Shellcode can't be integrated (25/11/2016)

###########################################################################