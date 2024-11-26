import random

temperature = 0

if temperature > 35:
    x = ("Drink plenty of water & wear lightly")
    print(x)

elif temperature > 25:
    x = ("It's a bit warm")
    print(x)

elif temperature > 15:
    x = ("Its a bit chilly, wear warmly")
    print(x)

elif temperature > 5:
    x = ("It's cold , dress heavily")
    print(x)

else:
    print("It's very, very cold")