class Loan():
    def __init__(self,loan_amount,loan_intrest):
        self._loan_amount=loan_amount
        self.loan_intrest=loan_intrest

    def calculate_intrest(self):
        x=self._loan_amount*(self.loan_intrest/100)
        return x