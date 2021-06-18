#this is the python file
#pip for windows and pip3 for any linux ditro or mac
from psutil import sensors_battery#if there is an error Moduel not found then run pip/pip3 install psutil in terminal
from playsound import playsound as p#if there is an error Moduel not found then run pip/pip3 install playsound in terminal
from notify2 import init , Notification#if there is an error Moduel not found then run pip/pip3 install notify2 in terminal
init("H")
def notify(title , body , icon=""):
    Notification(title , body , icon).show()
while True:
    bettery = sensors_battery() 
    percent = int(bettery.percent)
    plugged = bettery.power_plugged
    if percent == 10:#10% battery is low you can write your percent instead of 10
        if plugged == False:
            notify("Battery is low" , "I am hungry")
            p("/home/devyansh/Documents/My work/Python/My exprement/galaxy_low_battery.mp3")#instead of /home/devyansh/Documents/My work/Python/My exprement/galaxy_low_battery.mp3 give the path of your ringtone
    elif percent == 100:#100% battery is full you can write your percent instead of 100
        if plugged == True:
            notify("Battery is full" , "I am getting fat")
            p("/home/devyansh/Documents/My work/Python/My exprement/galaxy_low_battery.mp3")#instead of /home/devyansh/Documents/My work/Python/My exprement/galaxy_low_battery.mp3 give the path of your ringtone
