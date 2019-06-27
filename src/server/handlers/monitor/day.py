from datetime import date
from flask_restful import Resource, reqparse
from models.monitores import MonitorModel
from models.usuario import UsuarioModel 

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

