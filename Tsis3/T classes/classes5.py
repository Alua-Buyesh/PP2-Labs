class Account():
    def __init__(self,owner,balance =0 ):
        self.owner = owner
        self.balance = balance

    def deposit(self,a):
        self.balance+=a
        print(f"New balance: {self.balance}")
    
    def withdraw(self,subt):
        if subt<=self.balance:
            self.balance-=subt
            print(f"New balance: {self.balance}")
        else:
            print("Balance too low")
accaunt=Account(owner="Alua",balance =22000 )

accaunt.withdraw(500)
accaunt.withdraw(500000)

accaunt.deposit(1000)
accaunt.deposit(300)