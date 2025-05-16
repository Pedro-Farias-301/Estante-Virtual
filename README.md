# 📚 Estante Virtual

Um sistema simples de gerenciamento de biblioteca em Python. O projeto simula uma estante virtual onde usuários podem se registrar, fazer login e gerenciar uma coleção de livros de maneira fácil e interativa por meio do terminal.

## 🛠️ Funcionalidades

- ✅ Registro e login de usuários com salvamento em arquivo JSON
- ✅ Cadastro de livros com informações como:
  - Título
  - Autor
  - Edição
  - Editora
  - Ano de publicação
- ✅ Busca de livros pelo título
- ✅ Listagem completa de todos os livros cadastrados
- ✅ Persistência de dados usando arquivos JSON (`usuarios.json` e `estante.json`)

## 📁 Estrutura dos Arquivos

- `main.py`: Arquivo principal que inicia o sistema e gerencia os menus de interação.
- `Usuario.py`: Contém a lógica de cadastro e login de usuários.
- `Livros.py`: Implementa a classe e os métodos relacionados ao gerenciamento dos livros.
- `usuarios.json`: Armazena os dados dos usuários cadastrados.
- `estante.json`: Armazena os dados dos livros adicionados.

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou baixe os arquivos.
3. Execute o arquivo `main.py`:
   ```bash
   python main.py
