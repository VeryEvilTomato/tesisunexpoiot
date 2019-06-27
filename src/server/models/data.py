import datetime
import pytz
from db import _db

class MonitorDatoModel(_db.Model):
    """Modelo para gestionar los datos del sensor análogo IoT a monitorear"""
    __tablename__ = 'monitorDatos'

    zh = pytz.timezone('Etc/GMT-4')
    dtlocal = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(zh)

    id = _db.Column(_db.Integer, primary_key=True)
    dato = _db.Column(_db.Float, nullable=False)
    fecha = _db.Column(_db.DateTime, nullable=False,
        default=pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(pytz.timezone('America/Caracas'))
    )

    id_monitor = _db.Column(_db.Integer, _db.ForeignKey('monitores.id'))
    monitor = _db.relationship('MonitorModel')

    def __init__(self,id_monitor,dato):
        self.id_monitor = id_monitor
        self.dato = dato

    def json(self):
        """Regresa en formato JSON el dato actual"""
        return {
            'Dato': self.dato,
            'Fecha': {
                'Hora': self.fecha.hour,
                'Min': self.fecha.minute
            }
        }

    def guardar_en_db(self):
        """Guardar monitor en la base de datos"""
        self.fecha = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(pytz.timezone('America/Caracas'))
        _db.session.add(self)
        _db.session.commit()