from classes.ContaBancaria import *

conta1 = ContaCorrente("João", saldo=1000)
conta2 = ContaPoupanca("Maria", saldo=500)

conta1.exibir_saldo()
conta1.sacar(200)
conta1.exibir_saldo()

conta2.exibir_saldo()
conta2.calcular_juros()
conta2.exibir_saldo()

conta1.transferir(300, conta2)
conta1.exibir_saldo()
conta2.exibir_saldo()