from flask_restx import Resource,Namespace
from schemas import Empleado,Departamento,Puesto
from api_models import empleadoModel, departamentoModel, puestoModel,departamentoPostModel
from ext import db

nameSpace = Namespace("API HRM")

#EMPLEADOS
@nameSpace.route("/empleados")
class empleadoAPI(Resource):
    @nameSpace.marshal_list_with(empleadoModel)
    def get(self):
        return Empleado.query.all()

#DEPARTAMENTOS
@nameSpace.route("/departamentos")
class empleadoListAPI(Resource):
    @nameSpace.marshal_list_with(departamentoModel)
    def get(self):
        return Departamento.query.all()
    
    @nameSpace.expect(departamentoPostModel)
    @nameSpace.marshal_with(departamentoModel)#Nota * Conversion * JsonSerializable
    def post(self):
        data = nameSpace.payload
        departamentoExiste = Departamento.query.filter_by(departamento=data['departamento']).first()

        if departamentoExiste:
            return {"message": "El departamento ya existe."}, 409

        addDepartamento = Departamento(departamento=data['departamento'],estado=data['estado'])

        db.session.add(addDepartamento)
        db.session.commit()
        return addDepartamento, 201

@nameSpace.route("/departamento/<int:id>")
class departamentoAPI(Resource):
    @nameSpace.marshal_with(departamentoModel)
    def get(self,id):
        departamento = Departamento.query.get(id)
        return departamento
    
    @nameSpace.expect(departamentoPostModel)
    @nameSpace.marshal_with(departamentoModel) 
    def put(self,id):
        data = nameSpace.payload

        departamento = Departamento.query.get(id)
        departamento.departamento = data["departamento"]
        departamento.estado = data["estado"]
        db.session.commit()

        return departamento

    def delete (self, id):
        departamento = Departamento.query.get(id)
        db.session.delete(departamento)
        db.session.commit()
        return {"message": "Resistro eliminado exitosamente"}, 200

#PUESTOS
@nameSpace.route("/puestos")
class puestoAPI(Resource):
    @nameSpace.marshal_list_with(puestoModel)
    def get(self):
        return Puesto.query.all()
    

