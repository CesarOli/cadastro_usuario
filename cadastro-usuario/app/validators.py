from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from app import db

class CpfUnico(object):
    def __call__(self, formulario, field):
        from models.user_model import Usuario
        
        usuario = db.session.query(Usuario).filter_by(cpf=field.data).first()
        if usuario is not None:
            raise ValidationError('CPF já cadastrado.')


class PisUnico(object):
    def __call__(self, formulario, field):
        from models.user_model import Usuario
        
        usuario = db.session.query(Usuario).filter_by(pis=field.data).first()
        if usuario is not None:
            raise ValidationError('PIS já cadastrado')
