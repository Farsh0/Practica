from math import * 
x = int(input('Введите x'))
if x > 0:
    print('y = ', sin((x)**2))
else:
    print('y = ', 1 + 2 * (sin(x)**2))
