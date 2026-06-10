from AOO.classes.Pessoa import *
from AOO.classes.ContaBancaria import *
from AOO.classes.Produto import *
from AOO.classes.aluno import *

from utils import *


# pessoa = Pessoa()

# pessoa.apresentar_dados()

# print(pessoa.nome)


conta = ContaBancaria()



print("Digite o valor que vc quer depositar: ")
try:
    valorA = float(input("Quanto? \n"))
    conta.depositar(valorA)
except Exception as e:
    print("Deve ser um numero")
    print(f"error {e}")

print("Digite o valor que vc quer sacar: ")
try:
    valorA = float(input("Quanto? \n"))
    conta.sacar(valorA)
except Exception as e:
    print("Deve ser um numero")
    print(f"error {e}")

conta.exibir_extrato()


produto = Produto()

produto.comprar()
produto.vender()

aluno = Aluno()

aluno.media()
aluno.aprovado()

