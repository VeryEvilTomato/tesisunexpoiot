from server.data.db import _db
from server.models.states import StatesModel
import datetime

class SwitchModel(_db.Model):
    """Model para gestionar los datos de los switches"""
    __tablename__ = 'switches'

    id = _db.Column(_db.Integer, primary_key=True)
    id_user = _db.Column(_db.Integer, _db.ForeignKey('users.id'))
    name = _db.Column(_db.String(30))
    state = _db.Column(_db.Boolean)
    states = _db.relationship('StatesModel', cascade="all,delete", lazy='dynamic')

    def __init__(self,id_user,name,state):
        self.id_user = id_user
        self.name = name
        self.state = False

    def json(self):
        """Regresa en formato JSON el switch actual"""
        return {
            'id': self.id,
            'id_user': self.id_user,
            'name': self.name,
            'variable': self.current_state(),
            'type': 'switches',
            'registry': StatesModel.get_states(self.id)
            }
    
    def current_state(self):
        if self.state:
            return "Encendido"
        else:
            return "Apagado"

    @classmethod
    def find_by_id(cls,id_switch):
        """Encontrar switch en la DB por su id"""
        return cls.query.filter_by(id=id_switch).first()

    @classmethod
    def return_by_id_json(cls, id_user):
        """Todos los switches de un usuario en JSON"""
        switches = cls.query.filter_by(id_user=id_user).all()
        return {'content': [switch.json() for switch in switches]}

    @classmethod
    def find_by_name_id(cls,name,id_user):
        """Encontrar switch en la DB por su nombre"""
        return cls.query.filter_by(name=name).filter_by(id_user=id_user).first()

    def save_db(self):
        """Guardar switch en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    def delete_db(self):
        """Borrar switch de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()