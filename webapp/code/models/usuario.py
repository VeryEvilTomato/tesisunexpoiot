from db import _db

class UsuarioModel(_db.Model):
    """Model para los usuarios registrados"""
    __tablename__ = 'users'
    id_usuario = _db.Column(_db.Integer, primary_key=True)
    usuario = _db.Column(_db.String(20), unique=True)
    password = _db.Column(_db.String(30))

    def __init__(self,usuario,password):
        self.usuario = usuario
        self.password = password

    def guardar_db(self):
        """Guardar usuario en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    @classmethod
    def encontrar_por_usuario(cls, usuario):
        """Método para encontrar usuario en base de datos"""
        return cls.query.filter_by(usuario=usuario).first()