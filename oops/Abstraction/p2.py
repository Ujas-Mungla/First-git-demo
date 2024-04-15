class Account:
    def __init__(self,bal,acno) :
        self.balance=bal
        self.account_number=acno

    def debit(self,amount):
         self.balance -= amount
         print("Rs .",amount,"Was Debited")
         print("Total Balance =",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"Was Credited")
        print("Total Balance = ",self.get_balance())
    def get_balance(self):
        return self.balance


acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)

