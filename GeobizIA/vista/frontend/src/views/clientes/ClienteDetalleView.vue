<template>
    <div class="contenedor-principal">
        <div v-if="cliente">
            <h1>Detalle de: {{ cliente.razon_social || `Cliente ${cliente.id_cliente}` }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Cliente</h2>
                <form @submit.prevent="actualizarCliente">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="id_persona">ID Persona:</label>
                            <input type="number" id="id_persona" v-model="cliente.id_persona" readonly disabled>
                        </div>
                        <div class="form-group">
                            <label for="tipo">Tipo:</label>
                            <select id="tipo" v-model="cliente.tipo">
                                <option value="">Seleccionar tipo</option>
                                <option value="EMPRESA">Empresa</option>
                                <option value="AUTONOMO">Autónomo</option>
                                <option value="PARTICULAR">Particular</option>
                                <option value="ENTIDAD">Entidad</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="razon_social">Razón Social:</label>
                            <input type="text" id="razon_social" v-model="cliente.razon_social">
                        </div>
                        <div class="form-group">
                            <label for="nif">NIF:</label>
                            <input type="text" id="nif" v-model="cliente.nif">
                        </div>
                        <div class="form-group">
                            <label for="fecha_registro">Fecha Registro:</label>
                            <input type="date" id="fecha_registro" v-model="cliente.fecha_registro">
                        </div>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Cliente' }}
                    </button>
                    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                </form>
            </div>

            <!-- Zona de Peligro para Eliminar -->
            <div class="danger-zone">
                <h3>⚠️ Zona de Peligro</h3>
                <p>Esta acción <strong>NO SE PUEDE DESHACER</strong>. El cliente y todos sus datos serán eliminados permanentemente.</p>
                
                <div class="delete-confirmation">
                    <input type="checkbox" id="confirm-delete" v-model="confirmacionEliminar">
                    <label for="confirm-delete">
                        Entiendo que esta acción es irreversible y quiero eliminar este cliente
                    </label>
                </div>
                
                <button 
                    class="delete-button" 
                    @click="eliminarCliente" 
                    :disabled="!confirmacionEliminar || isDeleting"
                >
                    {{ isDeleting ? 'Eliminando...' : '🗑️ Eliminar Cliente Permanentemente' }}
                </button>
                
                <p v-if="deleteError" class="error-message">{{ deleteError }}</p>
            </div>
        </div>
        <div v-else>
            <p v-if="errorMsg">{{ errorMsg }}</p>
            <p v-else>Cargando cliente...</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const cliente = ref(null)
const isSubmitting = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const errorMsg = ref('')
const confirmacionEliminar = ref(false)
const isDeleting = ref(false)
const deleteError = ref('')

onMounted(async () => {
    const id = route.params.id
    await cargarCliente(id)
})

async function cargarCliente(id) {
    try {
        const res = await fetch(`http://localhost:8000/api/clientes/${id}`)
        if (!res.ok) throw new Error('No se pudo cargar el cliente.')
        cliente.value = await res.json()
    } catch (e) {
        errorMsg.value = e.message
    }
}

async function actualizarCliente() {
    isSubmitting.value = true
    successMessage.value = ''
    errorMessage.value = ''
    try {
        const id = route.params.id
        const response = await fetch(`http://localhost:8000/api/clientes/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(cliente.value)
        })
        const result = await response.json()
        if (!response.ok) throw new Error(result.detail || 'Error al actualizar.')
        successMessage.value = result.mensaje || 'Cliente actualizado correctamente.'
        
        // Redirigir a la lista de clientes tras actualizar
        setTimeout(() => {
            router.push('/clientes/ver')
        }, 1500) // Esperar 1.5 segundos para que el usuario vea el mensaje de éxito
        
    } catch (e) {
        errorMessage.value = e.message
    } finally {
        isSubmitting.value = false
    }
}

async function eliminarCliente() {
    if (!confirmacionEliminar.value) return
    isDeleting.value = true
    deleteError.value = ''
    try {
        const id = route.params.id
        const response = await fetch(`http://localhost:8000/api/clientes/${id}`, {
            method: 'DELETE'
        })
        const result = await response.json()
        if (!response.ok) throw new Error(result.detail || 'Error al eliminar.')
        
        // Mostrar mensaje de éxito y redirigir a la lista de clientes
        alert(result.mensaje || 'Cliente eliminado correctamente.')
        router.push('/clientes/ver')

    } catch (e) {
        deleteError.value = e.message
    } finally {
        isDeleting.value = false
    }
}
</script>

<style scoped>
.contenedor-principal { 
    max-width: 900px; 
    margin: 0 auto; 
    padding: 7rem 2rem 2rem; 
}

.form-container {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #333;
}

.form-group input,
.form-group select {
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

.form-group input:focus,
.form-group select:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
}

button {
    background-color: #007bff;
    color: white;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s;
}

button:hover:not(:disabled) {
    background-color: #0056b3;
}

button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
}

.success-message {
    color: #28a745;
    font-weight: bold;
    margin-top: 1rem;
}

.error-message {
    color: #dc3545;
    font-weight: bold;
    margin-top: 1rem;
}

.danger-zone {
    background: #fff5f5;
    border: 1px solid #fed7d7;
    border-radius: 8px;
    padding: 2rem;
    margin-top: 2rem;
}

.danger-zone h3 {
    color: #e53e3e;
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
