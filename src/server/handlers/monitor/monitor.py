from datetime import date
from flask_restful import Resource, reqparse
from models.monitores import MonitorModel
from models.usuario import UsuarioModel 


class Monitor(Resource):
    """Clase para gestión de cada monitor de datos análogos"""
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'id_usuario',
        type=int,
        required=True,
        help="Todo monitor necesita un usuario"
    )
    parser.add_argument(
        'nombre',
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

    def post(self):
        """Solicitud para guardar un Monitor nuevo en la base de datos"""

        req = Monitor.parser.parse_args()

        if MonitorModel.encontrar_por_nombre_id(req["nombre"],req["id_usuario"]):
            return {"Mensaje": "Un Monitor con ese nombre ya existe"},400
        if not UsuarioModel.encontrar_por_id(req["id_usuario"]):
            return {"Mensaje": "El ID de usuario no existe"},400
        
        monitor = MonitorModel(**req)
        
        try:
            monitor.guardar_en_db()
        except:
            return{ "Mensaje": "Un error ha ocurrido insertando este monitor"},500

        return {"Mensaje": "Monitor creado exitosamente"},201

    def delete(self):
        """Solicitud para borrar un monitor de la base de datos"""

        req = Monitor.parser.parse_args()
        monitor = MonitorModel.encontrar_por_nombre_id(req["nombre"],req["id_usuario"])

        if monitor:
            monitor.borrar_de_db()
            return {"Mensaje": "Monitor borrado de la base de datos"}, 201
        else:
            return {"Mensaje": "No se encontró el monitor especificado"}, 404


class MonitorDia(Resource):
    """Clase para solicitar todos los datos de un día"""

    parser = reqparse.RequestParser()

    parser.add_argument(
        'id_monitor',
        type=float,
        required=True,
        help="El campo 'id_monitor' no puede dejarse en blanco"
    )

    parser.add_argument(
        'año',
        type=int,
        required=True,
        help="El campo 'año' no puede dejarse en blanco"
    )
    parser.add_argument(
        'mes',
        type=int,
        required=True,
        help="El campo 'mes' no puede dejarse en blanco"
    )
    parser.add_argument(
        'dia',
        type=int,
        required=True,
        help="El campo 'dia' no puede dejarse en blanco"
    )

    def get(self):
        """Solicitud de datos de un día entero de un monitor en la base de datos"""
        req = self.parser.parse_args()

        fechaDia = date(year=req["año"],month=req["mes"],day=req["dia"])

        monitorDia = MonitorModel.encontrar_por_id(req["id_monitor"])

        if monitorDia:
            return monitorDia.datos_dia_json(fechaDia)
        else:
            return {"Mensaje": "No se encontró el ID del monitor"}


        
