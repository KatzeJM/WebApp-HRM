from flask import Flask
from flask_migrate import Migrate
from ext import db,api
from api_resources import empleadoNS, departamentoNS, puestoNS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/hrm-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Duda ** Investigar luego*

#Inicialización
db.init_app(app)
migrate = Migrate(app, db)

api.init_app(app)
#api.add_namespace(nameSpace)

api.add_namespace(empleadoNS)
api.add_namespace(departamentoNS)
api.add_namespace(puestoNS)

if __name__ == '__main__':
    app.run(debug=True)



