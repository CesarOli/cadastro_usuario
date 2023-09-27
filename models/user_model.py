from app import db

class Usuário(db.Model):
    __tablename__ = 'usuários'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    cpf = db.Column(db.String(14), unique= True)
    pis = db.Column(db.String(11), uniqu=True)
    senha = db.Column(db.String(128))

endereco_id = db.Column(db.Integer, db.ForeignKey('endereço_id'))
endereco = db.relationship('Endereco', back_populates='usuario')
