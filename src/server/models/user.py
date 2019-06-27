from server.data.db import _db


class UserModel(_db.Model):
    """Model para los usuarios registrados"""
    __tablename__ = 'users'
    id = _db.Column(_db.Integer, primary_key=True)
    user = _db.Column(_db.String(20), unique=True)
    password = _db.Column(_db.String(30))

    def __init__(self,user,password):
        self.user = user
        self.password = password

    def save_db(self):
        """Guardar usuario en la base de datos"""
        _db.session.add(self)
        _db.session.commit()

    @classmethod
    def find_by_user(cls, user):
        """Método para encontrar usuario en base de datos"""
        return cls.query.filter_by(user=user).first()
    
    @classmethod
    def find_by_id(cls,id_user):
        """Método para encontrar id de usuario en la base de datos"""
        return cls.query.filter_by(id=id_user).first()