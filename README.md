# Opti-CV 📄

Una aplicación web de arquitectura desacoplada (API + Cliente) diseñada para guardar datos de CVs y generar documentos PDF profesionales optimizados para ATS.

## El Problema que Resolvemos

En el mercado laboral actual, más del 75% de los CVs son descartados por sistemas automáticos (ATS). Opti-CV permite a los usuarios guardar su información profesional y generar un documento limpio, estructurado y 100% compatible con ATS en cualquier momento.

## Funcionalidades Clave 🚀

* **Arquitectura API REST:** Un back-end robusto en Flask que gestiona los datos.
* **Cliente Front-end Ligero:** Una interfaz de usuario (UI) en HTML/CSS/JS que consume la API.
* **Persistencia de Datos:** Toda la información se almacena de forma segura en una base de datos **PostgreSQL**.
* **Generación de PDF bajo demanda:** Los usuarios pueden descargar una versión en PDF de su CV guardado en cualquier momento.
* **(Próximamente) IA para generar texto profesional.**

## Stack Tecnológico 🛠️

* **Back-end (API):**
    * Python 3
    * Flask
    * Flask-SQLAlchemy (ORM)
    * PostgreSQL (Base de Datos)
    * ReportLab (Generación de PDF)

* **Front-end (Cliente):**
    * HTML5
    * CSS3
    * JavaScript (nativo) con `fetch` API

## Cómo Empezar (Instalación)

Este proyecto requiere que tanto el Back-end (Flask) como la Base de Datos (PostgreSQL) estén configurados y en ejecución.

### 1. Configuración de la Base de Datos

1.  Asegúrate de tener **PostgreSQL** instalado y un servidor corriendo.
2.  Crea un nuevo usuario (ej: `postgres`) y una nueva base de datos (ej: `opticv_db`).
3.  **Importante:** La aplicación buscará la base de datos usando las credenciales en `app.py`. Asegúrate de que coincidan con tu configuración local.

### 2. Configuración del Entorno de Python

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/ElianaMariaCorujo/optiCV.git](https://github.com/ElianaMariaCorujo/optiCV.git)
    cd optiCV
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    python app.py
    ```
    *Al arrancar, el servidor intentará conectarse a la base de datos y creará las tablas (`¡Tablas listas!`).*

5.  Abre tu navegador y ve a `http://127.0.0.1:5000`

## Uso (Flujo de la API)

1.  El usuario abre `http://127.0.0.1:5000` y el servidor Flask le entrega el `index.html`.
2.  El usuario rellena el formulario y presiona "Guardar CV".
3.  El JavaScript del front-end captura los datos, los convierte a **JSON** y los envía con `fetch` a la API (`POST /api/v1/cv`).
4.  El back-end (Flask) recibe el JSON, valida los datos y los guarda en la base de datos PostgreSQL.
5.  La API responde al front-end con un JSON del CV recién creado, incluyendo su nuevo `id`.
6.  El front-end muestra un enlace de descarga para el PDF (`/api/v1/cv/<id>/pdf`).
7.  Al hacer clic, el navegador pide esa ruta. El back-end busca el CV en la base de datos, genera el PDF con `ReportLab` y lo envía como una descarga.áticamente.
