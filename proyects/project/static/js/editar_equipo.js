
function guardarCambios(tareaId) {
    const estado = document.getElementById(`estado${tareaId}`).value;
    const comentario = document.getElementById(`comentario${tareaId}`).value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch(`/tareas/actualizar/${tareaId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ estado, comentario })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Mostrar un mensaje temporal
            const mensajeExito = document.createElement('div');
            mensajeExito.className = 'alert alert-success';
            mensajeExito.textContent = 'Cambios guardados exitosamente';
            document.body.appendChild(mensajeExito);

            // Ocultar el mensaje después de 3 segundos
            setTimeout(() => mensajeExito.remove(), 3000);

            // Cerrar el modal
            const modal = document.querySelector(`#detalleTareaModal${tareaId}`);
            const bootstrapModal = bootstrap.Modal.getInstance(modal);
            bootstrapModal.hide();
        } else {
            alert('Hubo un error al guardar los cambios');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al guardar los cambios');
    });
}

