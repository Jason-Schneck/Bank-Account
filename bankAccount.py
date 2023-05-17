class BankAccount:
    def __init__(self, int_rate, balance, fname, lname):
        self.int_rate = int_rate
        self.balance = balance
        self.fname = fname
        self.lname = lname
        self.amount = 0


    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is {self.balance}")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= amount:
            print(f"Insufficient funds: Charging a $5 fee: {self.balance - 5}")
        else:
            print(f"Your withdrew {amount}")
        return self


    def display_account_info(self):
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"New Balance: {self.balance}")
        return self


    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        print(f"Your Balance with the interest rate is {self.balance}")
        return self

jason = BankAccount(4, 25, "Jason", "Schneck")
josh = BankAccount(2, 20, "Josh", "Schneck")

jason.deposit(20).deposit(30).deposit(40).withdraw(3).display_account_info().yield_interest()
print("-----")
josh.deposit(15).deposit(10).withdraw(10).withdraw(8).withdraw(4).withdraw(2).display_account_info().yield_interest()