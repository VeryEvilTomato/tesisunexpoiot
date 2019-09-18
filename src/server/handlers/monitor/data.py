import datetime
from flask_restful import Resource, reqparse
from server.models.datum import MonitorDatumModel
from server.models.monitor import MonitorModel
from server.models.user import UserModel


class MonitorDatum(Resource):
    """Clase para gestión de cada dato"""
    parser = reqparse.RequestParser()

    parser.add_argument(
        'datum',
        type=float,
        required=True,
        help="El campo 'dato' no puede dejarse en blanco"
    )

    def post(self,id_monitor,id_user):
        """Solicitud para guardar un dato nuevo de un monitor en la base de datos"""

        req = MonitorDatum.parser.parse_args()

        monitorDatum = MonitorDatumModel(id_monitor, **req)

        if not MonitorModel.find_by_id(id_monitor):
            return{"Mensaje": "No existe un monitor con ese ID"},400
        if not UserModel.find_by_id(id_user):
            return {"Mensaje": "No existe un usuario con ese ID"},400

        try:
            monitorDatum.save_db()
        except:
            return {"Mensaje": "Un error ha ocurrido insertando este dato"}, 500

        return {"Mensaje": "Dato almacenado correctamente"},201
        

        

