from classesHeranca.veiculo import *  
from classesHeranca.carro_combustao import *
from classesHeranca.carro_eletrico import *
from classesHeranca.carro_hibrido import *

moto = Veiculo(
    marca = "Yamaha",
    modelo = "MT303",
    cor = "Azul",
    ano = 2020,
    placa = "abc20245"
)
                
voyage = CarroCombustao(
    marca = "Volkswagen",
    modelo = "Novo Voyage",
    ano = 2018,
    cor = "Vermelho",
    placa = "AAA-1234",
    volume_tanque = 55, # apenas do C.Combustao
    tipo_combustivel = "Flex",
    cambio = "Manual",
    consumo_combustao = 10
)

byd = CarroEletrico(
    modelo = "Dolphin",
    marca = "BYD",
    ano = 2025,
    cor = "Preto",
    placa = "AAA-4321",
    capacidade_bateria = 100, 
    tipo_bateria = "LFP",
    autonomia = 348,
    consumo_eletrico = 12
)

print(moto)
print(voyage)
print(byd)
voyage.abastecer(10)
byd.recarregar(12)
