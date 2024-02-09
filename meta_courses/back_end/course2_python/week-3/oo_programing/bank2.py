from abc import ABC, abstractmethod

class Bank(ABC):
    def basicinfo(self):
        print('This is a generic bank')
        return "Generic bank: 0"

    @abstractmethod
    def withdraw(self):
        pass



# Class Swiss
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.balance = 1000
    
    def basicinfo(self):
        print('This is a Swiss Bank')
        return f"Your balance {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return "Insufficient funds"
        self.balance -= amount
        print(f"Withdrawn amount: {amount}")
        print(f"New Balance: {self.bal}")
        return self.bal
    

class OnlineBank(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.balance = 1500

    def basicinfo(self):
        print('This is a Online Bank')
        return f"Your balance {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return "Insufficient funds"
        self.balance -= amount
        print(f"Withdrawn amount: {amount}")
        print(f"New Balance: {self.bal}")
        return self.bal
    
    def transfer(self,amount,recipient):
        amount_withdraw = self.withdraw(amount)
        if amount_withdraw != "Insufficient funds":
            recipient.balance += amount
            print(f"Recipient's account balance: {recipient.bal}")
            return self.bal