from utils import *

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} realizada com sucesso para {conta_destino.titular}.")
        else:
            print("Saldo insuficiente ou valor inválido.")  
    
    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa_saque=5):
        super().__init__(titular, saldo)
        self.taxa_saque = taxa_saque

    def sacar(self, valor):
        valor_total = valor + self.taxa_saque
        if valor_total <= self.saldo:
            self.saldo -= valor_total
            print(f"Saque de R${valor:.2f} realizado com sucesso! Taxa de saque: R${self.taxa_saque:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque com a taxa.")   

    def cobrar_taxa(self):

        if self.saldo > 0:
            self.saldo - (self.saldo * 0.30)
        else:
            print("Impossivel cobrar taxa")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa_juros=0.01):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}")
    

class contaSalario(ContaBancaria):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)

    def sacar(self, valor):
        return super().sacar(valor)
    
    def depositar(self, valor):
        return super().depositar(valor)