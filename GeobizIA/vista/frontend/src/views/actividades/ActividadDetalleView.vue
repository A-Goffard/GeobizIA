<template>
    <div class="contenedor-principal">
        <div v-if="actividad">
            <h1>Detalle de: {{ actividad.nombre }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Actividad</h2>
                <form @submit.prevent="actualizarActividad">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" v-model="actividad.nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="tipo">Tipo:</label>
                            <input type="text" id="tipo" v-model="actividad.tipo" required>
                        </div>
                        <div class="form-group">
                            <label for="responsable">Responsable:</label>
                            <input type="text" id="responsable" v-model="actividad.responsable" required>
                        </div>
                        <div class="form-group">
                            <label for="duracion">Duración:</label>
                            <input type="text" id="duracion" v-model="actividad.duracion" required>
                        </div>
                        <div class="form-group">
                            <label for="coste_economico">Coste (€):</label>
                            <input type="number" step="0.01" id="coste_economico" v-model="actividad.coste_economico" required>
                        </div>
                        <div class="form-group">
                            <label for="facturacion">Facturación (€):</label>
                            <input type="number" step="0.01" id="facturacion" v-model="actividad.facturacion" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="descripcion">Descripción:</label>
                        <textarea id="descripcion" v-model="actividad.descripcion"></textarea>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Actividad' }}
                    </button>
                    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                </form>
            </div>

            <!-- Listado de Actividades Realizadas -->
            <div class="listado-container">
                <h2>Historial de Realización</h2>
                <div v-if="realizadas.length > 0" class="realizadas-lista">
                    <div v-for="item in realizadas" :key="item.id_actividad_realizada" class="realizada-card" @click="abrirModalEdicion(item)">
                        <p><strong>Fecha:</strong> {{ item.fecha }}</p>
                        <p><strong>Asistentes:</strong> {{ item.asistentes ?? 'N/A' }}</p>
                        <p><strong>Coste:</strong> {{ formatCurrency(item.coste_economico) }}</p>
                        <p><strong>Facturación:</strong> {{ formatCurrency(item.facturacion) }}</p>
                        <p v-if="item.observaciones"><strong>Obs:</strong> {{ item.observaciones }}</p>
                    </div>
                </div>
                <div v-else class="no-data-container">
                    <p>Esta actividad aún no se ha realizado.</p>
                </div>
            </div>

            <!-- Zona de Peligro para Eliminar -->
            <div class="danger-zone">
                <h2>Zona de Peligro</h2>
                <div class="delete-confirmation">
                    <input type="checkbox" id="confirmDelete" v-model="confirmacionEliminar">
                    <label for="confirmDelete">Confirmo que quiero eliminar esta actividad. Esta acción es irreversible.</label>
                </div>
                <button @click="eliminarActividad" :disabled="!confirmacionEliminar || isDeleting" class="delete-button">
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar Actividad Permanentemente' }}
                </button>
                <p v-if="deleteError" class="error-message">{{ deleteError }}</p>
            </div>
        </div>
        <div v-else-if="errorMsg" class="error-container">
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <p>Cargando datos de la actividad...</p>
        </div>

        <!-- Modal de Edición -->
        <ActividadRealizadaEditModal
            v-if="registroSeleccionado"
            :actividad-realizada="registroSeleccionado"
            @close="cerrarModalEdicion"
            @updated="onRegistroActualizado"
            @deleted="onRegistroEliminado"
        />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ActividadRealizadaEditModal from '@/components/modals/ActividadRealizadaEditModal.vue';

const route = useRoute();
const router = useRouter();
const actividad = ref(null);
const realizadas = ref([]);
const isSubmitting = ref(false);
const successMessage = ref('');
const errorMessage = ref('');
const errorMsg = ref('');
const confirmacionEliminar = ref(false);
const isDeleting = ref(false);
const deleteError = ref('');
const registroSeleccionado = ref(null);

onMounted(async () => {
    const id = route.params.id;
    await cargarActividad(id);
    await cargarRealizadas(id);
});

async function cargarActividad(id) {
    try {
        const res = await fetch(`http://localhost:8000/api/actividades/${id}`);
        if (!res.ok) throw new Error('No se pudo cargar la actividad.');
        actividad.value = await res.json();
    } catch (e) {
        errorMsg.value = e.message;
    }
}

async function cargarRealizadas(id) {
    try {
        const res = await fetch(`http://localhost:8000/api/actividades_realizadas/por_actividad/${id}`);
        if (!res.ok) throw new Error('No se pudo cargar el historial.');
        realizadas.value = await res.json();
    } catch (e) {
        // No mostrar error si solo falla el historial
        console.error(e.message);
    }
}

async function actualizarActividad() {
    isSubmitting.value = true;
    successMessage.value = '';
    errorMessage.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/actividades/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(actividad.value)
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al actualizar.');
        successMessage.value = result.mensaje;
    } catch (e) {
        errorMessage.value = e.message;
    } finally {
        isSubmitting.value = false;
    }
}

