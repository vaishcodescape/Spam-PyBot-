#Spam Bot Created in Python
import pyautogui
import time

text = input("Enter the text you would like to spam: ")
n = input("Enter the number of times you would like to spam the text:")
x = int(input("Enter the number of times you would like to spam the text:"))
t = int(input("Enter the time interval between each spam in seconds:"))
time.sleep(t)

for i in range(x):
    pyautogui.typewrite(text)
    pyautogui.press("Enter")
