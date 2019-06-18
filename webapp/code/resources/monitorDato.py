import datetime
from flask_restful import Resource, reqparse
from models.monitorDato import MonitorDatoModel


class MonitorDato(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'id_monitor',
        type=float,
        required=True,
        help="El campo 'Estado' no puede dejarse en blanco"
    )
    parser.add_argument(
        'dato',
        type=float,
        required=True,
        help="El campo 'Estado' no puede dejarse en blanco"
    )

    def post(self):
        """Solicitud para guardar un Monitor nuevo en la base de datos"""
        req = MonitorDato.parser.parse_args()

        monitorDato = MonitorDatoModel(**req)

        try:
            monitorDato.guardar_en_db()
        except:
            return {"Mensaje": "Un error ha ocurrido insertando este dato"}, 500

        return {"Mensaje": "Dato almacenado correctamente"}