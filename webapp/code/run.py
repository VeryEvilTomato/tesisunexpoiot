from app import app
from db import _db

_db.init_app(app)

@app.before_first_request
def crear_tablas():
    _db.create_all()