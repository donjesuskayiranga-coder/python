#encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private can't access directly

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited :{amount}. New balance:{self.__balance} 👌")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance!")        
        else:
            self.__balance -= amount
            print(f"withdraw: {amount}. New balance: {self.__balance} 👌")   

    def get_balance(self):
        return self.__balance

account = BankAccount("KAYIRANGA", 500000)
account.deposit(1000000)
account.withdraw(500000)
print(f"your new balance: {account.get_balance()}")
print(account.__balance) #error can't get private data directly




