# Tomate IoT / Application to monitor IoT data and control IoT Devices

Devices will communicate with a web server using the Mosquitto MQTT broker as a bridge, Flask will connect to the broker using the MQTT Flask extension, thus establishing connection with said devices. All data handled will be saved into a SQLite3 database for users to monitor/control using a client side web application developed with React and MobX.

## Architecture
```
(devices)---(broker)-----(api) ---- (webapp) ---- (user)
           Mosquitto    Python       React
                           |
                           |
                       (database)
                        SQLite3
```

## Setup

Make sure to have installed `mosquitto`, `python`, `pyenv` and ` pipenv`. To install all of the project's dependencies use the following command:
```
pipenv install
```
(Before launching the web server) Start the MQTT Broker by using the following command inside src/mqtt
```
mosquitto -c config.conf
```

Launch the Flask web server which hosts the application:
```
pipenv run python src/run.py
```

To build the web static files, you must execute inside `src/client`:
```
npm install
```
then
```
npm run build
```

## Resources

- `/` - Web application 
- `/api/` - RESTish API


## API Behaviour

- `POST /api/user/register` - Register user

- `POST /api/monitors/` - Register a new monitor
- `DELETE /api/monitors/<id>` - Deleting a monitor with an specific ID

- `POST /api/monitors/2/data/` - Submit new lecture for specific monitor (mainly made for testing). 
- `GET  /api/monitors/1/data/date/2019-06-23` - Lecture data from monitor with ID 1 in the date 2019/06/23 (YearMonthDay)

## About

This application was developed as a dissertation work project to get an electronic engineering degree at the UNEXPO Vicerrectorado Puerto Ordaz University. This university lies on a spanish speaking country, hence why comments are in spanish.

Author:
- Orlando Guevara
