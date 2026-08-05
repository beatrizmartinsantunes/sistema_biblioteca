import os
print("Sistema de uma biblioteca")
def limpa():
    os.system('cls')

import csv
'''with open('livro.csv','w',encoding='utf-8') as estoque_de_livros:
    escritor = csv.writer(estoque_de_livros)
    escritor.writerow(['nome','autor','ano_publicado','codigo','status'])
estrutura = ['nome','autor','ano_publicado','codigo','status']'''

def cadastro_produto(nome,autor,ano_publicado,codigo,status):
    with open('livro.csv','a',newline='') as estoque:
        produto = {'nome':nome,'autor':autor,'ano_publicado':ano_publicado,'codigo':codigo,'status':status}
        escritor = csv.DictWriter(estoque,fieldnames=estrutura)
        escritor.writerow(produto)

cadastro_produto('O Senhor dos Anéis','J.R.R. Tolkien',1954,'001','Disponível')

def cadastro_de_livros():
    print("   CADRASTRO DE LIVROS    ")
    titulo=str(input("Nome do Livro: "))
    autor=str(input("Autor do Livro: "))
    ano_publicado=int(input("Ano de publicação: "))
    codigo=str(input("Código do Livro: "))
    status=bool(input("Status do Livro (Disponível/Indisponível): "))



