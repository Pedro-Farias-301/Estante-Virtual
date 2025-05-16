from Usuario import Usuario
from Livros import Livros

Usuario.carregar_usuarios()

def Entrada():
    while True:
        print('''
        ==== SISTEMA DE LOGIN ====
        1. Fazer login
        2. Registrar novo usuário
        3. Sair
        ''')

        opcao = input("> ")
        if opcao == '1':
            if Usuario.login():
                break  
        elif opcao == '2':
            Usuario.registrar()
        elif opcao == '3':
            print("Encerrando o sistema...")
            exit()
        else:
            print("Opção inválida")


def menu_principal():
    while True:
        print("\nO que você deseja fazer? ")
        print('''
1. Cadastrar um novo livro
2. Procurar por um livro
3. Mostrar todos os livros
4. Sair
        ''')
        try:
            opcao = int(input("> "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 1:
            tit = input("Título do livro: ")
            aut = input("Autor: ")
            ed = input("Editor: ")
            edit = input("Editora: ")
            try:
                year = int(input("Ano: "))
            except ValueError:
                print("Ano inválido. Deve ser um número.")
                continue
            livro = Livros(tit, aut, ed, edit, year)
            print("Livro cadastrado com sucesso!")
            livro.cadastrar_livro()

        elif opcao == 2:
            Livros.buscar_livro()
        
        elif opcao == 3:
            Livros.listar_estante()
            

        elif opcao == 4:
            confirmar = input("Você confirma que deseja sair? [S/N] ").lower()
            if confirmar == "s":
                print("Volte sempre!")
                break
            else:
                print("Retornando ao menu principal...")

        else:
            print("Opção inválida. Tente novamente.")

# Execução
Entrada()
Livros.carregar_estante()
menu_principal()
