from db import _db
import datetime

class MonitorModel(_db.Model):
    """Model para gestionar los datos de los monitores"""
    __tablename__ = 'monitores'

    id = _db.Column(_db.Integer, primary_key=True)
    id_usuario = _db.Column(_db.Integer, _db.ForeignKey('usuarios.id'))
    nombre = _db.Column(_db.String(30))
    variable = _db.Column(_db.String(30))
    datos = _db.relationship('MonitorDatoModel', lazy='dynamic')

    def __init__(self,id_usuario,nombre,variable):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.variable = variable

    def json(self):
        """Regresa en formato JSON el monitor actual"""
        return {
            'id_usuario': self.id_usuario,
            'Nombre': self.nombre,
            'Variable': self.variable
            }
    
    @classmethod
    def encontrar_por_id(cls,id_monitor):
        """Encontrar monitor en la DB por su id"""
        monitor = cls.query.filter_by(id=id_monitor).first()
        return monitor

    @classmethod
    def encontrar_por_nombre_id(cls,nombre,id_usuario):
        """Encontrar monitor en la DB por su nombre"""
        return cls.query.filter_by(nombre=nombre).filter_by(id_usuario=id_usuario).first()
    
    def datos_dia_json(self,fecha_dia):
        """Regresar JSON con los valores de un dia en específico"""
        datos = self.datos.all()
        return {'datos': [dato.json() for dato in filter(lambda x: x.fecha.date() == fecha_dia,datos)]}

    def guardar_en_db(self):
        """Guardar monitor en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    def borrar_de_db(self):
        """Borrar monitor de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()
