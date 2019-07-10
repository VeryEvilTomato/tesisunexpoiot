from datetime import date
from flask_restful import Resource, reqparse
from server.models.monitor import MonitorModel
from server.handlers.user.users import UserModel 


class Monitor(Resource):
    """Clase para gestión de cada monitor de datos análogos"""
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Todo monitor necesita un nombre"
    )
    parser.add_argument(
        'variable',
        type=str,
        required=True,
        help="Todo monitor observa una variable"
    )

    def post(self,id_monitor,id_user):
        """Solicitud para guardar un Monitor nuevo en la base de datos"""

        req = Monitor.parser.parse_args()

        if MonitorModel.find_by_name_id(req["name"],id_user):
            return {"Mensaje": "Un Monitor con ese nombre ya existe"},400
        if not UserModel.find_by_id(id_user):
            return {"Mensaje": "El ID de usuario no existe"},400
        
        monitor = MonitorModel(id_user,**req)
        
        try:
            monitor.save_db()
        except:
            return{ "Mensaje": "Un error ha ocurrido insertando este monitor"},500

        return {"Mensaje": "Monitor creado exitosamente"},201

    def delete(self,id_monitor,id_user):
        """Solicitud para borrar un monitor de la base de datos"""

        if not UserModel.find_by_id(id_user):
            return {"Mensaje": "No se encontró un usuario con ese ID"},400
        
        monitor = MonitorModel.find_by_id(id_monitor)

        if monitor:
            monitor.delete_db()
            return {"Mensaje": "Monitor borrado de la base de datos"}, 201
        else:
            return {"Mensaje": "No se encontró el monitor especificado"}, 404


        
