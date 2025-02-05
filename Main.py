import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'Class'))

from Class.bank import Bank

#working with the banking system

hdfc=Bank()
hdfc.create_account("Ansh","Savings")
hdfc.create_account("Darshit","current")
hdfc.create_account("Ansh1","Current")

Ansh_account=hdfc.accounts[10001]               
Darshit_account=hdfc.accounts[10002]
Ansh1_account=hdfc.accounts[10003]

Ansh_account.deposit(10000)
Darshit_account.withdraw(5000)
Ansh_account.check_balance()
Darshit_account.check_balance()

hdfc.transfer_money(10001,10003,1000)
Ansh1_account.check_balance()

hdfc.create_account("Ansh2","loan")
Ansh2_account=hdfc.accounts[10004]
Ansh2_account.take_loan(10000)
Ansh2_account.check_balance()
hdfc.transfer_money(10004,10003,2000)
Ansh2_account.repay_loan(10000)
Ansh2_account.check_loan_balance()