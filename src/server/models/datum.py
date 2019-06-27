from server.data.db import _db
import datetime
import pytz

class MonitorDatumModel(_db.Model):
    """Modelo para gestionar los datos del sensor análogo IoT a monitorear"""
    __tablename__ = 'monitorData'

    id = _db.Column(_db.Integer, primary_key=True)
    datum = _db.Column(_db.Float, nullable=False)
    date = _db.Column(_db.DateTime, nullable=False)
    id_monitor = _db.Column(_db.Integer, _db.ForeignKey('monitors.id'))
    monitor = _db.relationship('MonitorModel')

    def __init__(self,id_monitor,datum):
        self.id_monitor = id_monitor
        self.datum = datum

    def json(self):
        """Regresa en formato JSON el dato actual"""
        return {
            'datum': self.datum,
            'date': {
                'Hour': self.date.hour,
                'Min': self.date.minute
            }
        }

    def save_db(self):
        """Guardar monitor en la base de datos"""
        self.date = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(pytz.timezone('America/Caracas'))
        _db.session.add(self)
        _db.session.commit()