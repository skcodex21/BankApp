from Account import Account

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
        def withdraw(self, amount):
            available_funds = self.get_balance() + sel.overdraft_limit
            if 0 < amount <= available_funds:
                print(f"Withdrawal of ${amount} approved (using overdraft if necessary).")
            else:
                print("withdrawal deniel : Exceed overdraft limit.")
                print("\n--- Current Account ---")
                
current = CurrentAccount("Bob", 100)
current.withdraw(400)
