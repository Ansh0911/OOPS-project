
from bank_account import Bank_Account
from loan import Loan

class Loan_Account(Bank_Account,Loan):
    def __init__(self, name, accountnumber, balance=0.00, loan_amount=0.00, loan_intrest=10):
        Bank_Account.__init__(self,name, accountnumber, balance)
        Loan.__init__(self,loan_amount,loan_intrest)

    def take_loan(self,amount):
        self._loan_amount=self._loan_amount+amount
        self._balance=self._balance+amount
        print(f"Loan of Rs{amount} added to the balance successfully")
    
    def repay_loan(self,amount):
        if self._loan_amount>=amount:
            if self._balance>=amount:
                self._loan_amount=self._loan_amount-amount
                self._balance=self._balance-amount
                print(f"Repayment of Rs{amount} has been done for the Loan")
            else:
                print("Insufficient balance in loan account for the repayment")
        else:
            print("Repayment amount is greated than Loan amount")

    def deposit(self,amount):
        self._balance=self._balance+amount
        print(f"Rs{amount} successfully deposited to your Loan account")
    
    def withdraw(self,amount):
        if self._balance>=amount:
            self._balance=self._balance-amount
            print(f"Rs{amount} has been withdrawn from your Loan account")
        else:
            print("insufficient balance in your Loan account")

    def check_loan_balance(self):
        print(f"Loan Balance: Rs{self._loan_amount}")
        print(f"Intrest: Rs{self.calculate_intrest()}")