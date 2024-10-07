from flask_restx import Resource,Namespace,abort
from schemas import Empleado,Departamento,Puesto
from api_models import empleadoModel,empleadoPostModel, departamentoModel,departamentoPostModel, puestoPostModel,puestoModel
from ext import db

#nameSpace = Namespace("API HRM")
empleadoNS = Namespace("Empleados", description="EndPoints de empleados")
departamentoNS = Namespace("Departamentos", description="EndPoints de Departamentos")
puestoNS = Namespace("Puestos", description="EndPoints de Puesto")


#EMPLEADOS
@empleadoNS.route("/empleados")
class empleadoListAPI(Resource):
    @empleadoNS.marshal_list_with(empleadoModel)
    def get(self):
        return Empleado.query.all()
    
    @empleadoNS.expect(empleadoPostModel)
    @empleadoNS.marshal_with(empleadoModel)#Nota * Conversion * JsonSerializable
    def post(self):
        data = empleadoNS.payload
        departamento = data['departamento_id']  
        puesto = data['puesto_id']    

        if not departamento:
            abort(404, "El departamento ingresado no existe.")

        if not puesto:
            abort(404, "El puesto ingresado no existe.")

        addEmpleado = Empleado(
            nombre=data['nombre'],
            apellido=data['apellido'],
            direccion=data['direccion'],
            fechaNacimiento=data['fechaNacimiento'],
            estado=data['estado'],
            departamento_id=data['departamento_id'],
            puesto_id=data['puesto_id']   
        )

        db.session.add(addEmpleado)
        db.session.commit()
        return addEmpleado, 201



@empleadoNS.route("/empleados/<int:id>")
class EmpleadoAPI(Resource):
    @empleadoNS.marshal_with(empleadoModel)
    def get(self, id):
        empleado = Empleado.query.get(id)

        if not empleado:
            abort(404, f"El empleado con el ID {id} no existe.")
        return empleado

    @empleadoNS.expect(empleadoPostModel)
    @empleadoNS.marshal_with(empleadoModel) 
    def put(self, id):
        data = empleadoNS.payload
        empleado = Empleado.query.get(id)

        if not empleado:
            abort(404, f"El empleado con el ID {id} no existe.")

        empleado.nombre = data["nombre"]
        empleado.apellido = data["apellido"]
        empleado.direccion = data["direccion"]
        empleado.fechaNacimiento = data["fechaNacimiento"]
        empleado.estado = data["estado"]

        if "departamento_id" in data:
            empleado.departamento_id = data["departamento_id"]

        if "puesto_id" in data:
            empleado.puesto_id = data["puesto_id"]
            
        db.session.commit()
        return empleado

    def delete(self, id):
        empleado = Empleado.query.get(id)

        if not empleado:
            abort(404, f"El empleado con el ID {id} no existe.")

        empleado.departamento_id = None 
        empleado.puesto_id = None

        db.session.delete(empleado)
        db.session.commit()
        return {"message": f"El empleado con ID {id} fue eliminado exitosamente."}, 200

#DEPARTAMENTOS
@departamentoNS.route("/departamentos")
class empleadoListAPI(Resource):
    @departamentoNS.marshal_list_with(departamentoModel)
    def get(self):
        return Departamento.query.all()
    
    @departamentoNS.expect(departamentoPostModel)
    @departamentoNS.marshal_with(departamentoModel)#Nota * Conversion * JsonSerializable
    def post(self):
        data = departamentoNS.payload
        departamentoExiste = Departamento.query.filter_by(departamento=data['departamento']).first()

        if departamentoExiste:
            abort(409, "El departamento ingresado, ya existe.")

        addDepartamento = Departamento(departamento=data['departamento'],estado=data['estado'])

        db.session.add(addDepartamento)
        db.session.commit()
        return addDepartamento, 201

@departamentoNS.route("/departamento/<int:id>")
class departamentoAPI(Resource):
    @departamentoNS.marshal_with(departamentoModel)
    def get(self,id):
        departamento = Departamento.query.get(id)

        if not departamento:
            abort(404, f"El departamento con el ID {id} no existe.")
        return departamento
    
    @departamentoNS.expect(departamentoPostModel)
    @departamentoNS.marshal_with(departamentoModel) 
    def put(self,id):
        data = departamentoNS.payload
        departamento = Departamento.query.get(id)

        if not departamento:
            abort(404, f"El departamento con el ID {id} no existe.")

        departamento.departamento = data["departamento"]
        departamento.estado = data["estado"]
        db.session.commit()
        return departamento

    def delete (self, id):
        departamento = Departamento.query.get(id)
        if not departamento:
            abort(404, f"El departamento con el ID {id} no existe.")

        db.session.delete(departamento)
        db.session.commit()
        return {"message": f"El departamento con ID {id} fue eliminado exitosamente."}, 200
       

#PUESTOS
@puestoNS.route("/puestos")
class puestoListAPI(Resource):
    @puestoNS.marshal_list_with(puestoModel)
    def get(self):
        return Puesto.query.all()
    
    @puestoNS.expect(puestoPostModel)
    @puestoNS.marshal_with(puestoModel)
    def post(self):
        data = puestoNS.payload
        puestoExiste = Puesto.query.filter_by(puesto=data['puesto']).first()

        if puestoExiste:
            abort(409, "El puesto ingresado, ya existe.")

        addPuesto= Puesto(puesto=data['puesto'],estado=data['estado'])
        db.session.add(addPuesto)
        db.session.commit()
        return addPuesto, 201
    

@puestoNS.route("/puesto/<int:id>")
class puestoAPI(Resource):
    @puestoNS.marshal_with(puestoModel)
    def get(self,id):
        puesto = Puesto.query.get(id)
        return puesto
    
    @puestoNS.expect(puestoPostModel)
    @puestoNS.marshal_with(puestoModel) 
    def put(self,id):
        data = puestoNS.payload
        puesto = Puesto.query.get(id)

        if not puesto:
            abort(404, f"El puesto con el ID {id} no existe.")

        puesto.puesto = data["puesto"]
        puesto.estado = data["estado"]
        db.session.commit()
        return puesto

    def delete (self, id):
        puesto = Puesto.query.get(id)

        if not puesto:
            abort(404, f"El puesto con el ID {id} no existe.")

        db.session.delete(puesto)
        db.session.commit()
        return {"message": f"El departamento con ID {id} fue eliminado exitosamente."}, 200

    



