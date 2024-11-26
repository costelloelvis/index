import os

from random import randint

passcode = input("Key-in Your Passcode: ")

keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pwg = ''
while(pwg!=passcode):
    pwg=""
    for i in range(len(passcode)):
        guessPass = keys[randint(0,4)]
        pwg = str(guessPass)+str(pwg)
        print(pwg)
        print("attacking......, please wait")
        os.system("cls")

print(f"The passcode is: {pwg}")