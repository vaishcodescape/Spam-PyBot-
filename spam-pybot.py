#Spam Bot Created in Python

import pyautogui
import time

text = input("Enter the text you would like to spam: ")
num = int(input("Enter the number of times you would like to spam the text:"))
t = int(input("Enter the time interval between each spam in seconds:"))
time.sleep(time)

for i in range(num):
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
