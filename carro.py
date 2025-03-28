
class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.velocidade= 0 #atributo privado

    def acelerar (self, incremento):
        self.velocidade+=incremento
        print(f"{self.modelo}acelerou para{self.velocidade}km/h")

carro1 = veiculo("Toyota", "Corolla", 2022)

carro1.acelerar(30)

print("velocidade atual: ", carro1.velocidade())