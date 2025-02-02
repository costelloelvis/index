import random, sys, time

PAUSE = 0.15 
ROWS = [
    '     ##',   # Index 0 has no {}
    '   #{}-{}#',
    '  #{}---{}#',
    ' #{}-----{}#',
    '#{}------{}#',
    '#{}------{}#',
    ' #{}-----{}#',
    '  #{}---{}#',
    '  #{}-{}#',
    '    ## ',     # Index 9 has no {}
    '  #{}-{}#',
    ' #{}---{}#',
    ' #{}-----{}#',
    '#{}------{}#',
    '#{}------{}#',
    ' #{}-----{}#',
    ' #{}---{}#',
    '  #{}-{}#'
]

print('DNA Animation')
print('Press Ctrl-C to quit...')
time.sleep(2)

rowIndex = 0

try:
    while True:  # Main program loop
        # Increment rowIndex to draw next row
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        
        # Row indexes 0 and 9 don't have nucleotides
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
        
        # Randomly select nucleotides
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'
        
        # Print the row with nucleotides
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)  # Add a slight pause

except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program
