DATA_16 = '0123456789ABCDEF'


number = int(input('Enter number: '))
base = int(input('Enter base: '))
print(bin(number))
print(oct(number))
print(hex(number))

res = ''
while (number > 0):
    if base == 16:
        res = str(DATA_16[number % base]) + res
    else:
        res = str(number % base) + res
    number //= base
print(f'Your number in {base}: {res}')