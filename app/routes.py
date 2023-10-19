from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app import app, db

#Inicialização da aplicação Flask
app = Flask(__name__)

#Declaração chave secreta
app.secret_key = "chave_secreta"

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

        return jsonify({'message:''Usuário cadastrado com sucesso!!'})