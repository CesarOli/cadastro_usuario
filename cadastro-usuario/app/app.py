
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect
from forms import CadastroUsuario
from models.user_model import Usuario

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')
csrf = CSRFProtect(app)

app.secret_key = "chave_secreta"

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Seja Bem Vindo!!!'

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
    
if __name__ == '__main__':
    app.run(debug=True)