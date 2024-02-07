# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
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
        self.bal = 1000 

    def basicinfo(self):
        print('This is The Swiss Bank')
        return f'Swiss Bank: {self.bal}'
    
    def withdraw(self,amount):
        if amount > self.bal:
            print("Insufficient funds")
            return "Insufficient funds"
        self.bal -= amount
        print(f"Withdrawn amount: {amount}")
        print(f"New Balance: {self.bal}")
        return self.bal


class OnlineBank(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1500

    def basicinfo(self):
        print('This is an Online Bank')
        return f'Online Bank: {self.bal}'
    
    def withdraw(self,amount):
        if amount > self.bal:
            print("Insufficient funds")
            return "Insufficient funds"
        self.bal -= amount
        print(f"Withdrawn amount: {amount}")
        print(f"New Balance: {self.bal}")
        return self.bal
    
    def transfer(self,amount,recipient):
        withdraw_amount = self.withdraw(amount)
        if withdraw_amount != "Insufficient funds":
            recipient.bal += amount
            print(f"Recipient's account balance: {recipient.bal}")
            return self.bal


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

    print()

    luiz_bank = OnlineBank()
    igor_bank = OnlineBank()

    print('Luiz Bank: ',luiz_bank.basicinfo())
    luiz_bank.transfer(5000,igor_bank)
    print()
    print('Igor Bank: ',igor_bank.basicinfo())

if __name__ == "__main__":
    main()