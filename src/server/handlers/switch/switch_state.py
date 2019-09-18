from flask_restful import Resource, reqparse
from server.models.switch import SwitchModel
from server.models.states import StatesModel
from server.handlers.user.users import UserModel 


class SwitchState(Resource):
    """Clase para cambiar el estado de un interruptor"""
    
    def put(self, id_user, id_switch):

        switch = SwitchModel.find_by_id(id_switch)

        if not switch:
            return {"mensaje": "No existe un interruptor con ese ID"}
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "No existe un usuario con ese ID"}

        switch.state = not switch.state
        state = StatesModel(id_switch, switch.state)

        StatesModel.updateStates(id_switch)

        try:
            switch.save_db()
            state.save_db()
        except:
            return {"mensaje": "Ocurrió un error cambiando el estado de este monitor"}, 500

        return {"mensaje": switch.state}, 201