import periodictable

Atomic_No = int(input("Enter Element Atomic No: "))
element = periodictable.element[Atomic_No]
print('Atomic number: ' , element.symbol)
print('Symbol: ' , element.symbol)
print('Name: ' , element.name)
print('Atomic mass: ' , element.mass)
print('Density: ', element.density)