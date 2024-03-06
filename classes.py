#importacao de modulos

#Classes
class Moto:

    def __init__(self, placa:str, km_atual:int, marca:str=None):
        self.placa = placa
        self.km_atual = km_atual
        self.marca = marca 
        self.marca = marca 
        self.marca = marca 
        self.marca = marca 
        
    def __str__(self) -> str:
        return f"{self.marca}- Veículo placa {self.placa}, Quilometragem atual: {self.km_atual} Kms"
    def __repr__(self) -> str:
        return f"{type(self).__name__}(placa= {self.placa},km atual= {self.km_atual})"

class Harley(Moto):
    def __init__(self, placa, km_atual, troca_oleo_primaria, troca_oleo_embreagem):
        super().__init__(placa, km_atual)
        
        self.troca_oleo_primaria = troca_oleo_primaria
        self.troca_oleo_embreagem = troca_oleo_embreagem
        self.marca = "Harley Davidson"


m1 = Moto("GHE6560", 42000,"Suzuki")
m2 = Harley("EKB6303", 18000, 6000, 6000)    

print(m1.placa)
print(m1.km_atual)
#funcoes
