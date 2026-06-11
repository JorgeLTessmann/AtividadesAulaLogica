class Veiculo:
    def __init__(self, modelo, marca, cor, ano, placa):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.placa = placa

    def __str__(self):
        msg = f"Modelo: {self.modelo} \n"
        msg += f"Marca: {self.marca} \n"
        msg += f"Cor: {self.cor} \n"
        msg += f"Ano: {self.ano} \n"
        msg += f"Placa: {self.placa}"

        return msg

