from server.data.db import _db
import datetime
import pytz

class StatesModel(_db.Model):
    """Model para gestionar los estados de los interruptores"""
    __tablename__ = 'switchStates'

    id = _db.Column(_db.Integer, primary_key=True)
    state = _db.Column(_db.Boolean, nullable=False)
    date = _db.Column(_db.DateTime, nullable=False)
    id_switch = _db.Column(_db.Integer, _db.ForeignKey('switches.id'))
    switch = _db.relationship('SwitchModel')

    def __init__(self,id_switch,state):
        self.id_switch = id_switch
        self.state = state
    
    @classmethod
    def updateStates(cls, id_switch):
        """Observar si existen más de 10 entradas en el registro de cambios de estado"""
        states = cls.query.filter_by(id_switch=id_switch).all()
        if len(states) > 9:
            firstState = cls.query.filter_by(id_switch=id_switch).first()
            firstState.delete_db()
    
    @classmethod
    def get_states(cls, id_switch):
        """Obtener todos los estados de un dispositivo"""
        states = cls.query.filter_by(id_switch=id_switch).all()
        return [ state.json() for state in states ]
        
    def json(self):
        """Regresa en formato JSON el estado actual"""
        return {
            'state': self.checkState(),
            'time': self.date.strftime("%d/%m/%Y %H:%M:%S")
        }

    def checkState(self):
        if self.state:
            return "Encendido"
        else:
            return "Apagado"

    def save_db(self):
        """Guardar estado en la base de datos"""
        self.date = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(pytz.timezone('America/Caracas'))
        _db.session.add(self)
        _db.session.commit()
    
    def delete_db(self):
        """Borrar estado de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()