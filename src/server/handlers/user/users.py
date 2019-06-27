from flask_restful import Resource, reqparse
from server.models.user import UserModel


class User(Resource):
    """Clase para gestionar la ruta relacionada con registrar los usuarios"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'user',
        type=str,
        required=True,
        help="El campo 'user' no puede dejarse en blanco"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="El campo 'password' no puede dejarse en blanco"
    )

    def post(self):
        """Solicitud post para registrar usuarios"""
        req = User.parser.parse_args()

        if UserModel.find_by_user(req['user']):
            return {"Mensaje": "El usuario ya existe"}, 400
        
        usuario = UserModel(**req)
        usuario.save_db()
        
        return {"Mensaje": "Usuario creado exitosamente"}, 201