from classesHeranca.carro_combustao import *
from classesHeranca.carro_eletrico import *

class CarroHibrido(CarroCombustao, CarroEletrico):
    def __init__(self, modelo, marca, cor, ano, placa, volume_tanque, tipo_combustivel, cambio, consumo_combustao, capacidade_bateria, tipo_bateria, autonomia, consumo_eletrico):
        CarroCombustao.__init__(self, volume_tanque, tipo_combustivel, cambio, consumo_combustao)
        CarroEletrico.__init__(self, capacidade_bateria, tipo_bateria, autonomia, consumo_eletrico)

