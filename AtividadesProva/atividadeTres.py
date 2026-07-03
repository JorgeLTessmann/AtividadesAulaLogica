class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

        

class Pedido:
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})
        return True
    
    def calcular_total(self):
        total = 0
        for i in self.itens:
            total += i["produto"].preco * i["quantidade"]

        return total
    
class Cliente:
    def __init__(self, nome, cpf, telefone):

        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class OrdemServico:
    def __init__(self, numero_os, descricao_defeito, valor_orcamento, cliente):
        self.numero_os = numero_os
        self.descricao_defeito = descricao_defeito
        self.valor_orcamento = valor_orcamento
        self.cliente = cliente


    def exibir_comprovante(self):
        msg = f"Num Ordem de Serviço: {self.numero_os}\nDescri Completa: {self.descricao_defeito}\nValor do Orçamento: {self.valor_orcamento}\n"
        msg += f"\nDados do cliente:\nNome: {self.cliente.nome}\nCPF: {self.cliente.cpf}\nTelefone: {self.cliente.telefone}"

        return msg
    

cliente1 = Cliente("Jorge L", 1234567890, 2134567890)

p1 = Produto(1, "cadeira", 120.0)
p2 = Produto(2, "mesa", 150.0)

produtos = {p1, p2}

pedido1 = Pedido(1, cliente1)

produto = input("Informe qual produto vc deseja adicionar? ")

for p in produtos:
    if produto.strip().lower() == p.nome:
        quantidade = int(input("Informe a quantidade que vc deseja adicionar: "))
        if pedido1.adicionar_produto(p, quantidade):
            print("Produtos adicionados!")



for i in pedido1.itens:
    print(f"{i["produto"].nome}\n{i["quantidade"]}\n{pedido1.calcular_total()}")


