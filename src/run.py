from app import app
from server.data.db import _db

_db.init_app(app)

@app.before_first_request
def create_tables():
    _db.create_all()

app.run(host='0.0.0.0',port=5000)