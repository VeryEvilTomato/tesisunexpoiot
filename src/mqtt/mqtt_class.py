import traceback
import json
import time
from flask_mqtt import Mqtt

#Models
from server.models.user import UserModel
from server.models.monitor import MonitorModel
from server.models.datum import MonitorDatumModel

class MqttClass:
    def init_app(self, app):
        self.mqtt = Mqtt(app)

        @self.mqtt.on_connect()
        def handle_connect(client, userdata, flags, rc):
            self.mqtt.subscribe(topic='+/user/+/monitors/+', qos=1)

        @self.mqtt.on_message()
        def handle_message(client, userdata, message):
            try:
                messageArr = message.topic.split('/', 4)
            except:
                traceback.print_exc()
                print("Error en el tópico del mensaje")
            
            # messageArr[0] - Usuario
            # messageArr[2] - Nombre del monitor

            with app.app_context():
                user = UserModel.find_by_user(messageArr[2])
                if not user:
                    print("No se encuentra el usuario")
                    return
                monitor = MonitorModel.find_by_name_id( messageArr[4], user.id)
                if not monitor:
                    print("No existe el monitor", messageArr[4])

                datum = MonitorDatumModel(monitor.id, message.payload.decode())
                try:
                    datum.save_db()
                    print("Dato insertado para", messageArr[2])
                except:
                    print("Error insertando en la base de datos")

        @self.mqtt.on_publish()
        def handle_publish(client, userdata, result):
            print("Exitosamente publicado")
            pass
        
    def publish(self, user, name, payload):
        topic = [user,'switches', name]
        topicStr = "/".join(topic)
        try:
            self.mqtt.publish(topic=topicStr, payload=payload, qos=1)
            print("Topic:", topicStr)
            print("Data: ", payload)
        except:
            traceback.print_exc()
        pass

# Interpretar JSON del payload
# try:
#     payload = json.loads(str(message.payload.decode()))
#     print("Topic:   ", str(message.topic))
#     print("Payload: ", payload)
# except:
#     print("Payload: ")
#     print(str(message.payload.decode()))
#     print("Error message")
#     traceback.print_exc()