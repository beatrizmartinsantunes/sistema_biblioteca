import csv
import os # Necessário para a função de limpar o terminal

def limpa(): # Limpa o terminal
    os.system('cls')
   
def cabecalho(): 
    print("Programa feito por Beatriz Martins")
   
def carregar_dados(): # ele o que está no csv e coloca na lista
    
    with open("livros.csv", "r", encoding="utf-8") as leitor_de_arquivo: # "r" significa que não ira modificar nada do livros.csv
        leitor = csv.reader(leitor_de_arquivo)
        livros = [] # Livros é onde fica todos os livros na lista que é apagada quando o programa é finalizado
        for dados in leitor: # os dados são as informacções de cada livro
        
                livro = { # Livro é cada livro que fica em livros e tem dados
                    "titulo": dados[0],
                    "autor": dados[1],
                    "ano": int(dados[2]),
                    "isbn": dados[3],
                    "status": dados[4],
                }
                livros.append(livro)# Vai anexar o livro na lista livros
        return livros # encerra e devolve livros para fora dessa função
    
def salvar_dados(livros): #vai passar a lista livros para livros.csv
    with open("livros.csv", "w", encoding="utf-8", newline="") as escritor_de_arquivo:# "w" escreve o que quero mas apaga o resto
        escritor = csv.writer(escritor_de_arquivo)
        for livro in livros: 
            dados = [
                livro["titulo"],
                livro["autor"],
                livro["ano"],
                livro["isbn"],
                livro["status"],
            ]
            escritor.writerow(dados)# Escreve a lista Livros no livros.csv

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

    livros.append(novo_livro) # vai adicionar o novo livros cadastrado na lista
    salvar_dados(livros)# vai salvar a lista com o novo ivro em livro.csv
    print(f"\nLivro {titulo} cadastrado com sucesso!!!")
    return livros

def emprestar_livro(livros):
    print("\nREGISTRAR EMPRÉSTIMO")
    isbn_busca = input("Digite o ISBN do livro: ")

    for livro in livros:
        if livro["isbn"] == isbn_busca:
            if livro["status"] == "emprestado":
                print("\nEste livro já está emprestado!")
                return livros # Para a função e volta par o menu, pois foi onde q começou
            
            livro["status"] = "emprestado" # se não estiver emprestado vai ficar emprestádo(modificou na lista)
            salvar_dados(livros)#salvou a lista no livros.csv
            print("\nEmpréstimo realizado com sucesso!")
            return livros

    print("\nLivro não encontrado.")# Dessa forma ele vai ler toda a lista, se colocar if,elif e else ele vai ler só a primeira e da nçao encontrado
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
 
    for i in range(len(livros)):# numera os livros na lista livros
        if livros[i]["isbn"] == isbn_busca: # ve o livro com um numero que é o que vc quer apagar
            livro_removido = livros.pop(i)# apaga o livro que estava na posição na lista
            salvar_dados(livros) # atualiza a lista no livros.csv
            print(f"\nO livro {livro_removido} foi removido com sucesso!")
            return livros
 
    print("\nLivro não encontrado")
    return livros
def organizar_e_listar(livros):
 
    print("\nComo deseja organizar a lista?")
    print("1. Por Título (Ordem Alfabética)")
    print("2. Por Autor")
    print("3. Por Ano de Publicação")
    print("4. Ordem de cadastro")
    opcao_ordem = input("Escolha uma opção (1-4): ")
 
    if opcao_ordem == "1":
        livros.sort(key=lambda x: x["titulo"])#Tradução: "Organize a lista olhando para o título de cada livro (x)".
        print("\nLIVROS ORDENADOS POR TÍTULO:")
        for livro in livros:
            print(f"[{livro['status']}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")
    elif opcao_ordem == "2":
        livros.sort(key=lambda x: x["autor"])#sort ordena e key=lambda x: x fala como
        print("\nLIVROS ORDENADOS POR AUTOR:")
        for livro in livros:
            print(f"[{livro['status']}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")
    elif opcao_ordem == "3":
        livros.sort(key=lambda x: x["ano"])
        print("\nLIVROS ORDENADOS POR ANO:")
        for livro in livros:
                    print(f"[{livro['status']}] {livro['titulo']} - {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}")
    else:
        print("\nTODOS OS LIVROS (ORDEM DE CADASTRO):")
 
   

def buscar_livros(livros):
    print("\nBUSCAR LIVROS:")
    busca = input("Digite o título ou autor: ")
    
    encontrado = 0
    for livro in livros:
        if busca in livro["titulo"] or busca in livro["autor"]:
            print(f"[{livro['status'].()}] {livro['titulo']} por {livro['autor']} ({livro['ano']}) | ISBN: {livro['isbn']}") 
            encontrado = encontrado+1
    if encontrado == 0:
        print("Nenhum livro encontrado com esse termo.")

def menu():
    acervo = carregar_dados()

    while True:


        print("\nMENU PRINCIPAL DA BIBLIOTECA:")
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
            break
limpa()
menu()