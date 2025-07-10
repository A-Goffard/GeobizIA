<template>
    <div class="contenedor-principal">
        <div v-if="evento">
            <h1>Detalle de: {{ evento.nombre }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Evento</h2>
                <form @submit.prevent="actualizarEvento">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" v-model="evento.nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="tipo">Tipo:</label>
                            <input type="text" id="tipo" v-model="evento.tipo" required>
                        </div>
                        <div class="form-group">
                            <label for="lugar">Lugar:</label>
                            <input type="text" id="lugar" v-model="evento.lugar" required>
                        </div>
                        <div class="form-group">
                            <label for="fecha_comienzo">Fecha Comienzo:</label>
                            <input type="date" id="fecha_comienzo" v-model="evento.fecha_comienzo" required>
                        </div>
                        <div class="form-group">
                            <label for="fecha_final">Fecha Final:</label>
                            <input type="date" id="fecha_final" v-model="evento.fecha_final" required>
                        </div>
                        <div class="form-group">
                            <label for="poblacion">Población:</label>
                            <input type="text" id="poblacion" v-model="evento.poblacion" required>
                        </div>
                        <div class="form-group">
                            <label for="tematica">Temática:</label>
                            <input type="text" id="tematica" v-model="evento.tematica" required>
                        </div>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Evento' }}
                    </button>
                    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                </form>
            </div>

            <!-- Zona de Peligro para Eliminar -->
            <div class="danger-zone">
                <h2>Zona de Peligro</h2>
                <div class="delete-confirmation">
                    <input type="checkbox" id="confirmDelete" v-model="confirmacionEliminar">
                    <label for="confirmDelete">Confirmo que quiero eliminar este evento. Esta acción es irreversible.</label>
                </div>
                <button @click="eliminarEvento" :disabled="!confirmacionEliminar || isDeleting" class="delete-button">
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar Evento Permanentemente' }}
                </button>
                <p v-if="deleteError" class="error-message">{{ deleteError }}</p>
            </div>
        </div>
        <div v-else-if="errorMsg" class="error-container">
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <p>Cargando datos del evento...</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const evento = ref(null);
const isSubmitting = ref(false);
const successMessage = ref('');
const errorMessage = ref('');
const errorMsg = ref('');
const confirmacionEliminar = ref(false);
const isDeleting = ref(false);
const deleteError = ref('');

onMounted(async () => {
    const id = route.params.id;
    await cargarEvento(id);
});

async function cargarEvento(id) {
    try {
        const res = await fetch(`http://localhost:8000/api/eventos/${id}`);
        if (!res.ok) throw new Error('No se pudo cargar el evento.');
        evento.value = await res.json();
    } catch (e) {
        errorMsg.value = e.message;
    }
}

async function actualizarEvento() {
    isSubmitting.value = true;
    successMessage.value = '';
    errorMessage.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/eventos/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(evento.value)
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al actualizar.');
        successMessage.value = result.mensaje || 'Evento actualizado correctamente.';
        
        // Redirigir a la lista de eventos tras actualizar
        setTimeout(() => {
            router.push('/eventos/ver');
        }, 1500); // Esperar 1.5 segundos para que el usuario vea el mensaje de éxito
        
    } catch (e) {
        errorMessage.value = e.message;
    } finally {
        isSubmitting.value = false;
    }
}

async function eliminarEvento() {
    if (!confirmacionEliminar.value) return;
    isDeleting.value = true;
    deleteError.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/eventos/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al eliminar.');
        
        // Mostrar mensaje de éxito y redirigir a la lista de eventos
        alert(result.mensaje || 'Evento eliminado correctamente.');
        router.push('/eventos/ver');

    } catch (e) {
        deleteError.value = e.message;
    } finally {
        isDeleting.value = false;
    }
}
</script>

<style scoped>
.contenedor-principal { 
    max-width: 900px; 
    margin: 0 auto; 
    padding: 7rem 2rem 2rem; 
}

h1 { 
    color: #2c3e50; 
    margin-bottom: 2rem; 
}

h2 { 
    color: #2c3e50; 
    border-bottom: 2px solid #3498db; 
    padding-bottom: 10px; 
    margin-top: 2.5rem; 
    margin-bottom: 1.5rem; 
}

.form-container { 
    background: white; 
    padding: 2rem; 
    border-radius: 8px; 
    box-shadow: 0 4px 15px rgba(0,0,0,0.08); 
    margin-bottom: 2rem; 
}

.form-grid { 
    display: grid; 
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
    gap: 1.5rem; 
}

.form-group { 
    display: flex; 
    flex-direction: column; 
}

label { 
    margin-bottom: 0.5rem; 
    font-weight: bold; 
    color: #555; 
}

input, textarea { 
    padding: 0.8rem; 
    border: 1px solid #ccc; 
    border-radius: 4px; 
    font-size: 1rem; 
}

button { 
    margin-top: 1.5rem; 
    padding: 0.8rem 1.5rem; 
    background-color: #3498db; 
    color: white; 
    border: none; 
    border-radius: 4px; 
    cursor: pointer; 
    font-size: 1rem; 
    transition: background-color 0.3s; 
}

button:hover {
    background-color: #2980b9;
}

button:disabled { 
    background-color: #aaa; 
}

.success-message, .error-message { 
    margin-top: 1rem; 
}

.success-message { 
    color: green; 
}

.error-message { 
    color: red; 
}

.error-container {
    background-color: #fff0f0;
    border: 1px solid #ffcccc;
    border-left: 5px solid #ff4d4d;
    color: #333;
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
}

/* Estilos para la zona de peligro */
.danger-zone {
    border: 2px solid #e74c3c;
    border-radius: 8px;
    padding: 1.5rem;
    margin-top: 2rem;
    background-color: #fbeeee;
}

.danger-zone h2 {
    color: #c0392b;
    margin-top: 0;
    border-bottom-color: #e74c3c;
}

.delete-confirmation {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.delete-confirmation input[type="checkbox"] {
    width: 18px;
    height: 18px;
    margin-right: 10px;
}

.delete-confirmation label {
    color: #c0392b;
    font-weight: bold;
}

.delete-button {
    background-color: #e74c3c;
}

.delete-button:hover {
    background-color: #c0392b;
}

.delete-button:disabled {
    background-color: #f5b7b1;
    cursor: not-allowed;
}
</style>
