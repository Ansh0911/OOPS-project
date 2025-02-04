from abc import ABC,abstractmethod

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