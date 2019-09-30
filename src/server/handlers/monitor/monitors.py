from flask_restful import Resource
from server.models.monitor import MonitorModel
from server.handlers.user.users import UserModel
from flask_jwt import jwt_required


class Monitors(Resource):
    """Clase para solicitar los monitores de un usuario"""
    @jwt_required()
    def get(self,id_user):
        """Solicitud para guardar un Monitor nuevo en la base de datos"""
        if not UserModel.find_by_id(id_user):
            return {"Mensaje": "No existe un usuario asociado con ese ID"}

        return MonitorModel.return_by_id_json(id_user), 200