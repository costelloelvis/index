import random, shutil, sys, time

# set constants:
MIN_STREAM_LENGTH = 1
MAX_STREAM_LENGTH = 10
PAUSE = 0.05
STREAM_CHARS = ['0', '1']

# Density can range from 0.0 to 1.0:
DENSITY = 13.025

#Get the size of terminal window:
WIDTH = shutil.get_terminal_size()[0]

WIDTH -= 1

print('Digital Stream')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <=  DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)
                    
            if columns[i] >0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1

            else:
                print('', end='')
            print()
            sys.stdout.flush()
            time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()