from flask_restful import Resource
from server.models.user import UserModel
from flask_jwt import jwt_required

class Options(Resource):
    @jwt_required()
    def get(self,id_user):
        if not UserModel.find_by_id(id_user):
            return { "mensaje" : "Error" }, 400

        return {
            "content": {
                "types": [
                    {
                        "name":"Monitor",
                        "request":"monitors"
                    },
                    {
                        "name": "Interruptor",
                        "request": "switches"
                    }
                ],
                "variables": [ "Celsius", "Fahrenheit", "Candela", "Humedad" ]
            }
        }, 200