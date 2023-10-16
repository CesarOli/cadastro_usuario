from app import db

class Endereco(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    mmunicipio = db.Column(db.String(50))
    cep = db.Column(db.String(10))
    rua = db.Column(db.String(150))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))

    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios_id'))
    usuarios = db.relationship('Usuario', back_populates='endereco')