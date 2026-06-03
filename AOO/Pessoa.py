from utils import *

class Pessoa:
    def __init__(self):
        self.nome = input("Digite o nome da pessoa: ")
        self.idade = input_idade("Digite a idade: ", 0, 150)
        self.valor = input_float("Digite a altura: ")

    def apresentar_dados(self):
        print(f"nome: {self.nome}, idade: {self.idade}, altura: {self.valor}")

