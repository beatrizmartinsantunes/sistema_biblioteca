import csv
import os

def limpa():
    os.system('cls')
   
def cabecalho():
    print("Programa feito por Beatriz Martins")
   
def carregar_dados():
    
    with open("livros.csv", "r", encoding="utf-8") as leitor_de_arquivo:
        leitor = csv.reader(leitor_de_arquivo)
        livros = []
        for dados in leitor:
        
                livro = {
                    "titulo": dados[0],
                    "autor": dados[1],
                    "ano": int(dados[2]),
                    "isbn": dados[3],
                    "status": dados[4],
                }
                livros.append(livro)
        return livros
    
def salvar_dados(livros):
    with open("livros.csv", "w", encoding="utf-8", newline="") as escritor_de_arquivo:
        escritor = csv.writer(escritor_de_arquivo)
        for livro in livros:
            linha = [
                livro["titulo"],
                livro["autor"],
                livro["ano"],
                livro["isbn"],
                livro["status"],
            ]
            escritor.writerow(linha)

def cadastrar_livro(livros):
    print("\nCADASTRO DE LIVRO:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de Publicação: ")
    isbn = input("Código/ISBN: ")

    for livro in livros:
        if livro["isbn"] == isbn:
            print("\nJá existe um livro com este ISBN!")
            return livros

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "isbn": isbn,
        "status": "disponível",
    }

    livros.append(novo_livro)
    salvar_dados(livros)
    print(f"\nLivro '{titulo}' cadastrado com sucesso!!!")
    return livros

def emprestar_livro(livros):
    print("\nREGISTRAR EMPRÉSTIMO")
    isbn_busca = input("Digite o ISBN do livro: ")

    for livro in livros:
        if livro["isbn"] == isbn_busca:
            if livro["status"] == "emprestado":
                print("\nEste livro já está emprestado!")
                return livros
            
            livro["status"] = "emprestado"
            salvar_dados(livros)
            print("\nEmpréstimo realizado com sucesso!")
            return livros

    print("\nLivro não encontrado.")
    return livros

def devolver_livro(livros):
    print("\nREGISTRAR DEVOLUÇÃO")
    isbn_busca = input("Digite o ISBN do livro: ")

    for livro in livros:
        if livro["isbn"] == isbn_busca:
            if livro["status"] == "disponível":
                print("\nEste livro já está disponível!")
                return livros
            
            livro["status"] = "disponível"
            salvar_dados(livros)
            print("\nDevolução realizada com sucesso!")
            return livros

    print("\nLivro não encontrado.")
    return livros
 
def remover_livro(livros):

    print("\nREMOVER LIVRO DO ESTOQUE")
    isbn_busca = input("Digite o ISBN do livro que deseja remover: ")
 
    for i in range(len(livros)):
        if livros[i]["isbn"] == isbn_busca:
            livro_removido = livros.pop(i)
            salvar_dados(livros)
            print(f"\nO livro foi removido com sucesso!")
            return livros
 
    print("\nLivro não encontrado")
    return livros
def organizar_e_listar(livros):
 
    print("\nComo deseja organizar a lista?\n")
    print("1. Por Título (Ordem Alfabética)")
    print("2. Por Autor")
    print("3. Por Ano de Publicação")
    print("4. Ordem de cadastro")
    opcao_ordem = input("Escolha uma opção (1-4): ")
 
    if opcao_ordem == "1":
        livros.sort(key=lambda x: x["titulo"])
        print("\nLIVROS ORDENADOS POR TÍTULO:")
    elif opcao_ordem == "2":
        livros.sort(key=lambda x: x["autor"])
        print("\nLIVROS ORDENADOS POR AUTOR:")
    elif opcao_ordem == "3":
        livros.sort(key=lambda x: x["ano"])
        print("\nLIVROS ORDENADOS POR ANO:")
    else:
        print("\nTODOS OS LIVROS (ORDEM DE CADASTRO):")
 
    for livro in livros:
        print(f"[{livro['status'].upper()}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")

def buscar_livros(livros):
    print("\nBUSCAR LIVROS:")
    busca = input("Digite o título ou autor: ")
 
    
    for livro in livros:
        if busca in livro["titulo"] or busca in livro["autor"]:
            print(
                f"[{livro['status'].upper()}] {livro['titulo']} por {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}") 

    print("Nenhum livro encontrado com esse termo.")

def menu():
    acervo = carregar_dados()

    while True:


        print("\nMENU PRINCIPAL DA BIBLIOTECA:\n")
        print("1. Cadastrar Livro")
        print("2. Registrar Empréstimo")
        print("3. Registrar Devolução")
        print("4. Listar Livros (Organizar)")
        print("5. Buscar Livro")
        print("6. Remover Livro do Estoque")
        print("7. Sair")
    
        opcao = input("\nEscolha uma opção: ")
    
        if opcao == "1":
            acervo = cadastrar_livro(acervo)
        elif opcao == "2":
            acervo = emprestar_livro(acervo)
        elif opcao == "3":
            acervo = devolver_livro(acervo)
        elif opcao == "4":
            organizar_e_listar(acervo)
        elif opcao == "5":
            buscar_livros(acervo)
        elif opcao == "6":
            acervo = remover_livro(acervo)
        elif opcao == "7":
            print("\nTCHAU!!")
            break
        else:
            print("Opção inválida")

menu()