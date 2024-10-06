from flask_restx import fields
from ext import api

departamentoModel = api.model("Departamento", {
    "id_departamento": fields.Integer,
    "estado": fields.Boolean,
    "departamento": fields.String
})

departamentoPostModel = api.model("DepartamentoPost", {
    "departamento": fields.String(required=True),
    "estado": fields.Boolean(required=True)
})

puestoModel = api.model("Puesto", {
    "id_puesto": fields.Integer,
    "estado": fields.Boolean,
    "puesto": fields.String
})


empleadoModel = api.model("Persona", {
    "id_empleado": fields.Integer,
    "estado": fields.Boolean,
    "nombre": fields.String,
    "apellido": fields.String,
    "direccion": fields.String,
    "fechaNacimiento": fields.Date,
    "departamento": fields.Nested(departamentoModel),  
    "puesto": fields.Nested(puestoModel) 
})
