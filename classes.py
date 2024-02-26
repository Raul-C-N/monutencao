#importacao de modulos
from datetime import datetime as dt
#Classes
class Moto:

    def __init__(self, placa: str, km_atual: int, marca:str =None, tempo_troca_oleo_motor: int = None, timestamp = dt.now()) -> None:
        self.placa = placa
        self.km_atual = km_atual
        self.marca = marca 
        self.tempo_troca_oleo_motor = tempo_troca_oleo_motor
        self.timestamp = timestamp
    #método de apresentação
    def __str__(self) -> str:
        return f"{self.marca}- Veículo placa {self.placa}, Quilometragem atual: {self.km_atual} Kms, Tempo de troca de óleo do motor: {self.tempo_troca_oleo_motor}"
    #Somar tempo de troca de óleo do motor do manual com a quilometragem registrada da moto
    def ProximaTrocaMotor(self):
        return self.km_atual + self.tempo_troca_oleo_motor
    def AtualEm(self):
        return str(self.timestamp.date())
class Harley(Moto):
    #herda as funções da classe pai
    def __init__(self, placa: str, km_atual: int, marca: str = "Harley Davidson", tempo_troca_oleo_motor: int = None, ultima_troca_oleo_primaria: int = None, ultima_troca_oleo_embreagem: int = None) -> None:
        super().__init__(placa, km_atual, marca, tempo_troca_oleo_motor)
        if ultima_troca_oleo_primaria is None:
            ultima_troca_oleo_primaria = km_atual
        if ultima_troca_oleo_embreagem is None:
            ultima_troca_oleo_embreagem = km_atual
            
        self.ultima_troca_oleo_primaria = ultima_troca_oleo_primaria
        self.ultima_troca_oleo_embreagem = ultima_troca_oleo_embreagem
        self.marca = marca
class Suzuki(Moto):
    def __init__(self, placa: str, km_atual: int, marca: str = None, tempo_troca_oleo_motor: int = None) -> None:
        super().__init__(placa, km_atual, marca, tempo_troca_oleo_motor)
        self.marca = "Suzuki" 
#Funçôes
def TrOleo(moto):
    return str("Para a " +moto.marca+" - "+moto.placa+", a próxima troca de óleo do motor é com "+str(moto.ProximaTrocaMotor())+" Kms")


#Instancias
m1 = Moto("GHE0000", 42000)
m2 = Harley("EKB6303", 18000, tempo_troca_oleo_motor=6000)    

m4 = Suzuki("GHE000",40000,tempo_troca_oleo_motor=3000)

#testes
print(m1.placa)
print(m1.km_atual)
print(m4)
m2.ProximaTrocaMotor()


m2.AtualEm()