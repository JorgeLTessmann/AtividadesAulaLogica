from utils import *

class Aluno:
    def __int__(self):
        self.nome = input_nome("Digite o nome do aluno: ")
        self.nota1 = input_float("Digite a primeira nota: ")
        self.nota2 = input_float("Digite a segunda nota: ")

    def media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    def aprovado(self):
        
        if self.media >= 6:
            return f"Aprovado, a nota média  {self.media} foi maior que 6"
        else:
            return "Reprovado"  