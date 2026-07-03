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
    
cliente1 = Cliente("jorge", 123456789, 123456789)

ordem = OrdemServico(1, "BlaBlaBlaBla", 150.0, cliente1)

print(ordem.exibir_comprovante())
