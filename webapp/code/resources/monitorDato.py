from flask_restful import Resource, reqparse
from models.monitorDato import monitorDatoModel

class monitorDato(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id_usuario',
        type=int,
        required=True,
        help="El campo 'id_usuario' no puede dejarse en blanco"
    )
    parser.add_argument(
        'dato',
        type=str,
        required=True,
        help="El campo 'Estado' no puede dejarse en blanco"
    )

    def post(self):
        pass