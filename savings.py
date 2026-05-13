from Account import Account         
class SavingsAccount(Account):
    def __init__(self, owner, balance=0):
       super().__init__(owner, balance)
       self.withdraw_limit = 100
                    
    def withdraw(self, amount):
         if amount > self.withdraw_limit:
           print("Withdraw denied : Limit is $100")
         elif amount > self.__balance:
           print("Insufficient funds")
         else:
          self.balance -= amount
          print(f"${amount} withdraw successfully")
          
saving = SavingsAccount("Hubert", 500)
saving.withdraw(150)
