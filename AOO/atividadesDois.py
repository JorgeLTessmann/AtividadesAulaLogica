from utils import *
from AOO.classes.ERP import *



# Criação de pedido:
pedido = Pedido()

pedido.adicionar_produto()
pedido.adicionar_produto()
pedido.adicionar_produto()

pedido.calcular_total()

print(f"Pedido nº {pedido.numero_pedido}")
print(f"Total: R$ {pedido.calcular_total():.2f}")


# Cadastro de cliente e ordens de serviço

os1 = OrdemServico()
os1.exibir_comprovante()