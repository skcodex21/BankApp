class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(sef, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited $ {amount}. New balance: ${self.__balance}")
        else:
          print("Your balance is less than zero")
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
          self.__balance -= amount
          print(f"withdraw ${amount}. remaining: ${self.__balance}")
        else:
         print("Invalid withdrawal amount or insufficient funds.")
    def get_balance(self):
        """Public getter for the private__balance"""
        return self.__balance
