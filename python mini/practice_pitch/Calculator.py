import random

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choose Calculation: \n"
      "Add \n"
      "Multiply \n"
      "Subtract \n"
      "Divide")

calc = input()

if calc == 'Add':
    ans = num1+num2
    print(ans)

elif calc == 'Subtract':
    ans = num1-num2
    print(ans)

elif calc == 'Multiply':
    ans = num1*num2
    print(ans)

elif calc == 'Divide':
    ans = num1/num2
    print(ans)