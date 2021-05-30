# Config 
#================================

#               X   Y Format
searchField = 0, 0 # The search Field on whatsapp
firstChildOnSearch = 0, 0 # The first contact that appears after searching
messageField = 0, 0 # The message field



# For multiple message to multiple people

peopleToMessage = {
    "8281931488": "This is a random message",
    "8921511945": "Follow @psycho_sherlock on twitter",
    "mum": "Hope this code helps you"
    # The above are examples. Add more number/name:messages like above. Dont forget to seperate them by','
}


# For same message to multiple people(I AM NOT RESPONSIBLE IF YOU SPAM ANYONE)
message = """

This is a random message. Try to follow @psycho_sherlock on twitter for more amazing tools xD.

"""

#===========================================

import pyautogui as pg
from time import sleep
from sys import exit as close
from webbrowser import open

if '0, 0' in str(firstChildOnSearch):
    print("Please read https://www.github.com/psychoSherlock/whatsAuto or else the script won't run")
    close()
else:
    pass

print('\nWaiting to load is currently 10 seconds. Change this in the script if it starts running before loading. It depends on your internet\n')
prompt = input("1) Same message to random people\n2)Different message to different people\n>>")
open('https://web.whatsapp.com')
sleep(10) # Waits for 10 seconds. Adjust this as much as you want. It depends on your internet.



if '1' in str(prompt):
    while True:
        for member in peopleToMessage:

            pg.moveTo(searchField[0], searchField[1], 0.8)
            pg.click()
            pg.write(member , interval=0.5)
            sleep(2)
            pg.moveTo(firstChildOnSearch[0], firstChildOnSearch[1] ,0.3)
            pg.click()
            sleep(2)
            pg.moveTo(messageField[0], messageField[1], 0.3)
            pg.click()
            sleep(2)
            pg.write(message , interval=0.1)
            pg.press('enter')




else:
    while True:
        for member in peopleToMessage:

            pg.moveTo(searchField[0], searchField[1], 0.8)
            pg.click()
            pg.write(member , interval=0.5)
            sleep(2)
            pg.moveTo(firstChildOnSearch[0], firstChildOnSearch[1] ,0.3)
            pg.click()
            sleep(2)
            pg.moveTo(messageField[0], messageField[1], 0.3)
            pg.click()
            sleep(2)
            pg.write(peopleToMessage.get(member), interval=0.1)
            pg.press('enter')
