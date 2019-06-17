from flask_restful import Resource, reqparse
from models.switches import SwitchesModel
from models.usuario import UsuarioModel

class Switch(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument(
        'nombre',
        type=str,
        required=True,
        help="Todo switch necesita un nombre"
    )
    parser.add_argument(
        'id_usuario',
        type=int,
        required=True,
        help="Todo switch necesita un usuario"
    )

    def post(self):
        """Solicitud para guardar un Switch nuevo en la base de datos"""

        datos = Switch.parser.parse_args()

        if SwitchesModel.encontrar_por_nombre_id(datos["nombre"],datos["id_usuario"]):
            return {"Mensaje": "Un switch con ese nombre ya existe"},400
        if not UsuarioModel.encontrar_por_id(datos["id_usuario"]):
            return {"Mensaje": "El ID de usuario no existe"},400
        
        switch = SwitchesModel(**datos)
        try:
            switch.guardar_en_db()
        except:
            return{ "Mensaje": "Un error ha ocurrido insertando este switch"},500

        return {"Mensaje": "Switch creado exitosamente"},201

    def delete(self):
        """Solicitud para borrar un switch de la base de datos"""

        datos = Switch.parser.parse_args()
        switch = SwitchesModel.encontrar_por_nombre_id(datos["nombre"],datos["id_usuario"])

        if switch:
            switch.borrar_de_db()
        return {"Mensaje": "Switch borrado de la base de datos"}, 201
        
