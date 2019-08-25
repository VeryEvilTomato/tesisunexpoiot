from datetime import datetime
from flask_restful import Resource
from server.models.monitor import MonitorModel
from server.models.user import UserModel

class MonitorDay(Resource):
    """Clase para solicitar todos los datos de un día"""

    def get(self,id_monitor,id_user,date):
        """Solicitud de datos de un día entero de un monitor en la base de datos"""

        if not UserModel.find_by_id(id_user):
            return {"Mensaje":"No existe un usuario con ese ID"},400

        dateDay = datetime.strptime(date,'%Y%m%d')
        monitor = MonitorModel.find_by_id(id_monitor)

        if monitor:
            return monitor.get_day_json(dateDay.date()), 200
        else:
            return {"Mensaje": "No se encontró el ID del monitor"}, 400
