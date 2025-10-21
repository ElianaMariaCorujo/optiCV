import os
from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
# --- Configuración de la App ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi-clave-secreta-nadie-la-sabe'

# --- NUEVO: Configuración de Base de Datos (PostgreSQL) ---
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASS', 'probar123') 
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'opticv_db') 

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
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

    # Relaciones
    experiencias = db.relationship('Experiencia', backref='cv', lazy=True, cascade="all, delete-orphan")
    formaciones = db.relationship('Formacion', backref='cv', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        """Serializador: Convierte el objeto CV y sus relaciones a un diccionario."""
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
    descripcion_exp = db.Column(db.Text)
    
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cargo': self.cargo,
            'empresa': self.empresa,
            'fecha_inicio_exp': self.fecha_inicio_exp,
            'fecha_fin_exp': self.fecha_fin_exp,
            'descripcion_exp': self.descripcion_exp
        }

class Formacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    institucion = db.Column(db.String(100))
    fecha_fin_formacion = db.Column(db.String(50))
    
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'institucion': self.institucion,
            'fecha_fin_formacion': self.fecha_fin_formacion
        }


# --- NUEVO: Rutas de la API ---

# ELIMINADA: @app.route('/', ...) ya no sirve HTML

@app.route('/api/v1/cv', methods=['POST'])
def create_cv():
    """
    Crea un nuevo CV. Espera recibir un JSON.
    """
    data = request.json
    
    # Validación simple (en un proyecto más grande, usa Marshmallow o Pydantic)
    if not data or 'nombre_completo' not in data or 'email' not in data:
        return jsonify({"error": "Faltan datos (nombre_completo, email)"}), 400

    # Creamos el objeto CV principal
    nuevo_cv = CV(
        nombre_completo=data.get('nombre_completo'),
        email=data.get('email'),
        telefono=data.get('telefono'),
        ubicacion=data.get('ubicacion'),
        linkedin=data.get('linkedin'),
        github=data.get('github'),
        resumen=data.get('resumen'),
        habilidades=data.get('habilidades'),
        idiomas_certs=data.get('idiomas_certs')
    )
    db.session.add(nuevo_cv)
   
    db.session.flush()

    # Creamos las experiencias asociadas
    if 'experiencias' in data:
        for exp_data in data['experiencias']:
            exp = Experiencia(
                cargo=exp_data.get('cargo'),
                empresa=exp_data.get('empresa'),
            
                cv_id=nuevo_cv.id # Asociamos al CV
            )
            db.session.add(exp)

    # Creamos las formaciones asociadas
    if 'formaciones' in data:
         for form_data in data['formaciones']:
            form = Formacion(
                titulo=form_data.get('titulo'),
                institucion=form_data.get('institucion'),
                # ... (resto de campos de formación)
                cv_id=nuevo_cv.id # Asociamos al CV
            )
            db.session.add(form)
            
    # Ahora sí, guardamos todo en la base de datos
    db.session.commit()
    
    # Devolvemos el CV recién creado, serializado a JSON
    return jsonify(nuevo_cv.to_dict()), 201 # 201 = Created


@app.route('/api/v1/cv/<int:cv_id>', methods=['GET'])
def get_cv(cv_id):
    """
    Obtiene un CV específico por su ID.
    """
    cv = CV.query.get_or_404(cv_id)
    return jsonify(cv.to_dict())


if __name__ == '__main__':
 
    with app.app_context():
        db.create_all()
        print("Tablas de la base de datos creadas (si no existían).")
        
    app.run(debug=True)