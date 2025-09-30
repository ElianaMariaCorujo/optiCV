from flask import Flask

# Creamos la aplicación
app = Flask(__name__)

# Definimos la ruta principal
@app.route('/')
def hola_mundo():
    return '¡Mi app Opti-CV está funcionando!'

# Esto es para poder ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)