from abc import ABC,abstractmethod

#SRP (Single Responsibility Principle)
'''Following SRP (Single Responsibility Principle) as there are separate classes 
   for each operations'''

#OCP (Open/Closed Principle)
'''Following OCP (Open/Closed Principle) by using an abstract class as the Bank_Account 
   class is open for extension but closed for modification, allowing new account 
   types to be added easily.'''


class Bank_Account(ABC):

    def __init__(self,name,accountnumber,balance):
        self.name=name
        self.__accountnumber=accountnumber
        self._balance=balance
    
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def check_balance(self):
        print(f"\nAccount Number: {self.__accountnumber}")
        print(f"Account Holder: {self.name}")
        print(f"Available Balance: Rs{self._balance}\n")


#LSP (Liskov Substitution Principle)      
'''LSP (Liskov Substitution Principle)
   Following LSP (Liskov Substitution Principle) as Subclasses such as Savings_Account, 
   Current_Account, and Loan_Account substitute Bank_Account without breaking 
   functionality.'''


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


#DIP (Dependency Inversion Principle)
''' Following DIP (Dependency Inversion Principle) as the Bank class depend on abstraction Bank_Account.
    Bank does not directly depend on Savings_Account, Current_Account, or Loan_Account. 
    Instead, it depends on the abstraction Bank_Account'''

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self,name,account_type):
        account_number=len(self.accounts)+10001
        if account_type.lower()=='savings':
            account=Savings_Account(name,account_number)
        elif account_type.lower()=='current':
            account=Current_Account(name,account_number)
        else:
            account=Loan_Account(name,account_number)

        self.accounts[account_number]=account
        print(f"Account Created Successfully with Account Number : {account_number}")

    def transfer_money(self,from_acc,to_acc,amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            sender=self.accounts[from_acc]
            reciever=self.accounts[to_acc]
        
            if sender._balance>amount:
                sender.withdraw(amount)
                reciever.deposit(amount)

                print(f"Rs{amount} Transferred from {from_acc} to {to_acc}")
            else:   
                print("Insufficient balance in your Account")
        else:
            print("Enter correct Account Numbers")


#ISP (Interface Segregation Principle)
'''Following ISP (Interface Segregation) as Loan functionality is separate from 
   Bank_Account so that other account types don't have to implement Loan functionality'''


class Loan():
    def __init__(self,loan_amount,loan_intrest):
        self._loan_amount=loan_amount
        self.loan_intrest=loan_intrest

    def calculate_intrest(self):
        x=self._loan_amount*(self.loan_intrest/100)
        print(f"The intrest on loan is Rs{x}")


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
        print(f"Interest: Rs{self.calculate_interest()}")