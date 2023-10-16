from models import user_model
from app import app, db
from flask import request, jsonify

#criação da rota/url 'cadastro'
@app.route('/cadastro', methods=['POST'])

#função que cadastra usuários
def cadastrar_usuario():

    #lógica para adquirir dados do usuário através do formulário
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        pis = request.form['pis']
        senha = request.form['senha']

        #criação de uma nova instância do modelo de usuário cadastrado.
        novo_usuario = user_model(nome=nome, email=email, cpf=cpf, pis=pis, senha=senha)

        #adição da instância criada ao banco de dados.
        db.session.add(novo_usuario)

        #salva a transação no banco de dados.
        db.session.commit()