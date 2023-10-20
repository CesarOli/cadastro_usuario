from typing import Any
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from app import app, db
from models import user_model, Usuario

#Inicialização da aplicação Flask
app = Flask(__name__)

#Declaração chave secreta
app.secret_key = "chave_secreta"

class CpfUnico(object):
    def __call__(self, formulario, field):
        usuario = db.session.query(Usuario).filter_by(cpf=field.data).first()
        if usuario is not None:
            raise ValidationError('CPF já cadastrado.')
        
class PisUnico(object):
    def __call__(self, formulario, field):
        usuario = db.session.query(Usuario).filter_by(pis=field.data).first()
        if usuario is not None:
            raise ValidationError('PIS já cadastrado')

class CadastroUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=90)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11,max=11), Regexp(r'^\d{11}$', message='CPF inválido'), CpfUnico()])
    pis = StringField('PIS',validators=[DataRequired(), Length(min=11, max=11), Regexp(r'^\d{11}$', message='PIS inválido'), PisUnico()])
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
