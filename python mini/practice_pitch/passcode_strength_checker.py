import random

c, l, s, n = 0, 0, 0, 0

passcode = input("Enter Passcode: ")
capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerletters = "abcdefghijklmnopqrstuvwxyz"
specialchars = "!@#$%^&*"
nums = "0123456789"

if (len(passcode) >= 10):
    for a in passcode:
        if (a in capletters):
            c+=1
        if (a in lowerletters):
            l+=1
        if (a in specialchars):
            s+=1
        if (a in nums):
            n+=1

if (c >= 1 and l >= 1 and s >= 1 and n >=1 
                                and c + l + s + n == (len(passcode))):
    print('Passcode Valid')

else:
    print('Passcode Invalid, Please Try Again.')