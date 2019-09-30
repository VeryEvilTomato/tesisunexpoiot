from flask_restful import Resource, reqparse
from server.models.switch import SwitchModel
from server.handlers.user.users import UserModel
from flask_jwt import jwt_required

class Switches(Resource):
    @jwt_required()
    def get(self, id_user):
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "No existe un usuario con ese ID"}
        return SwitchModel.return_by_id_json(id_user)