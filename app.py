# Importamos Flask y ahora también 'render_template'
from flask import Flask, render_template

# Creamos la aplicación
app = Flask(__name__)

# Definimos la ruta principal
@app.route('/')
def inicio():
    # Ya no devolvemos un texto, sino que "renderizamos" nuestro archivo HTML
    return render_template('index.html')

# Esto es para poder ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
    