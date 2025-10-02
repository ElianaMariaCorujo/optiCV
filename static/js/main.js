// Este código se ejecuta cuando la página se ha cargado por completo
document.addEventListener('DOMContentLoaded', function() {
    
    // Busca el botón "Añadir experiencia"
    const addButton = document.getElementById('agregar-experiencia');
    
    // Busca el contenedor donde se añadirán los nuevos bloques
    const container = document.getElementById('experiencia-container');
    
    let experienceCount = 1;

    // Escucha los clics en el botón
    addButton.addEventListener('click', function() {
        experienceCount++; // Aumenta el contador para tener nombres únicos

        // Crea un nuevo div para el bloque de experiencia
        const newBlock = document.createElement('div');
        newBlock.classList.add('experiencia-bloque');
        
        // Este es el HTML para los nuevos campos
        newBlock.innerHTML = `
            <label for="cargo${experienceCount}">Cargo:</label><br>
            <input type="text" id="cargo${experienceCount}" name="cargo${experienceCount}"><br><br>
            
            <label for="empresa${experienceCount}">Empresa:</label><br>
            <input type="text" id="empresa${experienceCount}" name="empresa${experienceCount}"><br><br>
            
            <label for="fecha_inicio_exp${experienceCount}">Fecha de Inicio:</label><br>
            <input type="text" id="fecha_inicio_exp${experienceCount}" name="fecha_inicio_exp${experienceCount}" placeholder="ej: Enero 2020"><br><br>
            
            <label for="fecha_fin_exp${experienceCount}">Fecha de Fin:</label><br>
            <input type="text" id="fecha_fin_exp${experienceCount}" name="fecha_fin_exp${experienceCount}" placeholder="ej: Diciembre 2022 o Actualidad"><br><br>

            <label for="descripcion_exp${experienceCount}">Descripción y Logros:</label><br>
            <textarea id="descripcion_exp${experienceCount}" name="descripcion_exp${experienceCount}" rows="5" cols="60"></textarea><br><br>
            <hr>
        `;

        // Añade el nuevo bloque de campos al contenedor
        container.appendChild(newBlock);
    });
});
// --- Lógica para añadir Formación Académica ---
document.addEventListener('DOMContentLoaded', function() {
    // Esto ya existe, solo añadimos la nueva lógica dentro del mismo evento
    const addFormacionButton = document.getElementById('agregar-formacion');
    const formacionContainer = document.getElementById('formacion-container');
    let formacionCount = 1;

    addFormacionButton.addEventListener('click', function() {
        formacionCount++;

        const newBlock = document.createElement('div');
        newBlock.classList.add('formacion-bloque');
        
        newBlock.innerHTML = `
            <label for="titulo${formacionCount}">Título / Carrera:</label><br>
            <input type="text" id="titulo${formacionCount}" name="titulo${formacionCount}"><br><br>
            
            <label for="institucion${formacionCount}">Institución:</label><br>
            <input type="text" id="institucion${formacionCount}" name="institucion${formacionCount}"><br><br>
            
            <label for="fecha_fin_formacion${formacionCount}">Año de Finalización:</label><br>
            <input type="text" id="fecha_fin_formacion${formacionCount}" name="fecha_fin_formacion${formacionCount}" placeholder="ej: 2024 o En curso"><br><br>
            <hr>
        `;
        formacionContainer.appendChild(newBlock);
    });
});