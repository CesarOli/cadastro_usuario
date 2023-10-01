# Projeto de Cadastro de Usuário

## Descrição
Este é um projeto de desenvolvimento de uma aplicação web para o cadastro de usuários. A aplicação é direcionada apenas no backend e será desenvolvida através do linguagem de programação Python, framework Flask e banco de dados PostgreSQL.

## Objetivo de Aprendizados
O principal objetivo deste projeto é aprender e praticar o desenvolvimento de aplicativos web com foco no backend. Os principais tópicos de aprendizado incluem:

- Configuração do ambiente de desenvolvimento com Python, Flask e PostgreSQL.
   - Configuração de Variáveis de ambiente;
   - Criação do arquivo .gitignore para não publicar informações sensíveis do projeto;
- Criação de um banco de dados PostgreSQL e definição da estrutura de dados.
- Implementação de recursos de autenticação, incluindo registro, login e gerenciamento de sessões.
- Desenvolvimento de páginas web simples para apresentar informações aos usuários.
- Implementação de operações CRUD (Criar, Ler, Atualizar, Excluir) para os dados do usuário.
- Validação de campos de entrada e gerenciamento de erros.

## Bibliotecas Utilizadas
Durante o desenvolvimento deste projeto, foram utilizadas as seguintes bibliotecas e frameworks:

- Framework Flask
- Flask-SQLAlchemy: Uma extensão do Flask para interagir com bancos de dados SQLAlchemy.
- PostgreSQL: Um sistema de gerenciamento de banco de dados relacional.


## Como usar: 
Para executar este projeto em seu ambiente local, siga estas etapas:

1. Clone este repositório para o seu computador.

2. Configure o ambiente virtual Python e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
   pip install -r requirements.txt


    Configure o banco de dados PostgreSQL e atualize as configurações no arquivo .env.

    Execute a aplicação:

    bash
    Copy code
    flask run
    Acesse a aplicação em seu navegador web em http://localhost:5000.
