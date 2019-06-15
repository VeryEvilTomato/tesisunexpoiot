from db import _db

class SwitchesModel(_db.Model):
    """Model para gestionar estados de interruptores"""
    __tablename__ = 'switches'

    id_switch = _db.Column(_db.Integer, primary_key=True)
    id_usuario = _db.Column(_db.Integer, _db.ForeignKey('usuarios.id_usuario'))
    nombre = _db.Column(_db.String(30))

    def __init__(self,id_usuario,nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def json(self):
        """Regresa en formato JSON el switch actual"""
        return {
            'nombre': self.nombre,
            'id_usuario': self.id_usuario
            }
    
    @classmethod
    def encontrar_por_id(cls,id_switch):
        """Encontrar switch en la DB por su id"""
        return cls.query.filter_by(id_switch=id_switch).first()

    @classmethod
    def encontrar_por_nombre(cls,nombre):
        """Encontrar switch en la DB por su nombre"""
        return cls.query.filter_by(nombre=nombre).first()
    
    def guardar_db(self):
        """Guardar switch en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    def borrar_db(self):
        """Borrar switch de la base de datos"""
        _db.session.delete(self)
        _db.session.commit()
