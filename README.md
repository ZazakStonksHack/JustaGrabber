<h1 align="center">🎄 JustaGrabber - A discord token grabber written in python3<h1>
<h3 align="center">🎇 Made by kldiscord https://github.com/kldiscord<h3>

## ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ 🌟Star This Repository If You Liked Hazard Token Grabber V2!

---

## Installation 

#### upon running the file you will get the following sent to your webhook:
 -  Username
 -  ComputerName
 -  IP
 -  City
 -  Region
 -  Country
 -  Google Maps Location
 -  Screenshot of their pc
 -  All Their Valid Discord Tokens
 -  Password For Discord (You get Their Password if They Update it)
 -  Their Whole Credit Card (if They Put one in)
 -  All Their Chrome Passwords And Cookies
> Webhook looks like this:

<p align="left"><img src="https://i.imgur.com/4KmwB6I.png"</p>

### 📁・Setting up Hazard Token Grabber.V2
1. Start off by installing [python](https://www.python.org/) ofc
2. run the `Install_requirements.cmd` and wait for it to install the requirements
3. open main.py with any code editor of your choice and paste your webhook on line 7
4. additionally [compile](https://github.com/Rdimo/Hazard-Token-Grabber-V2#compiling-source-code) it 
5. send exe to your victims 😈

### ⚙・Compiling Source Code
Start of by opening a cmd in your directory and type:
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
