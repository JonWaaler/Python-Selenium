# Python-Selenium
With this repository I will be testing out various functionalities in 
python such as web manipulation and executable programs. These functionalities
will help create the auto-play application that has been missing from all these
anime websites.


## Current Challenges
Before setting up this repository I quickly made some selenium test code that 
would open up a popular anime website [AnimeDao](http://animedao.to) unfortunatly
it's bot protection would'nt let me in so I will have to attempt this application
using other anime websites.

## Basic Selenium Code - Open a Webpage
```
from selenium import webdriver
PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www12.9anime.to/home")
```
All this code does is open up the listed URL.

## Python Script -> Application
### PyInstaller
1. use: `pip install pyinstaller` to install the library.
2. locate the location to your 'python.py' file through Command Prompt
3. use `pyinstaller --onefile python.ph` in Command Prompt

This will create 3 folders in that location: build, dist and NameOfPythonScript.py. 
The file called `dist` will hold the single '.exe' file that you can now use like
an application.

### PEX
Also noted that [PEX](https://github.com/pantsbuild/pex#pex), mentioned in
[Overview of Packaging for Python](https://packaging.python.org/overview/)
also produces an executable file, though I believe it relies on python being
installed.

## Installers
For distributing python programming it's also nice to use an installer as it will compress the
files being distributed and allow the user to more easily set-up the application. Currently,
I'm looking into [Inno](https://jrsoftware.org/isinfo.php)


# About this Application
* Userbase: People who watch anime on their computer and want an easier user experience
* This software will be installed by people who may know nothing about coding
* This software will run on desktops (windows first because it'll be easy to make MVP)
* Installation needs to be as easy as **1-click** and the .exe as **2-clicks**
