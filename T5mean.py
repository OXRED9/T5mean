# Made by OXRED9
# Twitter: @OXRED9

import urllib.request
import time
import sys
import os

def art():
    print('''\033[31m
 /$$$$$$$$ /$$$$$$$                                             
|__  $$__/| $$____/                                             
   | $$   | $$       /$$$$$$/$$$$   /$$$$$$   /$$$$$$  /$$$$$$$ 
   | $$   | $$$$$$$ | $$_  $$_  $$ /$$__  $$ |____  $$| $$__  $$
   | $$   |_____  $$| $$ \ $$ \ $$| $$$$$$$$  /$$$$$$$| $$  \ $$
   | $$    /$$  \ $$| $$ | $$ | $$| $$_____/ /$$__  $$| $$  | $$
   | $$   |  $$$$$$/| $$ | $$ | $$|  $$$$$$$|  $$$$$$$| $$  | $$
   |__/    \______/ |__/ |__/ |__/ \_______/ \_______/|__/  |__/
                                                                
    ''')

art()

resetTheScreen = 0


# This function will print dots (.) 
# It will clear the screen when it's find a path
def looking():
    global resetTheScreen
    if resetTheScreen == 500:
        os.system("cls")
        art()
        print("Found: \n" + founds, end="")
        print("\033[31m_______________________________________________________")
        resetTheScreen = 0
    print("\033[32m", end="")
    sys.stdout.write(".")
    sys.stdout.flush()

try:
    url = input("Enter the (URL): ")
    if url[-1] != "/":
        url += "/"
except:
    exit()
print()

# Check sends requests to the server 
try: 
    checkServerStatus = urllib.request.urlopen(url, timeout=3)
except:
    print("The server seems to be down, if not, then the path is not exist")
    exit()

try:
    choice = input("If you have a specified wordlist press 1, if not press 2: ")
except:
    print()
    print("invalid input, We will use the default wordlist...")
    choice = "2"
    time.sleep(5)

print()

if choice == "1":
    fileName = input("Enter the name of the wordlist: ")    
elif choice == "2":
    fileName = "guss2.txt"

print()

# Will throw an exception if the (fileName) is not found
try:
    openFile = open(fileName, "r")
except:
    print("File (wordlist) not found...")
    print("Make sure that the file (wordlist) is in the same folder of the tool, or check the path you have entered and make sure it's correct")
    print()
    print("Hint: don't forget to write the file's extension ^_^")
    exit()

if checkServerStatus.getcode() == 200:
    print("URL: " + url + "\033[32m "+ "(" + str(checkServerStatus.getcode()) + ")")
#     time.sleep(1.5)
else:
    print("Page not found 404")
    exit()

allFounds = ""
founds = ""
counter = 0

for x in openFile:
    try:
        connectToUrl = urllib.request.urlopen(url + x)
        if connectToUrl.getcode() == 200:
            os.system("cls")
            
            colorsUrl = "\033[32m" + url
            colorsPathsFound = "\033[31m" + x
            
            founds += "\033[0m" + colorsUrl + colorsPathsFound.strip("\n") + "\033[34m | status: " + str(connectToUrl.getcode()) + "\n"
            art()
            print("Found: \n" + founds, end="")
            print("\033[31m_______________________________________________________")
            # To recognize founds path
            time.sleep(2)
            counter += 1
    except:
        looking()
        resetTheScreen += 1
        continue
    
if counter != 0:
    print()
    print("\033[32mNumbers of directories found: " + "\033[31m" + str(counter))
    print()
else:
    print("We did not find anything in: " + url)

openFile.close()
