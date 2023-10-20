from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app import app, db
from models import user_model, Usuario

#Inicialização da aplicação Flask
app = Flask(__name__)

#Declaração chave secreta
app.secret_key = "chave_secreta"

class CadastroUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=90)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha =PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

@app.route('/cadastro', methods=['GET','POST'])

def cadastrar_usuario():
    formulario = CadastroUsuario()
    if formulario.validate_on_submit():
       
       usuario = Usuario(
           nome=formulario.nome.data,
           email=formulario.email.data,
           cpf=formulario.cpf.data,
           pis=formulario.pis.data,
           senha=formulario.senha.data
       )

        #adição da instância criada ao banco de dados.
       db.session.add(usuario)

        #salva a transação no banco de dados.
       db.session.commit()

       flash('Usuário cadastrado com sucesso!')

       return redirect(url_for('pagina_de_sucesso'))
    
    return render_template('cadastro_usuario.html', form=formulario)
