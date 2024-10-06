from flask_restx import Resource,Namespace
from schemas import Empleado,Departamento,Puesto
from api_models import empleadoModel, departamentoModel, puestoModel,departamentoPostModel
from ext import db

nameSpace = Namespace("API HRM")

@nameSpace.route("/Empleados")
class empleadoAPI(Resource):
    @nameSpace.marshal_list_with(empleadoModel)
    def get(self):
        return Empleado.query.all()

@nameSpace.route("/Departamentos")
class empleadoAPI(Resource):
    @nameSpace.marshal_list_with(departamentoModel)
    def get(self):
        return Departamento.query.all()
    

@nameSpace.route("/Puestos")
class empleadoAPI(Resource):
    @nameSpace.marshal_list_with(puestoModel)
    def get(self):
        return Puesto.query.all()
    

