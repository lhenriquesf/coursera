class Recipes():
    def __init__(self,dish,items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(f'The {self.dish} has {self.items} and takes {str(self.time)} min to prepare')



class MyFirstClass:
    #print('Who wrote this?')
    index = "Author-Book"

    def hand_list(self,philosopher,book):
        print(MyFirstClass.index)
        print(f'{philosopher} wrote the book: {book}')



class Payslips:
    def __init__(self,name,payment,amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = 'yes'


    def status(self):
        if self.payment == 'yes':
            return f'{self.name} is paid {self.amount}'
        else:
            return f'{self.name} is not paid yet'



class Computer:

    def __init__(self,cpu,ram,storage) -> None:
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def system(self):
        return f'CPU: {self.cpu}; RAM: {str(self.ram)}gb; Storage: {str(self.storage)}tb'


class Laptop(Computer):
    def __init__(self, cpu, ram, storage) -> None:
        super().__init__(cpu, ram, storage)



class Employees:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last


class Supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password


class Chefs(Employees):
    def leave_request(self,days):
        return f'May I take a leave for {str(days)} days'
    