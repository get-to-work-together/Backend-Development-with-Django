
class BankAccount:

    def __init__(self, number, holder, saldo = 0.0):
        self.number = number
        self.holder = holder
        self.saldo = saldo

    def deposit(self, amount):
        self.saldo += amount

    def withdraw(self, amount):
        self.saldo -= amount    

    def info(self):
        print(f'Rekening {self.number} van {self.holder} heeft een saldo van {self.saldo}.')


# ------------------------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL32ABCD0456723456', 'Peter')

    acc1.info()
    acc1.deposit(1000)
    acc1.withdraw(234)
    acc1.withdraw(32)
    acc1.withdraw(92)
    acc1.info()