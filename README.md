# Opti-CV 📄✨

Una aplicación web minimalista y potente diseñada para crear CVs profesionales que están optimizados para superar los Sistemas de Seguimiento de Candidatos (ATS) utilizados por los departamentos de Recursos Humanos.

## El Problema que Resolvemos

En el mercado laboral actual, más del 75% de los CVs son descartados por sistemas automáticos (ATS) antes de que un ser humano los vea. Esto sucede por problemas de formato, falta de palabras clave o diseños incompatibles. **Opti-CV** soluciona este problema generando un documento limpio, estructurado y rico en contenido relevante.

## Funcionalidades Clave 🚀

* **Formulario Guiado:** Un formulario web intuitivo que te pide toda la información necesaria paso a paso.
* **Generación de PDF al Instante:** Descarga tu CV en formato PDF, el estándar de la industria.
* **Diseño 100% Compatible con ATS:** Plantilla de una sola columna, fuentes estándar y estructura limpia para garantizar una lectura perfecta por parte del software.
* **Guía de Contenido:** Incluye consejos y secciones clave para maximizar el impacto de tu perfil.
* **(Próximamente) Analizador de Palabras Clave:** Sugerencias de palabras clave basadas en la descripción de la oferta de trabajo.
* **IA para generar texto profesional.
* **Seguridad de datos.

## Stack Tecnológico 🛠️

* **Back-end:** Python, Flask
* **Generación de PDF:** ReportLab
* **Front-end:** HTML5, CSS3
* **Despliegue (a definir):** Vercel / PythonAnywhere / Heroku

## Cómo Empezar (Instalación)

¿Quieres probar el proyecto en tu máquina local? Sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/optiCV.git](https://github.com/TU_USUARIO/optiCV.git)
    cd optiCV
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows es `venv\Scripts\activate`
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    flask run
    ```

5.  Abre tu navegador y ve a `http://127.0.0.1:5000`

## Uso

1.  Abre la aplicación en tu navegador.
2.  Lee las recomendaciones de la ventana emergente para tener toda tu información a mano.
3.  Rellena cada sección del formulario con tu información profesional.
4.  Haz clic en el botón "Generar CV".
5.  ¡Listo! Tu CV en formato PDF se descargará automáticamente.
