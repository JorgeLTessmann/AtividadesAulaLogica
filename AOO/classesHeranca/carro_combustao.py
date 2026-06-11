from classesHeranca.veiculo import *

class CarroCombustao(Veiculo):
    def __init__(self, modelo, marca, cor, ano, placa,
                  volume_tanque, tipo_combustivel, cambio, consumo_combustao): # especificas para carros a combustão (C.combustao)
        
        super().__init__(modelo, marca, cor, ano, placa)
        self.volume_tanque = volume_tanque
        self.nivel_tanque = 0
        self.tipo_combustivel = tipo_combustivel
        self.cambio = cambio
        self.consumo_combustao = consumo_combustao


    def __str__(self):
        msg = super().__str__() #Resume os metodos da classe pai
        msg += f"Volume de tanque: {self.volume_tanque}l\n"
        msg += f"Tipo de combustivel: {self.tipo_combustivel} \n"
        msg += f"Câmbio: {self.cambio} \n"
        msg += f"Consumo médio: {self.consumo_combustao}Km/l \n"
        return msg
    
    def abastecer(self, volume):
        if volume >= 0:
            if self.nivel_tanque + volume <= self.volume_tanque:
                self.volume_tanque += self.volume_tanque
                print("Abastecimento OK")
                print(f"Volume atual: {self.volume_tanque}")
            else:
                print("O tanque vai transbordar")
        else:
            print("O volume deve ser positivo")