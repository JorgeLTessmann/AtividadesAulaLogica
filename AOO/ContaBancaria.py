from utils import *

class ContaBancaria:
    def __init__(self):
        self.titular = input("Digite o nome da pessoa: ")
        self.saldo = input_float("Digite o valor de saldo inicial: ")

    def depositar(self, valor):

        self.saldo = self.saldo + valor
        print(f"Novo valor: {self.saldo}")

    def sacar(self, valorA):
        

        if self.saldo <= 0.0:
            print("Impossivel reitar valor, a conta está zerada")
        else:
            self.saldo = self.saldo - valorA
            print(f"Novo valor: {self.saldo}")