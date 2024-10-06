from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id_empleado = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean) 
    nombre = db.Column(db.String(200), nullable=False)
    apellido = db.Column(db.String(200), nullable=False)
    direccion = db.Column(db.String(300), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False)
   #Foreing Keys 
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id_departamento'), nullable=False)
    puesto_id = db.Column(db.Integer, db.ForeignKey('puestos.id_puesto'), nullable=False)  
    #Referencia
    departamento = db.relationship('Departamento', backref='empleados')
    puesto = db.relationship('Puesto', backref='empleados')


class Departamento(db.Model):
    __tablename__ = 'departamentos'
    
    id_departamento = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Boolean) 


class Puesto(db.Model):
    __tablename__ = 'puestos'
    
    id_puesto    = db.Column(db.Integer, primary_key=True)
    puesto = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Boolean) 
