# Whatsapp automated timer message
# Once login the program will run as per your data entered
# Note: User must have active internet connection, and the user is requested to not to "close the window"

import pywhatkit as kit
import webbrowser
from datetime import datetime
import time
                            # ASCII 
print('''
ooooooooooooooooooooooooo
oooooooooo+++++oooooooooo
oooooo+:-..----..:+oooooo
ooooo:`:++oooooo+:`-ooooo
oooo-`+o-`-ooooooo+`-oooo
ooo+ :oo- .oooooooo: +ooo
ooo+ :ooo:`-/+::+oo: +ooo
oooo-`+ooo+:-.``-o+`-oooo
oooo/ /++ooooo+++-`:ooooo
oooo``.--..---..-:+oooooo
oooo+ooooo+++++oooooooooo
ooooooooooooooooooooooooo
''')
print("________________________________")
print("\r")
print("* Welcome to Whatsapp automation")
print("* uses 24 hours clock format")
print("* Enter mobile number without +91")

clock = datetime.now()
current_time = clock.strftime("%H:%M:%S")
print("* Current time:", current_time)
print("________________________________")
print("\r")

try:
    no = input("Mobile Number to send message:- ")      # variable to store user mobile number input 
    num = "+91" + no
    print("________________________________")
    print("\r")
    msg = input("Enter your message:- ")
    print("________________________________")
    print("\r")
    h = int(input("Enter specific time in hour hand:- "))   # hour in time ex: 15
    s = int(input("Enter specific time in mins :- "))       # mins in time ex: 25
    print("________________________________")
    print("\r")
    login = input("Press Enter to go to login.")
    webbrowser.open("https://web.whatsapp.com/")        # Redirecting to Whatsapp Web
    print("\r")

    # Allowing some time for the user to scan the QR code and log in...
    time.sleep(15)

    kit.sendwhatmsg(num, msg, h, s)
except Exception as e:
    print("________________________________")
    print("\r")
    print(f"Technical error ! ")
    print("________________________________")
    print("\r")
    input("Press Enter to exit...")
    print("\r")
    print("________________________________")

# contact user : securezone@duck.com
# Please feel free to contact me for any further changes or DM for collab..
# Thank you !
