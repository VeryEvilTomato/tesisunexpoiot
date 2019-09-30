from flask_restful import Resource, reqparse
from server.models.monitor import MonitorModel
from server.handlers.user.users import UserModel 
from flask_jwt import jwt_required

class MonitorDelete(Resource):
    """Clase para borrar un monitor del sistema"""
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Especifique el nombre del monitor a borrar por favor"
    )

    @jwt_required()
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