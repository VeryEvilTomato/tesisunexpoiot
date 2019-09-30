from flask_restful import reqparse, Resource
from server.models.switch import SwitchModel
from server.models.user import UserModel
from flask_jwt import jwt_required


class SwitchSubmit(Resource):
    """Clase para agregar un switch al sistema"""
    parser = reqparse.RequestParser();

    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Todo interruptor necesita un nombre"
    )

    @jwt_required()
    def post(self, id_user):
        """Solicitud para guardar un Switch nuevo en la base de datos"""

        req = SwitchSubmit.parser.parse_args()

        if SwitchModel.find_by_name_id(req["name"], id_user):
            return {"mensaje": "Un interruptor con ese nombre ya existe"}, 400
        if not UserModel.find_by_id(id_user):
            return {"mensaje": "El ID de ese usuario no existe"}, 400
        
        switch = SwitchModel(id_user, req["name"], False)
        
        try:
            switch.save_db()
        except:
            return { "mensaje": "Un error ha ocurrido insertando este interruptor"},500
        
        return {"mensaje": "Interruptor creado exitosamente"},201