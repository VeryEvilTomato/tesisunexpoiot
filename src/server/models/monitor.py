from server.data.db import _db
import datetime

class MonitorModel(_db.Model):
    """Model para gestionar los datos de los monitores"""
    __tablename__ = 'monitors'

    id = _db.Column(_db.Integer, primary_key=True)
    id_user = _db.Column(_db.Integer, _db.ForeignKey('users.id'))
    name = _db.Column(_db.String(30))
    variable = _db.Column(_db.String(30))
    data = _db.relationship('MonitorDatumModel', lazy='dynamic')

    def __init__(self,id_user,name,variable):
        self.id_user = id_user
        self.name = name
        self.variable = variable

    def json(self):
        """Regresa en formato JSON el monitor actual"""
        return {
            'id_user': self.id_usuario,
            'name': self.name,
            'variable': self.variable
            }
    
    @classmethod
    def find_by_id(cls,id_monitor):
        """Encontrar monitor en la DB por su id"""
        return cls.query.filter_by(id=id_monitor).first()

    @classmethod
    def find_by_name_id(cls,name,id_user):
        """Encontrar monitor en la DB por su nombre"""
        return cls.query.filter_by(name=name).filter_by(id_user=id_user).first()
    
    def get_day_json(self,dataDate):
        """Regresar JSON con los valores de un dia en específico"""
        data = self.data.all()
        return {'data': [datum.json() for datum in filter(lambda x: x.date.date() == dataDate,data)]}

    def save_db(self):
        """Guardar monitor en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    def delete_db(self):
        """Borrar monitor de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()
