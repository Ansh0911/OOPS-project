from bank_account import Bank_Account


class Savings_Account(Bank_Account):
    def __init__(self, name, accountnumber, balance=0.00 , intrest_rate=3 ):
        super().__init__(name, accountnumber, balance)
        self.intrest_rate=intrest_rate

    def deposit(self,amount):
        self._balance=self._balance+amount
        print(f"Rs{amount} successfully deposited to your savings account")
    
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance=self._balance-amount
            print(f"Rs{amount} has been withdrawn from your savings account")
        else:
            print("insufficient balance in your savings account")