class BankAccount:
    bank_name = "KDJ Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Account Owner:{self.owner} | Balance: {self.__balance}"

    def deposit(self, amount):
        if amount > 0:
         self.__balance += amount
        print(f"{amount} deposited successfully") 

    def withdraw(self, amount):
       if amount > self.__balance:
          print("Not enough balance!")

       else:
          self.__balance -= amount
          print(f"{amount} withdrawed successfully!")

    def get_balance(self):
       return self.__balance

account1 = BankAccount("Achille", 500000)
account2 = BankAccount("GOA", 450000)
print(account1)

account1.deposit(4000)
account1.withdraw(2000)
print(account1.get_balance())
print(BankAccount.bank_name)

              