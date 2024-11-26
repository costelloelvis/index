import csv, sys, re

# Attempt to open the periodic table CSV file
try:
    with open('periodictable.csv', encoding='utf-8') as elementsFile:
        elementsCsvReader = csv.reader(elementsFile)
        elements = list(elementsCsvReader)
except FileNotFoundError:
    print("Error: The file 'periodictable.csv' was not found.")
    sys.exit(1)  # Exit the program with a non-zero status code

# Initialize variables and constants
ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point', 'Specific heat capacity',
               'Electronegativity', 'Abundance in earth\'s crust']
LONGEST_COLUMN = max(len(column) for column in ALL_COLUMNS)
ELEMENTS = {}  # Dictionary to store element data

# Process each line in the CSV file
for line in elements:
    element = {
        'Atomic Number': line[0],
        'Symbol': line[1],
        'Element': line[2],
        'Origin of name': line[3],
        'Group': line[4],
        'Period': line[5],
        'Atomic weight': line[6] + ' u',
        'Density': line[7] + ' g/cm^3',
        'Melting point': line[8] + ' K',
        'Boiling point': line[9] + ' K',
        'Specific heat capacity': line[10] + ' J/(g*K)',
        'Electronegativity': re.sub(r'\[(I|V|X)+\]', '', line[11]),
        'Abundance in earth\'s crust': line[12] + ' mg/kg'
    }

    # Store element information in ELEMENTS dictionary using symbol and atomic number as keys
    ELEMENTS[line[1]] = element
    ELEMENTS[line[0]] = element

# Display introductory message
print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()

# Main interactive loop
while True:
    print('''            Periodic Table of Elements
            1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
         1 H                                         He
         2 Li Be                            B C N O F Ne
         3 Na Mg                         Al Si P S Cl Ar
         4 K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
         5 Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe
         6 Cs Ba La Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
         7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()  # Convert user input to title case

    if response == 'Quit':
        sys.exit()  # Exit the program if the user types 'QUIT'

    if response in ELEMENTS:
        element_data = ELEMENTS[response]
        for key in ALL_COLUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(f'{keyJustified}: {element_data[key]}')
            input('Press Enter to continue...')
    else:
        print('Invalid input. Please enter a valid symbol or atomic number.')