from classesHeranca.veiculo import *

class CarroEletrico(Veiculo):
    def __init__(self, modelo, marca, cor, ano, placa, capacidade_bateria, tipo_bateria, autonomia, consumo_eletrico):
        Veiculo.__init__(self, modelo, marca, cor, ano, placa)
        self.capacidade_bateria = capacidade_bateria
        self.tipo_bateria = tipo_bateria
        self.nivel_bateria = 0
        self.autonomia = autonomia
        self.consumo_eletrico = consumo_eletrico




    def __str__(self):
        msg = super().__str__() #Resume os metodos da classe pai
        msg += f"Capacidade da bateria: {self.capacidade_bateria}; " 
        msg += f"Tipo de bateria: {self.tipo_bateria}; "
        msg += f"Autonomia: {self.autonomia}; "
        msg += f"Consumo eletrico: {self.consumo_eletrico}; "

        return msg

    def recarregar(self, carga):
        if carga >= 0:
            if self.nivel_bateria + carga <= self.capacidade_bateria:
                self.nivel_bateria += carga
                print(f"Carro recarregado com sucesso! \n Nivel: {self.nivel_bateria}")
            else:
                print("Sobrecarga")
        else:
            print("Carga deve ser positiva")
            
    def carga_rapida(self):
            carga = 50
            if self.nivel_bateria + carga <= self.carga_rapida:
                self.nivel_bateria += carga
                print("Recarga rapida realizada com sucesso")
                print(f"Nivel: {self.nivel_bateria}")
            else:
                print("Sobrecarga")