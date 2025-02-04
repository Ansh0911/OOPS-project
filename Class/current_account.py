
from bank_account import Bank_Account

class Current_Account(Bank_Account):
    def __init__(self, name, accountnumber, balance=0.00, overdraft_limit=50000):
        super().__init__(name, accountnumber, balance)
        self.overdraft_limit=overdraft_limit

    def deposit(self, amount):
        self._balance=self._balance+amount
        print(f"Rs{amount} successfully deposited to your current account")

    def withdraw(self,amount):
        if self._balance+self.overdraft_limit>=amount:
            self._balance=self._balance-amount
            print(f"Rs{amount} has been withdrawn from your current account")
        else:
            print("insufficient balance in your current account")