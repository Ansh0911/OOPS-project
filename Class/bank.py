
from savings_account import Savings_Account
from current_account import Current_Account
from loan_account import Loan_Account


class Bank:                                        
    def __init__(self):
        self.accounts = {}

    def create_account(self,name,account_type):                 #Method to create account
        account_number=len(self.accounts)+10001
        if account_type.lower()=='savings':
            account=Savings_Account(name,account_number)
        elif account_type.lower()=='current':
            account=Current_Account(name,account_number)
        else:
            account=Loan_Account(name,account_number)

        self.accounts[account_number]=account
        print(f"Account Created Successfully with Account Number : {account_number}")

    def transfer_money(self,from_acc,to_acc,amount):                    #Method to transfer money
        if from_acc in self.accounts and to_acc in self.accounts:
            sender=self.accounts[from_acc]
            reciever=self.accounts[to_acc]
        
            if sender._balance>amount:
                #sender.withdraw(amount)
                #reciever.deposit(amount)
                sender._balance=sender._balance-amount
                reciever._balance=reciever._balance+amount