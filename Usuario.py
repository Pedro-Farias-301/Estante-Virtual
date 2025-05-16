import json
import os
import getpass

class Usuario:
    usuarios = {}

    @classmethod
    def carregar_usuarios(cls):
        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r", encoding="utf-8") as f:
                cls.usuarios = json.load(f)

    @classmethod
    def salvar_usuarios(cls):
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(cls.usuarios, f, ensure_ascii=False, indent=4)

    @classmethod
    def registrar(cls):
        username = input("Novo nome de usuário: ")
        if username in cls.usuarios:
            print("Usuário já existe. Tente outro nome.")
            return
        senha = getpass.getpass("Digite sua senha: ")
        cls.usuarios[username] = senha
        cls.salvar_usuarios()
        print("Usuário registrado com sucesso!")

    @classmethod
    def login(cls):
        username = input("Digite seu nome de usuário: ")
        senha = getpass.getpass("Digite sua senha: ")
        if cls.usuarios.get(username) == senha:
            print(f"Bem-vindo, {username}!")
            return True
        else:
            print("Usuário ou senha incorretos.")
            return False
