from models import user_model
from app import app, db
from flask import request, jsonify

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        pis = request.form['pis']
        senha = request.form['senha']