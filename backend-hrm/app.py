from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hrm-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Duda ** Investigar luego*

db.init_app(app)
migrate = Migrate(app, db)

#ruta inicial
@app.route('/')
def index():
    return "Prueba de conexión"

if __name__ == '__main__':
    app.run(debug=True)



