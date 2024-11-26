import random

print('Your passcode: ')

chars = 'qwertyuiopasdfghjklzxcvnm1234567890'

passcode = ''
for a in range(16):
    passcode += random.choice(chars)

print(passcode)