class BankAccount:
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficent balance"

    def checkbalance(self):
        return self.__balance


def main():
    b1 = BankAccount("Joshua", 1000)
    print(b1.withdraw(1700))
    b1.deposit(2000)
    print(b1.widthdraw(2000))
    print(b1.checkbalance())
    print(b1.withdraw(1000))
    print(b1.checkbalance())


    main()

    
    
