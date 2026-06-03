from utils import *

class Produto:
    def __init__(self):
        self.nome = input("Digite o nome do produto: ")
        self.preco = input_float("Digite o preço do produto: ")
        self.quantidade = input_int("Digite a quantidade de produtos: ")

    def vender(self):
        print("Qual vai ser a quantidade de produtos que vc quer vender?")
        qtd = int(input())

        self.quantidade = self.quantidade - qtd
        print(f"Preço a ser ganho: {qtd * self.preco}")
        print(f"Quantidade de produtos que ficaram: {self.quantidade}")

    def comprar(self):
        print("Qual vai ser a quantidade de produtos que vc quer comprar?")
        qtd = int(input())

        self.quantidade = self.quantidade + qtd
        print(f"Preço a ser pago: {qtd * self.preco}")
        print(f"Quantidade de produtos que ficaram: {self.quantidade}")
        