#Sistema de Gerenciamento de Biblioteca

Descrição:
Este projeto é um sistema dede biblioteca desenvolvido, que permite cadastrar livros, registrar empréstimos e devoluções, buscar livros, listar o acervo de diferentes formas e remover livros do estoque. Os dados são armazenados em um arquivo CSV, assim as informações são mantidas mesmo após fechar do programa.

Como executar o programa:

Para executar o sistemade biblioteca, é necessário ter o Visual Studio Code, Python e Git instalados no computador.

1. Instalar os programas necessários
Visual Studio Code — utilizado para abrir, editar e executar o código.
Python — linguagem utilizada para desenvolver o sistema.
Git — utilizado para baixar e controlar o projeto através do GitHub.

2. Acessar o projeto pelo GitHub
Acesse o GitHub e faça login na sua conta.
Abra o repositório do projeto.
Copie o link do repositório.
Abra o Visual Studio Code.
Utilize a opção de clonar um repositório (Clone Repository).
Cole o link do repositório do GitHub.
Escolha a pasta onde deseja salvar o projeto.
Aguarde o download dos arquivos.

3. Abrir o projeto no Visual Studio Code
Depois de clonar o repositório, abra a pasta do projeto no Visual Studio Code.
O projeto deve possuir:
SISTEMA_BIBLIOTECA
main.py - Contém o código principal
livros.csv - Armazena os dados dos livros cadastrados
README.md

Rode o programa 
Utilize o menu exibido no terminal para acessar as funcionalidades do sistema.

Requisitos técnicos aplicados:
Lista (livros) para armazenar os livros carregados do arquivo.
Dicionários para representar cada livro e seus atributos.
Utilização do arquivo livros.csv para armazenamento permanente dos dados.
Funções ao longo do código

Funções:
carregar_dados() - Passa o que já está salvo no livros.csv para a lista livros
salvar_dados() - Passa o que está na lista livros para o arquivo livros.csv
cadastrar_livro() - Cadastra um livro novo
emprestar_livro() - Registra o emprestimo de um livro
devolver_livro() - Registra a devolução de um livro
remover_livro() - Remove um livro do acevo
organizar_e_listar() - Lista os livros cadastrados, podendo ser por : título,autor,ano ou ordem de cadastro
buscar_livros() - Busca um livro pelo título ou autor
menu() - Menu principal onde escolhe o que deseja fazer e roda as funções

Requisitos técnicos aplicados:

Estruturas de dados:
A variável livros é utilizada como uma lista global para permitir que diferentes partes do programa acessem e atualizem os livros durante sua execução.
Lista: utilizada para armazenar os livros durante a execução do programa
Dicionários: utilizados para armazenar os dados de cada livro
(Cada livro possui: Título, autor, ano de publicação, ISBN, status (disponível ou emprestado))

Manipulação de arquivos:
Arquivo CSV: utilizado para armazenar os dados dos livros de forma permanente.
csv.reader: utilizado para realizar a leitura dos dados armazenados no livros.csv.
csv.writer: utilizado para gravar e atualizar os dados no livros.csv
Modos de abertura de arquivo (r e w): utilizados para leitura e escrita dos dados.

Estruturas de controle:
if, elif e else: utilizados para tomar decisões de acordo com as opções escolhidas pelo usuário e com as condições dos livros.
for: utilizado para percorrer os livros e realizar buscas, verificações e alterações.
while: utilizado para manter o menu principal funcionando até que o usuário escolha sair.

Organização de dados:
sort(): utilizado para ordenar os livros de acordo com título, autor ou ano de publicação.
lambda: utilizada junto ao sort() para definir qual informação será utilizada na ordenação.
len(): utilizada para obter a quantidade de livros e controlar a posição dos elementos durante a remoção.
append(): utilizado para adicionar novos livros à lista.
pop(): utilizado para remover livros da lista.
clear(): utilizado para limpar a lista antes de carregar novamente os dados do arquivo.
csv: utilizada para trabalhar com o arquivo livros.csv.
os: utilizada para limpar o terminal durante a execução do programa.






Beatriz Martins Antunes
