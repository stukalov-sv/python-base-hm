import decimal

class ATM:
    # Константы:
    PRECISION = 35
    TAKE_OFF_TAX = 1.5 /100
    REFINANCE_RATE = 3.0 / 100
    LOWER_BOUND, UPPER_BOUND = 30, 600
    TOTAL_LIMIT = 5_000_000.0
    WEALTH_TAX = 10 / 100
    LCM = 50
    Q = 3

    def __init__(self, prec= 35):
        self.sum_ = 0
        self.operation_counter = 0

        self.exit_flag = False
        self.locked = False
    
    def take_off(self, money_amount: int) -> bool:
        if not self.valid(money_amount):
            print(f'Money amount must divisible by {ATM.LCM}')
            return False
        elif money_amount > self.sum_:
            print(f'Money amount too high')
            return False
        # operation successful:
        self.operation_counter += 1
        # tax calculation:
        tax = money_amount * ATM.TAKE_OFF_TAX
        if tax < ATM.LOWER_BOUND:
            tax = ATM.LOWER_BOUND
        elif tax > ATM.UPPER_BOUND:
            tax = ATM.UPPER_BOUND
        if money_amount + tax > self.sum_:
            # early exit:
            print(f'cannot process the common taxation')
            return False
        # tax for wealth:
        taxable_amount = 0
        if self.wealth:
            taxable_amount = money_amount if self.sum_ - money_amount >= ATM.TOTAL_LIMIT \
                else self.sum_ - ATM.TOTAL_LIMIT
        wealth_tax = taxable_amount * ATM.WEALTH_TAX
        # checks for possibility of tax withdrawal (validity of wealth-taxation included):
        if (amount := money_amount + tax + wealth_tax) > self.sum_:
            print(f'cannot process the wealth-taxation')
            return False
        # main action:
        self.sum_ -= amount
        print(f'{self}')
        return True

    def put(self, money_amount: int) -> bool:
        if not self.valid(money_amount):
            print(f'Money amount must divisible by {ATM.LCM}')
            return False
        
        self.operation_counter += 1
        amount = money_amount * (1 - ATM.WEALTH_TAX) if self.wealth else money_amount
        self.sum_ += amount
        if self.third_op:
            self.sum_ += money_amount * ATM.REFINANCE_RATE
        print(f'{self}')
        return True            
    @property
    def wealth(self) -> bool:
        return self.sum_ > ATM.TOTAL_LIMIT

    @property
    def third_op(self) -> bool:
        return self.operation_counter % ATM.Q == 0

    @staticmethod
    def valid(amount: int) -> bool:
        return amount % ATM.LCM == 0
    
    def __str__(self):
        return f'account money: {self.sum_}'
    
    def __repr__(self):
        return str(self)
    
    def exit(self) -> None:
        self.exit_flag = True
        print(f'Session closed, account money: {self.sum_}')

def input_valid_num(message: str) -> int:
    string = input(message)
    if string.isdigit() and (num := int(string)) > 0:
        return num
    else:
        print(f'Enter a natural number')
        input_valid_num(message)

def main():
    atm = ATM(prec=36)
    while not atm.exit_flag:
        command = input(f'Enter your request: ')
        match command:
            case 'take off':
                amount = input(f'Enter money amount to be taken off: ')
                if not atm.take_off(int(amount)):
                    print(f'Invalid operation')
            case 'put':
                amount = input_valid_num(f'Enter money amount to put: ')
                if not atm.put(int(amount)):
                    print(f'Invalid operation')
            case 'exit':
                atm.exit()
                break
            case _:
                print(f'Enter a valid request: '
                      f"'take off', 'put' or 'exit'")

main()