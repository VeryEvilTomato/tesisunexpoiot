import datetime
from flask_restful import Resource, reqparse
from models.monitorDato import MonitorDatoModel
from models.monitores import MonitorModel

class MonitorDato(Resource):
    """Clase para gestión de cada dato"""
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id_monitor',
        type=int,
        required=True,
        help="El campo 'id_monitor' no puede dejarse en blanco"
    )

    parser.add_argument(
        'dato',
        type=float,
        required=True,
        help="El campo 'dato' no puede dejarse en blanco"
    )

    def post(self):
        """Solicitud para guardar un dato nuevo de un monitor en la base de datos"""

        req = MonitorDato.parser.parse_args()

        monitorDato = MonitorDatoModel(**req)

        if not MonitorModel.encontrar_por_id(req["id_monitor"]):
            return{"Mensaje": "No existe un usuario con ese id_usuario"},400
        
        try:
            monitorDato.guardar_en_db()
        except:
            return {"Mensaje": "Un error ha ocurrido insertando este dato"}, 500

        return {"Mensaje": "Dato almacenado correctamente"},201
        

        

