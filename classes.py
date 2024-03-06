#importacao de modulos
from datetime import datetime as dt
#Classes
class Moto:

    def __init__(self,placa:str, km_atual:int, marca:str =None, intervalo_km_troca_ol_motor: int = 3000, intervalo_meses_troca_ol_motor: int = None) -> str:
        self.placa = placa
        self.km_atual = km_atual
        self.marca = marca 
        self.intervalo_km_troca_ol_motor = intervalo_km_troca_ol_motor 
        self.intervalo_meses_troca_ol_motor = intervalo_meses_troca_ol_motor 
                
    def __repr__(self) -> str:
        return f"{type(self).__name__}"
        
    def __str__(self) -> str:
        return f"{self.marca}- Veículo placa {self.placa}, Quilometragem atual: {self.km_atual} Kms"
    #Somar tempo de troca de óleo do motor do manual com a quilometragem registrada da moto
    def ProximaTrocaMotor(self):
        return self.km_atual + self.intervalo_km_troca_ol_motor
    def AtualEm(self):
        #return str(self.timestamp.date())    def __repr__(self) -> str:
        return f"{type(self).__name__}(placa= {self.placa},km atual= {self.km_atual})"

class Harley(Moto):
    def __init__(self, *args, troca_oleo_primaria, troca_oleo_embreagem):
    #def __init__(self, placa:str, km_atual:int, marca:str =None, intervalo_km_troca_ol_motor: int = 3000, intervalo_meses_troca_ol_motor: int = None, troca_oleo_primaria:int=6000, troca_oleo_embreagem:int=6000):
        super(Harley,self).__init__(self, *args, **kwargs)
        
        self.troca_oleo_primaria = troca_oleo_primaria
        self.troca_oleo_embreagem = troca_oleo_embreagem
        self.marca = "Harley Davidson"
##OBS: verificar a como a classe Harley herda os metodos da classe Moto

m1 = Moto("GHE6560", 42000, "Suzuki", 10000)   
m2 = Harley("EKB6303", 18000)    

print(m1.placa)
print(m1.km_atual)
print(m1)
m2.ProximaTrocaMotor()


m2.AtualEm()
#etiqueta de tempo
#timestamp = dt.now()