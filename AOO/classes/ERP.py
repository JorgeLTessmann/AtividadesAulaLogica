from utils import *

class Produto:
    def __init__(self):
        self.codigo = input_int("Digite o codigo do produto: ")
        self.nome = input("Digite o nome do produto: ")
        self.preco = input_float("Digite o preço do produto: ")


class Pedido: 
    contador = 0
    def __init__(self):
        Pedido.contador += 1
        self.numero_pedido = Pedido.contador
        self.itens = []

    def adicionar_produto(self):
        produtos = Produto()
        quantidade = input_float("Qual a quantidade desse produto que vc quer?")

        self.itens.append((produtos, quantidade))

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        print(total)

class Cliente:
    def __init__(self):
        self.nome = input("Digite qual o seu nome: ")
        self.cpf = input_int("Digite o seu cpf: ")
        self.telefone = input_int("Digite o seu telefone: ")

class OrdemServico:
    contador = 0
    def __init__(self):
        OrdemServico.contador += 1
        self.numero_os = OrdemServico.contador
        self.descricao_defeito = input("Digite a descrição do problema: \n")
        self.valor_orcamento =input_float("Digite o valor do orçamento: ")
        self.cliente = Cliente()

    def exibir_comprovante(self):
        print("Dados de Serviço:")
        print(f"Numero do serviço: {self.numero_os} \n Descrição do defeito: {self.descricao_defeito} \n Valor do orçamento: {self.valor_orcamento}")
        print("Dados do cliente: ")
        print(f"Nome do cliente: {self.cliente.nome} \n Cpf do cliente: {self.cliente.cpf} \n Telefone do cliente: {self.cliente.telefone}")