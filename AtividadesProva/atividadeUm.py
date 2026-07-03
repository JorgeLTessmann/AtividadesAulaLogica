class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

        

class Pedido:
    def __init__(self, numero_pedido):
        self.numero_pedido = numero_pedido
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})
        return True
    
    def calcular_total(self):
        total = 0
        for i in self.itens:
            total += i["produto"].preco * i["quantidade"]

        return total




produto1 = Produto(1, "carrinho", 10.0)
print("Produto 1 cadastrado")
produto2 = Produto(2, "cadeira", 200.0)
print("Produto 2 cadastrado")

catalago = [produto1, produto2]



pedido1 = Pedido(1)
print("Pedido 1 cadastrado")

produto = input("Informe qual produto vc deseja adicionar? ")

for p in catalago:
    if produto.strip().lower() == p.nome:
        quantidade = int(input("Informe a quantidade que vc deseja adicionar: "))

        if pedido1.adicionar_produto(p, quantidade):
            print("Produtos adicionados!")
        else:
            print("Não rolou")


produto = input("Informe qual produto vc deseja adicionar? ")

for p in catalago:
    if produto.strip().lower() == p.nome:
        quantidade = int(input("Informe a quantidade que vc deseja adicionar: "))

        if pedido1.adicionar_produto(p, quantidade):
            print("Produtos adicionados!")
        else:
            print("Não rolou")

print(pedido1.calcular_total())