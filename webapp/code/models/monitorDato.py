import datetime
import pytz
from db import _db

class MonitorDatoModel(_db.Model):
    """Modelo para gestionar los datos del sensor análogo IoT a monitorear"""
    __tablename__ = 'monitorDatos'

    zh = pytz.timezone('Etc/GMT-4')
    dtlocal = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(zh)

    id_monitor = _db.Column(_db.Integer, _db.ForeignKey('monitores.id_monitor'))
    id_monitorDato = _db.Column(_db.Integer, primary_key=True)
    dato = _db.Column(_db.Float, nullable=False)
    datetime = _db.Column(_db.DateTime, nullable=False,
        default=pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(pytz.timezone('America/Caracas'))
    )

    def __init__(self,id_monitor,dato):
        self.id_monitor = id_monitor
        self.dato = dato

    def json(self):
        """Regresa en formato JSON el monitor actual"""
        return {
            'id_monitor': self.id_usuario,
            'Dato': self.dato
        }

    def guardar_en_db(self):
        """Guardar monitor en la base de datos"""
        _db.session.add(self)
        _db.session.commit()