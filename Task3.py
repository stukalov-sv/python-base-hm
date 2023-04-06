import sys

TAKE_OFF_TAX = 1.5 /100
REFINANCE_RATE = 3.0 / 100
LOWER_BOUND, UPPER_BOUND = 30, 600
TOTAL_LIMIT = 5_000_000.0
WEALTH_TAX = 10 / 100
LCM = 50
Q = 3

cash = 0
operation_count = 0

def operation_count_check() -> bool:
    global cash
    global operation_count

    if operation_count == Q:
        operation_count = 0
        return True
    else:
        operation_count += 1
        return False


def balance_limit() -> bool:
    global cash

    if cash > TOTAL_LIMIT:
        return True
    return False


def balance_show() -> None:
    global cash
    print(f'Balance: {cash}')


def money_put() -> None:
    global cash

    balance_show()
    limit = balance_limit()
    operation_check = operation_count_check()

    while True:
        value = int(input(f'Enter money amount to put: '))
        if value % LCM != 0:
            print(f'Incorrect sum. Money amount must divisible by {LCM}')
            break
        else:
            if operation_check and limit:
                print(f'Operation and balance limit. {REFINANCE_RATE + WEALTH_TAX}% from operation will be kept')
                cash = cash + value * (1 - REFINANCE_RATE - WEALTH_TAX)
            elif operation_check and not limit:
                print(f'Operation limit. {REFINANCE_RATE}% from operation will be kept')
                cash = cash + value * (1 - REFINANCE_RATE)
            elif not operation_check and limit:
                print(f'Balance limit. {WEALTH_TAX}% from operation will be kept')
                cash = cash + value * (1 - WEALTH_TAX)
            else:
                cash = cash + value
            balance_show()
            break


def money_get() -> None:
    global cash

    balance_show()
    limit = balance_limit()
    operation_check = operation_count_check()

    while True:
        print(f'All take off operations kept {TAKE_OFF_TAX}%')
        value = int(input(f'Enter money amount to be taken off: '))

        commission = value * TAKE_OFF_TAX
        if commission < LOWER_BOUND:
            commission = LOWER_BOUND
        elif commission > UPPER_BOUND:
            commission = UPPER_BOUND

        if value % LCM != 0:
            print(f'Incorrect sum. Money amount must divisible by {LCM}')
            break
        else:
            if cash < value + commission:
                print(f'Not enough money. Enter amount lower than {cash + commission}.\n')
                break
            else:
                if operation_check and limit:
                    print(f'Operation and balance limit. {REFINANCE_RATE + WEALTH_TAX}% from operation will be kept')
                    cash = cash - commission - value * (1 + REFINANCE_RATE + WEALTH_TAX)
                elif operation_check and not limit:
                    print(f'Operation limit. {REFINANCE_RATE}% from operation will be kept')
                    cash = cash - commission - value * (1 + REFINANCE_RATE)
                elif not operation_check and limit:
                    print(f'Balance limit. {WEALTH_TAX}% from operation will be kept')
                    cash = cash - commission - value * (1 + WEALTH_TAX)
                else:
                    cash = cash - value - commission
                balance_show()  
                break


def exit_program() -> None:
    balance_show()
    print(f'Good bye')
    sys.exit()

def main():
    print(f"Possible ATM request: 'take off', 'put', 'balance' or 'exit'")
    while True:
        command = input(f'Enter your request: ')
        match command:
            case 'take off':
                money_get()
            case 'put':
                money_put()
            case 'balance':
                balance_show()
            case 'exit':
                exit_program()
                break
            case _:
                print(f'Enter a valid request: '
                      f"'take off', 'put', 'balance' or 'exit'")

main()