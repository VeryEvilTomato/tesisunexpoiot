# Casa domótica / Aplicación IoT

Autores:
- Orlando Guevara
- Luixandri Hernandez


## Ambiente de desarrollo

Asegúrate de tener instalado `python`, `pyenv` y ` pipenv`. Para instalar las dependencias del proyecto usa el comando:
```
pipenv install
```

Para ejecutar la aplicación web y el servidor usa el comando:
```
pipenv run python src/run.py
```

Si necesitas instalar un nuevo paquete usa el comando `pipenv install <paquete>`. Asegúrate de hacer commit de los cambios en los archivos `Pipfile` y `Pipfile.lock` luego de que hayas instalado un nuevo paquete.


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

- `GET /api/monitores/` - listado de monitores
- `GET /api/monitores/1/` - informacion del monitor 1
- `GET /api/monitores/1/lecturas/` - listado de lecturas del monitor 1
- `GET /api/monitores/1/lecturas/fecha/20190623` - listado de lecturas del monitor 1 el 20190623
- `POST /api/monitores/2/` - registar el monitor 2
- `POST /api/monitores/2/lecturas/` - registrar lecturas para el monitor 2
