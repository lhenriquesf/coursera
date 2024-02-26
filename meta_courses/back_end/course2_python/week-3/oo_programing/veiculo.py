from abc import abstractmethod, ABC

class Veiculo(ABC):
    def basicinfo(self):
        print('É um veiculo')
        return 'Veiculo'
    
    @abstractmethod
    def chassi(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        super().__init__()
        self.rodas = 4

    def basicinfo(self):
        print("Esse é um carro")
        return 'Carro'
    
    def chassi(self):
        print('Tem 4 portas')
        return '4 portas'
    

class Moto(Veiculo):
    def __init__(self) -> None:
        super().__init__()
        self.rodas = 2

    def basicinfo(self):
        print('É uma moto')
        return 'Moto'
    
    def chassi(self):
        print('Somente duas rodas')
        return 'Mais rápido'
    

if __name__ == '__main__':
    pass