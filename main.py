import os
print("Sistema de uma biblioteca")
def limpa():
    os.system('cls')
class Biblioteca:
    def __init__(self):
        self.livros = []

def cadastro_de_livros():
    print("   CADRASTRO DE LIVROS    ")
    titulo=str(input("Nome do Livro: "))
    autor=str(input("Autor do Livro: "))
    ano_publicado=int(input("Ano de publicação: "))
    codigo=str(input("Código do Livro: "))
    status=bool(input("Status do Livro (Disponível/Indisponível): "))



