import os
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from generador_pdf import crear_cv_pdf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi-clave-secreta-nadie-la-sabe'

DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASS', 'probar123')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'opticv_db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?client_encoding=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(50))
    ubicacion = db.Column(db.String(100))
    linkedin = db.Column(db.String(100))
    github = db.Column(db.String(100))
    resumen = db.Column(db.Text)
    habilidades = db.Column(db.Text)
    idiomas_certs = db.Column(db.Text)

    experiencias = db.relationship('Experiencia', backref='cv', lazy=True, cascade="all, delete-orphan")
    formaciones = db.relationship('Formacion', backref='cv', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'telefono': self.telefono,
            'ubicacion': self.ubicacion,
            'linkedin': self.linkedin,
            'github': self.github,
            'resumen': self.resumen,
            'habilidades': self.habilidades,
            'idiomas_certs': self.idiomas_certs,
            'experiencias': [exp.to_dict() for exp in self.experiencias],
            'formaciones': [form.to_dict() for form in self.formaciones]
        }

class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(100))
    empresa = db.Column(db.String(100))
    fecha_inicio_exp = db.Column(db.String(50))
    fecha_fin_exp = db.Column(db.String(50))
    descripcion_exp = db.Column