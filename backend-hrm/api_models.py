from flask_restx import fields
from ext import api

#Departamento Model Data#
departamentoModel = api.model("Departamento", {
    "id_departamento": fields.Integer,
    "estado": fields.Boolean,
    "departamento": fields.String
})

departamentoPostModel = api.model("DepartamentoPost", {
    "departamento": fields.String(required=True),
    "estado": fields.Boolean(required=True)
})


#Puesto Model Data#
puestoModel = api.model("Puesto", {
    "id_puesto": fields.Integer,
    "estado": fields.Boolean,
    "puesto": fields.String
})

puestoPostModel = api.model("PuestoPost", {
    "puesto": fields.String(required=True),
    "estado": fields.Boolean(required=True)
})

#Empleado Model Data#
empleadoModel = api.model("Empleado", {
    "id_empleado": fields.Integer,
    "estado": fields.Boolean,
    "nombre": fields.String,
    "apellido": fields.String,
    "direccion": fields.String,
    "fechaNacimiento": fields.Date,
    "departamento": fields.Nested(departamentoModel),  
    "puesto": fields.Nested(puestoModel) 
})

empleadoPostModel = api.model("EmpleadoPost", {
    "estado": fields.Boolean,
    "nombre": fields.String,
    "apellido": fields.String,
    "direccion": fields.String,
    "fechaNacimiento": fields.Date,
    "departamento_id": fields.Integer(required=True), 
    "puesto_id": fields.Integer(required=True)      
})
