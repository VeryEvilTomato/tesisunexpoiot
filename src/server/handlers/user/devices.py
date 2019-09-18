from flask_restful import Resource
from server.models.user import UserModel
from server.models.monitor import MonitorModel
from server.models.switch import SwitchModel

class Devices(Resource):
    """Clase para solicitar todos los dispositivos de un usuario"""
    def get(self, id_user):
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "no existe un usuario con ese ID"}

        monitors = MonitorModel.return_by_id_json(id_user)
        switches = SwitchModel.return_by_id_json(id_user)

        devices = monitors["content"] + switches["content"]

        return {'content': devices}