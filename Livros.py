import json
import os

class Livros:
    estante = []  

    def __init__(self, titulo, autor, edicao, editora, ano):
        self.titulo = titulo
        self.autor = autor
        self.edicao = edicao
        self.editora = editora
        self.ano = ano

    def cadastrar_livro(self):
        livro_info = {
            'Título': self.titulo,
            'Autor': self.autor,
            'Edição': self.edicao,
            'Editora': self.editora,
            'Ano': self.ano
        }
        Livros.estante.append(livro_info)
        Livros.salvar_estante()
        print("Livro cadastrado com sucesso!")

    @classmethod
    def buscar_livro(cls):
        nome_livro = input("Digite o nome do livro que deseja buscar: ")

        encontrados = [
            livro for livro in cls.estante
            if nome_livro.lower() in livro['Título'].lower()
        ]

        if encontrados:
            print("\nLivro(s) encontrado(s):")
            for livro in encontrados:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}")
                print('-' * 30)
        else:
            print("Livro não encontrado na estante.")

    @classmethod
    def listar_estante(cls):
        if not cls.estante:
            print("A estante está vazia.")
        else:
            print("\nTodos os livros cadastrados:")
            for livro in cls.estante:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}")
                print('-' * 30)

    @classmethod
    def listar_estante(cls):
        if not cls.estante:
            print("A estante está vazia.")
        else:
            print("\nTodos os livros cadastrados:")
            for livro in cls.estante:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}")
                print('-' * 30)

    @classmethod
    def salvar_estante(cls):
        with open("estante.json", "w", encoding="utf-8") as f:
            json.dump(cls.estante, f, ensure_ascii=False, indent=4)

    @classmethod
    def carregar_estante(cls):
        if os.path.exists("estante.json"):
            with open("estante.json", "r", encoding="utf-8") as f:
                cls.estante = json.load(f)

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"
