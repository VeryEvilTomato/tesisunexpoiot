from db import _db

class MonitorModel(_db.Model):
    """Model para gestionar los datos de los monitores"""
    __tablename__ = 'monitores'

    id_monitor = _db.Column(_db.Integer, primary_key=True)
    id_usuario = _db.Column(_db.Integer, _db.ForeignKey('usuarios.id_usuario'))
    nombre = _db.Column(_db.String(30))
    variable = _db.Column(_db.String(30))

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
    def encontrar_por_id(cls,id_usuario):
        """Encontrar monitor en la DB por su id"""
        return cls.query.filter_by(id_usuario=id_usuario).first()

    @classmethod
    def encontrar_por_nombre_id(cls,nombre,id_usuario):
        """Encontrar monitor en la DB por su nombre"""
        return cls.query.filter_by(nombre=nombre).filter_by(id_usuario=id_usuario).first()
    
    def guardar_en_db(self):
        """Guardar monitor en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    def borrar_de_db(self):
        """Borrar monitor de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()
