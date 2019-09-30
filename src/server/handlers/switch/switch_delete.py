from flask_restful import reqparse, Resource
from server.models.switch import SwitchModel
from server.models.user import UserModel
from flask_jwt import jwt_required

class SwitchDelete(Resource):
    """Clase para borrar un interruptor al sistema"""

    @jwt_required()
    def delete(self, id_user, id_switch):
        """Solicitud para borrar un interruptor de la base de datos"""

        if not UserModel.find_by_id(id_user):
            return {"Mensaje": "No se encontró un usuario con ese ID"},400
        
        switch = SwitchModel.find_by_id(id_switch)

        if switch:
            switch.delete_db()
            return {"mensaje": "Switch borrado de la base de datos"}, 201
        else:
            return {"mensaje": "No se encontró el interruptor especificado"}, 404 