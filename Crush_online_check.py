import pyautogui
import subprocess
import os
import time
first_time=0
def Send_Text_SMS():
    from twilio.rest import TwilioRestClient
    from credentialstwilio import account_sid, auth_token, my_cell, my_twilio

    # Find these values at https://twilio.com/user/account
    client = TwilioRestClient(account_sid, auth_token)

    my_msg = "Dinesh is Online Now."

    message = client.messages.create(to=my_cell, from_=my_twilio,
                                         body=my_msg)

def check_status():
    #locate the online tag
    global first_time
    location=pyautogui.locateOnScreen('find.png',grayscale=True)
    if location :
        print("Online")
        if first_time==0:
            first_time=1
            Send_Text_SMS()
    else:
        first_time=0


#start bluestack
os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\BlueStacks.lnk')
time.sleep(20)

#locate whatsapp icon on screen
location=pyautogui.locateOnScreen('whatsapp_icon.png',grayscale=True)
pyautogui.click(x=location[0]+15,y=location[1]+15)
time.sleep(5)

#locate message icon on whatsapp
location=pyautogui.locateOnScreen('message.png',grayscale=True)
pyautogui.click(x=location[0]+30,y=location[1]+30)
time.sleep(2)

#locate search icon
location=pyautogui.locateOnScreen('search_icon.png',grayscale=True)
pyautogui.click(x=location[0]+20,y=location[1]+20)
time.sleep(2)

#type the name of person you want to search
pyautogui.typewrite('Dinesh Choudhary',interval=0.25)

#click the first search next to create group
pyautogui.click(x=location[0]-500,y=location[1]+100)
time.sleep(1)

#check status every 10 seconds
while True:
    check_status()
    time.sleep(10)
