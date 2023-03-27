MIN_NUMBER = 1
MAX_NUMBER = 100000
condition = True

while condition:
    number = int(input('Enter positive number to 100 000: '))

    if (MIN_NUMBER > number) or (MAX_NUMBER < number):
        print('Incorrect data. Try again')
    elif (number == 1):
        res = 'Not composite and not prime number'
        condition = False
    elif (MIN_NUMBER < number <= MAX_NUMBER):
        for i in range(MIN_NUMBER + 1, MAX_NUMBER + 1):
            if number % i == 0 and i != number:
                res = 'Composite number'
                condition = False
                break
            else:
                res = 'Prime number'
                condition = False

print(res)