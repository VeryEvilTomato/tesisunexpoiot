from db import _db

class MonitorDatoModel(_db.model):
    """Modelo para gestionar los datos del dispositivo IoT a monitorear"""

    def __init__(self,id_monitor,estado):
        self.id_monitor = id_monitor
        self.dato = dato