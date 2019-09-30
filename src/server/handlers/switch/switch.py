from flask_restful import reqparse, Resource
from server.models.switch import SwitchModel
from server.models.states import StatesModel
from server.models.user import UserModel
from flask_jwt import jwt_required


class Switch(Resource):
    """Clase para chequear el estado de un switch al sistema"""
    @jwt_required()
    def get(self, id_switch, id_user):
        switch = SwitchModel.find_by_id(id_switch)
            
        if not switch:
            return {"mensaje": "No existe un interruptor con ese id"}, 400
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "No existe un usuario con ese id"}, 400
        
        return { 'device': switch.json() }