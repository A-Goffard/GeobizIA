<template>
    <div class="contenedor-principal">
        <div v-if="empresa">
            <h1>Detalle de: {{ empresa.nombre }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Empresa</h2>
                <form @submit.prevent="actualizarEmpresa">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="nombre">Nombre:</label>
                            <input type="text" id="nombre" v-model="empresa.nombre" required>
                        </div>
                        <div class="form-group">
                            <label for="sector">Sector:</label>
                            <input type="text" id="sector" v-model="empresa.sector" required>
                        </div>
                        <div class="form-group">
                            <label for="ubicacion">Ubicación:</label>
                            <input type="text" id="ubicacion" v-model="empresa.ubicacion" required>
                        </div>
                        <div class="form-group">
                            <label for="logo">Logo (URL):</label>
                            <input type="url" id="logo" v-model="empresa.logo" placeholder="https://...">
                        </div>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Empresa' }}
                    </button>
                    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                </form>
            </div>

            <!-- Zona de Peligro para Eliminar -->
            <div class="danger-zone">
                <h2>🚨 Zona de Peligro</h2>
                <p>Esta acción no se puede deshacer. La empresa será eliminada permanentemente.</p>
                
                <div class="delete-confirmation">
                    <label class="checkbox-container">
                        <input type="checkbox" v-model="deleteConfirmed">
                        <span class="checkmark"></span>
                        Confirmo que deseo eliminar permanentemente la empresa "{{ empresa.nombre }}"
                    </label>
                </div>
                
                <button 
                    @click="eliminarEmpresa" 
                    class="delete-button" 
                    :disabled="!deleteConfirmed || isDeleting"
                >
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar Empresa' }}
                </button>
            </div>

            <!-- Navegación -->
            <div class="navigation">
                <router-link to="/empresas/ver" class="back-button">← Volver a la lista de empresas</router-link>
            </div>
        </div>

        <!-- Estado de carga -->
        <div v-else-if="loading" class="loading-container">
            <p>🔄 Cargando detalles de la empresa...</p>
        </div>

        <!-- Error de carga -->
        <div v-else class="error-container">
            <h2>⚠️ Error al cargar la empresa</h2>
            <p>{{ loadError }}</p>
            <router-link to="/empresas/ver" class="back-button">← Volver a la lista de empresas</router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const empresa = ref(null)
const loading = ref(true)
const loadError = ref('')
const successMessage = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)
const isDeleting = ref(false)
const deleteConfirmed = ref(false)

onMounted(async () => {
    await cargarEmpresa()
})

async function cargarEmpresa() {
    try {
        loading.value = true
        loadError.value = ''
        
        const id = route.params.id
        const response = await fetch(`http://localhost:8000/api/empresas/${id}`)
        
        if (response.ok) {
            empresa.value = await response.json()
        } else {
            throw new Error(`Error ${response.status}: ${response.statusText}`)
        }
    } catch (error) {
        loadError.value = error.message
        console.error('Error al cargar empresa:', error)
    } finally {
        loading.value = false
    }
}

async function actualizarEmpresa() {
    try {
        isSubmitting.value = true
        errorMessage.value = ''
        successMessage.value = ''
        
        const response = await fetch(`http://localhost:8000/api/empresas/${empresa.value.id_empresa}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nombre: empresa.value.nombre,
                sector: empresa.value.sector,
                ubicacion: empresa.value.ubicacion,
                logo: empresa.value.logo || null
            })
        })
        
        if (response.ok) {
            const data = await response.json()
            successMessage.value = data.mensaje || 'Empresa actualizada exitosamente'
            // Actualizar datos locales con la respuesta
            if (data.empresa) {
                empresa.value = { ...empresa.value, ...data.empresa }
            }
        } else {
            const data = await response.json()
            errorMessage.value = data.detail || 'Error al actualizar la empresa'
        }
    } catch (error) {
        errorMessage.value = 'Error de conexión. Intente nuevamente.'
        console.error('Error:', error)
    } finally {
        isSubmitting.value = false
    }
}

async function eliminarEmpresa() {
    try {
        isDeleting.value = true
        
        const response = await fetch(`http://localhost:8000/api/empresas/${empresa.value.id_empresa}`, {
            method: 'DELETE'
        })
        
        if (response.ok) {
            // Redireccionar a la lista con mensaje de éxito
            router.push({
                path: '/empresas/ver',
                query: { mensaje: `Empresa "${empresa.value.nombre}" eliminada exitosamente` }
            })
        } else {
            const data = await response.json()
            errorMessage.value = data.detail || 'Error al eliminar la empresa'
        }
    } catch (error) {
        errorMessage.value = 'Error de conexión al eliminar empresa'
        console.error('Error:', error)
    } finally {
        isDeleting.value = false
    }
}
</script>

<style scoped>
.contenedor-principal {
    max-width: 800px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.contenedor-principal h1 {
    margin-bottom: 30px;
    font-size: 2.5rem;
    color: #333;
}

.form-container {
    background: #f8f9fa;
    padding: 30px;
    border-radius: 8px;
    margin-bottom: 30px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-container h2 {
    margin-top: 0;
    margin-bottom: 20px;
    color: #333;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #333;
}

.form-group input {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

.form-group input:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 2px rgba(0,123,255,0.25);
}

button[type="submit"] {
    background: #007bff;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.2s;
}

button[type="submit"]:hover:not(:disabled) {
    background: #0056b3;
}

button[type="submit"]:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

.success-message {
    background: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 4px;
    margin-top: 15px;
    border: 1px solid #c3e6cb;
}

.error-message {
    background: #f8d7da;
    color: #721c24;
    padding: 10px;
    border-radius: 4px;
    margin-top: 15px;
    border: 1px solid #f1b0b7;
}

.danger-zone {
    background: #fff5f5;
    border: 2px solid #fed7d7;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;
}

.danger-zone h2 {
    color: #e53e3e;
    margin-top: 0;
    margin-bottom: 15px;
}

.danger-zone p {
    color: #744210;
    margin-bottom: 20px;
}

.delete-confirmation {
    margin-bottom: 20px;
}

.checkbox-container {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-size: 14px;
    color: #333;
    margin-bottom: 15px;
}

.checkbox-container input[type="checkbox"] {
    margin-right: 10px;
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.checkbox-container:hover {
    color: #e53e3e;
}

.delete-button {
    background: #dc3545;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.2s;
}

.delete-button:hover:not(:disabled) {
    background: #c82333;
}

.delete-button:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

.navigation {
    margin-top: 30px;
}

.back-button {
    display: inline-block;
    background: #6c757d;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.2s;
}

.back-button:hover {
    background: #545b62;
}

.loading-container {
    text-align: center;
    padding: 50px;
    font-size: 18px;
    color: #666;
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

.error-container h2 {
    color: #cc0000;
    margin-top: 0;
}
</style>
