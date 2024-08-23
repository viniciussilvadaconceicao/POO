class Carro :
    def __init__(self, marca, modelo, cor, cambio, ano):
        self.cambio = cambio
        self.ano = ano 
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
        self.ls_running = False
        self.velocidade = float(0)

    def __str__(self):
        return f'''
    o carro é :{self.marca}
    modelo:{self.modelo}
    cor:{self.cor}
    cambio:{self.cambio}
    ano:{self.ano}
    '''

    def acelerar(self, velocidade_2):
        if self.ls_running:
            self.velocidade += velocidade_2
            print(f'velocidade é {self.velocidade} km/h')
        else:
            print(f'o carro {self.modelo} está desligado')

    def ligar(self):
        if not self.ls_running:
            self.ls_running = True
            print(f'o carro {self.marca} está ligado')

    def parar(self):
        if self.ls_running:
            self.ls_running = False
            print(f'o carro {self.modelo} está parado')
        else:
            print(f'o carro {self.modelo} está desligado')

class Moto:
    def __init__(self, marca, modelo, cor, ano, cilindada):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.cilindada = cilindada

    def __str__(self):
        return f'''
    a moto é :{self.marca}
    modelo:{self.modelo}
    cor:{self.cor}
    ano:{self.ano}
    cilindada:{self.cilindada}
    '''

