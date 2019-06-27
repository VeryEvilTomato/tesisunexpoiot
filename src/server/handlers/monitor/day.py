from datetime import datetime
from flask_restful import Resource
from server.models.monitor import MonitorModel

class MonitorDay(Resource):
    """Clase para solicitar todos los datos de un día"""

    def get(self,id_monitor,date):
        """Solicitud de datos de un día entero de un monitor en la base de datos"""

        dateDay = datetime.strptime(date,'%Y-%m-%d')
        monitor = MonitorModel.find_by_id(id_monitor)

        if monitor:
            return monitor.get_day_json(dateDay.date())
        else:
            return {"Mensaje": "No se encontró el ID del monitor"}

