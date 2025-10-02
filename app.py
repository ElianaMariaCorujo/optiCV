# Importamos Flask y ahora también 'render_template'
from flask import Flask, render_template

# Creamos la aplicación
app = Flask(__name__)

# Definimos la ruta principal
@app.route('/')
def inicio():
    # Ya no devolvemos un texto, sino que "renderizamos" nuestro archivo HTML
    return render_template('index.html')
@app.route('/generar-cv', methods=['POST'])
def generar_cv():
    return "Datos recibidos. Revisa la terminal de VS Code para ver la información."
# Esto es para poder ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
    