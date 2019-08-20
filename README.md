# Casa domótica / Aplicación IoT

Autor:
- Orlando Guevara


## Ambiente de desarrollo

Asegúrate de tener instalado `python`, `pyenv` y ` pipenv`. Para instalar las dependencias del proyecto usa el comando:
```
pipenv install
```

Para ejecutar la aplicación web y el servidor usa el comando:
```
pipenv run python src/run.py
```

Para generar un build de la aplicación web, se debe ejecutar el siguiente comando estando dentro de la carpeta `src/client`:
```
npm run build
```

## Arquitectura del sistema
```
  (api) ---- (webapp) ---- (user)
  Python      React
    |
    |
(database)
  SQLite
```


## Recursos disponibles

- `/` - Aplicación web
- `/api/` - RESTish API


## Comportamiento del API

- `POST /api/user/register` - Registrar usuario

- `POST /api/monitors/` - Registrar un nuevo monitor
- `DELETE /api/monitors/<id>` - Borrar un monitor segun su ID

- `POST /api/monitors/2/data/` - Registrar lecturas para el monitor 2
- `GET  /api/monitors/1/data/date/2019-06-23` - Listado de lecturas del monitor de ID 1 el 20190623 (AñoMesDía)

