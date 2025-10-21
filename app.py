from flask import Flask, render_template, request, flash # 'flash' es nuevo, para enviar mensajes
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional
from generador_pdf import crear_cv_pdf
from flask import make_response

# --- Configuración de la App ---
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mi-clave-secreta-nadie-la-sabe'

# 1. Definimos un sub-formulario para la Experiencia
class ExperienciaForm(FlaskForm):
    cargo = StringField('Cargo')
    empresa = StringField('Empresa')
    fecha_inicio_exp = StringField('Fecha de Inicio')
    fecha_fin_exp = StringField('Fecha de Fin')
    descripcion_exp = TextAreaField('Descripción')

# 2. Definimos un sub-formulario para la Formación
class FormacionForm(FlaskForm):
    titulo = StringField('Título')
    institucion = StringField('Institución')
    fecha_fin_formacion = StringField('Año de Finalización')

# 3. Definimos el Formulario Principal
class CvForm(FlaskForm):
    nombre_completo = StringField('Nombre Completo', validators=[DataRequired(message="Tu nombre es obligatorio.")])
    email = StringField('Email', validators=[DataRequired(), Email(message="Introduce un email válido.")])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    ubicacion = StringField('Ubicación', validators=[DataRequired()])
    
    linkedin = StringField('LinkedIn', validators=[Optional()]) # Opcional
    github = StringField('GitHub', validators=[Optional()])
    
    resumen = TextAreaField('Resumen', validators=[DataRequired(), Length(min=20, message="El resumen debe tener al menos 20 caracteres.")])
    
    # Aquí le decimos que puede recibir una "lista de formularios" de Experiencia y Formación
    experiencias = FieldList(FormField(ExperienciaForm))
    formaciones = FieldList(FormField(FormacionForm))

    habilidades = TextAreaField('Habilidades', validators=[DataRequired()])
    idiomas_certs = TextAreaField('Idiomas y Certificaciones', validators=[DataRequired()])
    
    submit = SubmitField('Generar mi CV')


# --- Rutas de la Aplicación ---

@app.route('/', methods=['GET', 'POST'])
def inicio():
    form = CvForm()
    

if form.validate_on_submit():
    # Si los datos son válidos, los procesamos
    print("¡Formulario validado con éxito!")

    # 1. Obtenemos los datos del formulario validado
    datos = form.data

    # 2. Llamamos a nuestra función para crear el PDF
    buffer_pdf = crear_cv_pdf(datos)

    # 3. Preparamos la respuesta para el navegador
    nombre_archivo = f"CV_{datos['nombre_completo'].replace(' ', '_')}.pdf"

    response = make_response(buffer_pdf.getvalue())
    response.mimetype = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename={nombre_archivo}'

    # 4. Enviamos el PDF al usuario
    return response

elif request.method == 'POST':
        print("Falló la validación")
        # ESTA ES LA LÍNEA NUEVA
        flash('Para generar tu mejor CV debes completar todos los campos.', 'danger')


    return render_template('index.html', form=form)


@app.route('/generar-cv', methods=['POST'])
def generar_cv():
   
    return "Esta ruta está en desuso. El procesamiento se hace en la ruta principal."


if __name__ == '__main__':
    app.run(debug=True)
    