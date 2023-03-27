from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 1000
ATTEMPTS = 10

hidden = randint(MIN_NUMBER, MAX_NUMBER)

print(f'Guess number from {MIN_NUMBER} to {MAX_NUMBER} for {ATTEMPTS } attempts')

for i in range(ATTEMPTS):
    number = int(input(f'Attempts amount: {ATTEMPTS - i}. Enter your number: '))

    if number == hidden:
        print('Got it! Congratulation!')
        break
    elif hidden > number:
        whisper = 'Number is higher'
    else:
        whisper = 'Number is lower'

    print(whisper)
else:
    print('Sorry. Unfortunately, attempts is over.')
