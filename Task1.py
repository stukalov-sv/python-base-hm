a = int(input('Enter first triangle side length (int): '))
b = int(input('Enter second triangle side length (int): '))
c = int(input('Enter third triangle side length (int): '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Equilateral triangle')
    elif a == b or a == c or b == c:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
else:
    print('Triangle does not exist')   