import math

r = 10.9876    # radius
l = 12.876    # length
w = 9.876     # width
h = 15.945    # height

print("Choose operation: \n"
      "circle \n"
      "rectangle \n"
      "square \n"
      "cube \n"
      "cuboid \n"
      "open cylinder \n"
      "closed cylinder")

calc = input()

if calc == 'circle':
    ans = math.pi*(r**2)
    print(ans)

elif calc == 'rectangle':
    ans = l*w
    print(ans)

elif calc == 'square':
    ans = l*l
    print(ans)

elif calc == 'cuboid':
    ans = '2(l*l)' + '2(l*w)' + '2(l*h)'
    print(ans)

elif calc == 'cube':
    ans = 6(l*l)
    print(ans)

elif calc == 'open cylinder':
    ans = (2*math.pi * r**2 ) + math.pi*(2*r*h)
    print(ans)

elif calc == 'closed cylinder':
    ans = (math.pi * r**2 ) + math.pi*(2*r*h)
    print(ans)