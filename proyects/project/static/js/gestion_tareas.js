function guardarCambios(tareaId) {
    // Obtén los datos del formulario
    const estado = document.getElementById(`estado${tareaId}`).value;
    const comentario = document.getElementById(`comentario${tareaId}`).value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Configura la solicitud AJAX
    fetch(`/tareas/actualizar/${tareaId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            estado: estado,
            comentario: comentario
        })
    })
    .then(response => {
        if (response.ok) {
            // Si la respuesta es correcta, muestra un mensaje de éxito y cierra el modal
            const mensajeExito = document.createElement('div');
            mensajeExito.className = 'alert alert-success';
            mensajeExito.textContent = 'Cambios guardados con éxito';
            document.body.appendChild(mensajeExito);

            // Oculta el mensaje después de 3 segundos
            setTimeout(() => mensajeExito.remove(), 3000);

            // Cierra el modal
            const modal = document.querySelector(`#detalleTareaModal${tareaId}`);
            const bootstrapModal = bootstrap.Modal.getInstance(modal);
            bootstrapModal.hide();

            // Actualiza la página
            location.reload();
        } else {
            alert('Hubo un error al guardar los cambios');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al procesar la solicitud');
    });
}

function guardarCambiosdesarrollador(tareaId) {
    // Obtén los datos del formulario
    const estado = document.getElementById(`estado${tareaId}`).value;
    const comentario = document.getElementById(`comentario${tareaId}`).value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Configura la solicitud AJAX
    fetch(`/tareas/actualizar/${tareaId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            estado: estado,
            comentario: comentario
        })
    })
    .then(response => {
        if (response.ok) {
            // Si la respuesta es correcta, muestra un mensaje de éxito y cierra el modal
            const mensajeExito = document.createElement('div');
            mensajeExito.className = 'alert alert-success';
            mensajeExito.textContent = 'Cambios guardados con éxito';
            document.body.appendChild(mensajeExito);

            // Oculta el mensaje después de 3 segundos
            setTimeout(() => mensajeExito.remove(), 3000);

            // Cierra el modal
            const modal = document.querySelector(`#tareaModal`);
            const bootstrapModal = bootstrap.Modal.getInstance(modal);
            bootstrapModal.hide();

            // Actualiza la página
            location.reload();
        } else {
            alert('Hubo un error al guardar los cambios');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al procesar la solicitud');
    });
}
