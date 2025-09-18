class Bankaccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited.")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn")
            print(f"new balance is {self.balance}")
    
    
account=Bankaccount("AJAY",5000)
account.deposit(1000)
account.withdraw(4000)
        
       
