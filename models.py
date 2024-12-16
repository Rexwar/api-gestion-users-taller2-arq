from flask_sqlalchemy import SQLAlchemy

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    primer_apellido = db.Column(db.String(50), nullable=False)
    segundo_apellido = db.Column(db.String(50))
    rut = db.Column(db.String(20), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    carrera_id = db.Column(db.Integer, nullable=False)

class Progreso(db.Model):
    __tablename__ = 'progreso'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    asignatura_codigo = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
