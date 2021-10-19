#written by Akshay patil
class Bank():
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.min_balance=min_balance
        self.balance=balance

        
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Sorry, not enough funds")
    def deposit(self,amount):
        self.balance+=amount
    def statement(self):
        print("Account balance is Rs.{}".format(self.balance))
 #   def __str__(self):
 #       return "Test account child class of parent class bank "
    

class Current_Account(Bank):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return "{} 's Current account : Balance is Rs.{} ".format(self.name,self.balance)

class Saving_Account(Bank):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{} 's Saving account : Balance is Rs.{} ".format(self.name,self.balance)
#class Test_Account(Bank):
#    def __init__(self):
 #       pass
        
    
#print("{}".format(Test_Account()))        
        
    
