from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from validators import CpfUnico, PisUnico

class CadastroUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=90)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11), Regexp(r'^\d{11}$', message='CPF inválido'), CpfUnico()])
    pis = StringField('PIS', validators=[DataRequired(), Length(min=11, max=11), Regexp(r'^\d{11}$', message='PIS inválido'), PisUnico()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
