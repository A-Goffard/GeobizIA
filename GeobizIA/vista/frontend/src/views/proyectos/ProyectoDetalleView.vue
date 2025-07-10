<template>
    <div class="contenedor-principal">
        <div v-if="proyecto">
            <h1>Detalle de: {{ proyecto.nombre }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Proyecto</h2>
                <form @submit.prevent="actualizarProyecto">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" v-model="proyecto.nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="estado">Estado:</label>
                            <select id="estado" v-model="proyecto.estado" required>
                                <option value="PLANIFICACION">Planificación</option>
                                <option value="EN_PROGRESO">En Progreso</option>
                                <option value="PAUSADO">Pausado</option>
                                <option value="COMPLETADO">Completado</option>
                                <option value="CANCELADO">Cancelado</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="fecha_inicio">Fecha Inicio:</label>
                            <input type="date" id="fecha_inicio" v-model="proyecto.fecha_inicio">
                        </div>
                        <div class="form-group">
                            <label for="fecha_fin">Fecha Fin:</label>
                            <input type="date" id="fecha_fin" v-model="proyecto.fecha_fin">
                        </div>
                        <div class="form-group">
                            <label for="poblacion">Población:</label>
                            <input type="text" id="poblacion" v-model="proyecto.poblacion">
                        </div>
                        <div class="form-group">
                            <label for="responsable">Responsable:</label>
                            <input type="text" id="responsable" v-model="proyecto.responsable">
                        </div>
                        <div class="form-group">
                            <label for="presupuesto">Presupuesto (€):</label>
                            <input type="number" step="0.01" id="presupuesto" v-model="proyecto.presupuesto">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="descripcion">Descripción:</label>
                        <textarea id="descripcion" v-model="proyecto.descripcion" required></textarea>
                    </div>
                    <div class="form-group">
                        <label for="objetivos">Objetivos:</label>
                        <textarea id="objetivos" v-model="proyecto.objetivos"></textarea>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Proyecto' }}
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
                    <label for="confirmDelete">Confirmo que quiero eliminar este proyecto. Esta acción es irreversible.</label>
                </div>
                <button @click="eliminarProyecto" :disabled="!confirmacionEliminar || isDeleting" class="delete-button">
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar Proyecto Permanentemente' }}
                </button>
                <p v-if="deleteError" class="error-message">{{ deleteError }}</p>
            </div>
        </div>
        <div v-else-if="errorMsg" class="error-container">
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <p>Cargando datos del proyecto...</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const proyecto = ref(null);
const isSubmitting = ref(false);
const successMessage = ref('');
const errorMessage = ref('');
const errorMsg = ref('');
const confirmacionEliminar = ref(false);
const isDeleting = ref(false);
const deleteError = ref('');

onMounted(async () => {
    const id = route.params.id;
    await cargarProyecto(id);
});

async function cargarProyecto(id) {
    try {
        const res = await fetch(`http://localhost:8000/api/proyectos/${id}`);
        if (!res.ok) throw new Error('No se pudo cargar el proyecto.');
        proyecto.value = await res.json();
    } catch (e) {
        errorMsg.value = e.message;
    }
}

async function actualizarProyecto() {
    isSubmitting.value = true;
    successMessage.value = '';
    errorMessage.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/proyectos/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(proyecto.value)
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al actualizar.');
        successMessage.value = result.mensaje || 'Proyecto actualizado correctamente.';
        
        // Redirigir a la lista de proyectos tras actualizar
        setTimeout(() => {
            router.push('/proyectos/ver');
        }, 1500); // Esperar 1.5 segundos para que el usuario vea el mensaje de éxito
        
    } catch (e) {
        errorMessage.value = e.message;
    } finally {
        isSubmitting.value = false;
    }
}

async function eliminarProyecto() {
    if (!confirmacionEliminar.value) return;
    isDeleting.value = true;
    deleteError.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/proyectos/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al eliminar.');
        
        // Mostrar mensaje de éxito y redirigir a la lista de proyectos
        alert(result.mensaje || 'Proyecto eliminado correctamente.');
        router.push('/proyectos/ver');

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
    border-bottom: 2px solid #27ae60; 
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

input, textarea, select { 
    padding: 0.8rem; 
    border: 1px solid #ccc; 
    border-radius: 4px; 
    font-size: 1rem; 
}

textarea { 
    min-height: 100px; 
    resize: vertical; 
}

button { 
    margin-top: 1.5rem; 
    padding: 0.8rem 1.5rem; 
    background-color: #27ae60; 
    color: white; 
    border: none; 
    border-radius: 4px; 
    cursor: pointer; 
    font-size: 1rem; 
    transition: background-color 0.3s; 
}

button:hover {
    background-color: #229954;
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