function abrirModalEdicion(registro) {
    registroSeleccionado.value = registro;
}

function cerrarModalEdicion() {
    registroSeleccionado.value = null;
}

function onRegistroActualizado(registroActualizado) {
    const index = realizadas.value.findIndex(r => r.id_actividad_realizada === registroActualizado.id_actividad_realizada);
    if (index !== -1) {
        realizadas.value[index] = registroActualizado;
    }
    cerrarModalEdicion();
}

function onRegistroEliminado(idEliminado) {
    realizadas.value = realizadas.value.filter(r => r.id_actividad_realizada !== idEliminado);
    cerrarModalEdicion();
}

async function eliminarActividad() {
    if (!confirmacionEliminar.value) return;
    isDeleting.value = true;
    deleteError.value = '';
    try {
        const id = route.params.id;
        const response = await fetch(`http://localhost:8000/api/actividades/${id}`, {
            method: 'DELETE'
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.detail || 'Error al eliminar.');
        
        // Redirigir a la lista de actividades tras eliminar
        router.push('/actividades');

    } catch (e) {
        deleteError.value = e.message;
    } finally {
        isDeleting.value = false;
    }
}

function formatCurrency(value) {
    if (value === null || value === undefined) return '0.00€';
    return new Intl.NumberFormat('es-ES', { style: 'currency', currency: 'EUR' }).format(value);
}
</script>

<style scoped>
.contenedor-principal { max-width: 900px; margin: 0 auto; padding: 7rem 2rem 2rem; }
h1 { color: #2c3e50; margin-bottom: 2rem; }
h2 { color: #2c3e50; border-bottom: 2px solid var(--lightgreen); padding-bottom: 10px; margin-top: 2.5rem; margin-bottom: 1.5rem; }
.form-container, .listado-container { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-bottom: 2rem; }
.form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; }
.form-group { display: flex; flex-direction: column; }
label { margin-bottom: 0.5rem; font-weight: bold; color: #555; }
input, textarea { padding: 0.8rem; border: 1px solid #ccc; border-radius: 4px; font-size: 1rem; }
textarea { min-height: 100px; resize: vertical; }
button { margin-top: 1.5rem; padding: 0.8rem 1.5rem; background-color: var(--green); color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 1rem; transition: background-color 0.3s; }
button:disabled { background-color: #aaa; }
.success-message, .error-message { margin-top: 1rem; }
.success-message { color: green; }
.error-message { color: red; }
.realizadas-lista { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.realizada-card { background: #f8f9fa; padding: 1rem; border-radius: 5px; border-left: 3px solid var(--shoftgreen); cursor: pointer; transition: background-color 0.2s; }
.realizada-card:hover { background-color: #e9ecef; }
.realizada-card p { margin: 0.5rem 0; font-size: 0.9rem; }
.no-data-container { text-align: center; padding: 1rem; background-color: #f0f8ff; border-radius: 5px; }

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
.delete-button:disabled {
    background-color: #f5b7b1;
    cursor: not-allowed;
}
</style>
