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
1. use: `pip install pyinstaller` to install the library.
2. locate the location to your 'python.py' file through Command Prompt
3. use `pyinstaller --onefile python.ph` in Command Prompt

This will create 3 folders in that location: build, dist and NameOfPythonScript.py. 
The file call `dist` will hold the single .exe file that you can now use like
an application.