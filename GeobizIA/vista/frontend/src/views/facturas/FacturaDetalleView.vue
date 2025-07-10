<template>
    <div class="contenedor-principal">
        <div v-if="factura">
            <h1>Detalle de: Factura #{{ factura.numero_factura }}</h1>
            
            <!-- Formulario de Edición -->
            <div class="form-container">
                <h2>Editar Factura</h2>
                <form @submit.prevent="actualizarFactura">
                    <!-- Campos del formulario -->
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="id_cliente">ID Cliente:</label>
                            <input type="number" id="id_cliente" v-model.number="factura.id_cliente" required>
                        </div>
                        <div class="form-group">
                            <label for="fecha_facturacion">Fecha Facturación:</label>
                            <input type="date" id="fecha_facturacion" v-model="factura.fecha_facturacion" required>
                        </div>
                        <div class="form-group">
                            <label for="fecha_vencimiento">Fecha Vencimiento:</label>
                            <input type="date" id="fecha_vencimiento" v-model="factura.fecha_vencimiento" required>
                        </div>
                        <div class="form-group">
                            <label for="concepto">Concepto:</label>
                            <input type="text" id="concepto" v-model="factura.concepto" required>
                        </div>
                        <div class="form-group">
                            <label for="responsable">Responsable:</label>
                            <input type="text" id="responsable" v-model="factura.responsable" required>
                        </div>
                        <div class="form-group">
                            <label for="iva">IVA (%):</label>
                            <input type="number" step="0.01" id="iva" v-model.number="factura.iva" required min="0" max="100">
                        </div>
                        <div class="form-group">
                            <label for="base_imponible">Base Imponible (€):</label>
                            <input type="number" step="0.01" id="base_imponible" v-model.number="factura.base_imponible" required min="0">
                        </div>
                        <div class="form-group">
                            <label for="coste_total">Coste Total (€):</label>
                            <input type="number" step="0.01" id="coste_total" v-model.number="factura.coste_total" required min="0">
                        </div>
                        <div class="form-group">
                            <label for="numero_factura">Número Factura:</label>
                            <input type="text" id="numero_factura" v-model="factura.numero_factura" required>
                        </div>
                        <div class="form-group">
                            <label for="tipo_pago">Tipo de Pago:</label>
                            <select id="tipo_pago" v-model="factura.tipo_pago" required>
                                <option value="">Selecciona tipo de pago</option>
                                <option value="efectivo">Efectivo</option>
                                <option value="transferencia">Transferencia</option>
                                <option value="tarjeta">Tarjeta</option>
                                <option value="cheque">Cheque</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="irpf">IRPF (%):</label>
                            <input type="number" step="0.01" id="irpf" v-model.number="factura.irpf" required min="0" max="100">
                        </div>
                    </div>
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Actualizando...' : 'Actualizar Factura' }}
                    </button>
                    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
                </form>
            </div>

            <!-- Zona de Peligro para Eliminar -->
            <div class="danger-zone">
                <h2>🚨 Zona de Peligro</h2>
                <p>Esta acción no se puede deshacer. La factura será eliminada permanentemente.</p>
                
                <div class="delete-confirmation">
                    <label class="checkbox-container">
                        <input type="checkbox" v-model="deleteConfirmed">
                        <span class="checkmark"></span>
                        Confirmo que deseo eliminar permanentemente la factura "{{ factura.numero_factura }}"
                    </label>
                </div>
                
                <button 
                    @click="eliminarFactura" 
                    class="delete-button" 
                    :disabled="!deleteConfirmed || isDeleting"
                >
                    {{ isDeleting ? 'Eliminando...' : 'Eliminar Factura' }}
                </button>
            </div>

            <!-- Navegación -->
            <div class="navigation">
                <router-link to="/facturas/ver" class="back-button">← Volver a la lista de facturas</router-link>
            </div>
        </div>

        <!-- Estado de carga -->
        <div v-else-if="loading" class="loading-container">
            <p>🔄 Cargando detalles de la factura...</p>
        </div>

        <!-- Error de carga -->
        <div v-else class="error-container">
            <h2>⚠️ Error al cargar la factura</h2>
            <p>{{ loadError }}</p>
            <router-link to="/facturas/ver" class="back-button">← Volver a la lista de facturas</router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const factura = ref(null)
const loading = ref(true)
const loadError = ref('')
const successMessage = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)
const isDeleting = ref(false)
const deleteConfirmed = ref(false)

onMounted(async () => {
    await cargarFactura()
})

async function cargarFactura() {
    try {
        loading.value = true
        loadError.value = ''
        
        const id = route.params.id
        const response = await fetch(`http://localhost:8000/api/facturas/${id}`)
        
        if (!response.ok) {
            throw new Error(`Error ${response.status}: ${response.statusText}`)
        }
        
        factura.value = await response.json()
    } catch (error) {
        loadError.value = error.message || 'Error al cargar la factura'
        console.error('Error cargando factura:', error)
    } finally {
        loading.value = false
    }
}

async function actualizarFactura() {
    try {
        isSubmitting.value = true
        successMessage.value = ''
        errorMessage.value = ''

        const response = await fetch(`http://localhost:8000/api/facturas/${factura.value.id_factura}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                id_cliente: factura.value.id_cliente,
                fecha_facturacion: factura.value.fecha_facturacion,
                fecha_vencimiento: factura.value.fecha_vencimiento,
                concepto: factura.value.concepto,
                responsable: factura.value.responsable,
                iva: factura.value.iva,
                coste_total: factura.value.coste_total,
                base_imponible: factura.value.base_imponible,
                numero_factura: factura.value.numero_factura,
                tipo_pago: factura.value.tipo_pago,
                irpf: factura.value.irpf
            })
        })

        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.detail || `Error del servidor: ${response.status}`)
        }

        successMessage.value = 'Factura actualizada correctamente'
    } catch (error) {
        errorMessage.value = error.message || 'Error al actualizar la factura'
        console.error('Error actualizando factura:', error)
    } finally {
        isSubmitting.value = false
    }
}

async function eliminarFactura() {
    if (!deleteConfirmed.value) {
        errorMessage.value = 'Debe confirmar la eliminación'
        return
    }

    try {
        isDeleting.value = true
        errorMessage.value = ''

        const response = await fetch(`http://localhost:8000/api/facturas/${factura.value.id_factura}`, {
            method: 'DELETE'
        })

        if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.detail || `Error del servidor: ${response.status}`)
        }

        // Redirigir a la lista después de eliminar
        router.push('/facturas/ver')
    } catch (error) {
        errorMessage.value = error.message || 'Error al eliminar la factura'
        console.error('Error eliminando factura:', error)
    } finally {
        isDeleting.value = false
    }
}
</script>

<style scoped>
.contenedor-principal {
    max-width: 1000px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.contenedor-principal h1 {
    margin-bottom: 30px;
    font-size: 2.5rem;
    color: #2c3e50;
}

.form-container {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
}

.form-container h2 {
    margin-bottom: 1.5rem;
    color: #34495e;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 10px;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #34495e;
}

.form-group input,
.form-group select {
    padding: 0.75rem;
    border: 2px solid #e9ecef;
    border-radius: 5px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

button[type="submit"] {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    min-width: 200px;
}

button[type="submit"]:hover:not(:disabled) {
    background: linear-gradient(135deg, #2980b9, #1abc9c);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

button[type="submit"]:disabled {
    background: #bdc3c7;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.danger-zone {
    background: #fff5f5;
    border: 2px solid #feb2b2;
    border-radius: 10px;
    padding: 2rem;
    margin: 30px 0;
}

.danger-zone h2 {
    color: #c53030;
    margin-bottom: 1rem;
}

.danger-zone p {
    color: #742a2a;
    margin-bottom: 1.5rem;
}

.delete-confirmation {
    margin: 20px 0;
}

.checkbox-container {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-size: 1rem;
    color: #742a2a;
    user-select: none;
}

.checkbox-container input[type="checkbox"] {
    margin-right: 10px;
    transform: scale(1.2);
}

.delete-button {
    background: linear-gradient(135deg, #e74c3c, #c0392b);
    color: white;
    padding: 1rem 2rem;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.delete-button:hover:not(:disabled) {
    background: linear-gradient(135deg, #c0392b, #a93226);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(231, 76, 60, 0.3);
}

.delete-button:disabled {
    background: #bdc3c7;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.navigation {
    margin-top: 30px;
    text-align: center;
}

.back-button {
    display: inline-block;
    background: #95a5a6;
    color: white;
    padding: 0.75rem 1.5rem;
    text-decoration: none;
    border-radius: 5px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.back-button:hover {
    background: #7f8c8d;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.loading-container,
.error-container {
    text-align: center;
    padding: 3rem;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.error-container {
    background: #fff5f5;
    border: 2px solid #feb2b2;
    color: #742a2a;
}

.success-message {
    color: #27ae60;
    font-weight: 600;
    text-align: center;
    margin-top: 1rem;
    padding: 0.75rem;
    background: #d5f4e6;
    border: 1px solid #27ae60;
    border-radius: 5px;
}

.error-message {
    color: #e74c3c;
    font-weight: 600;
    text-align: center;
    margin-top: 1rem;
    padding: 0.75rem;
    background: #fdf2f2;
    border: 1px solid #e74c3c;
    border-radius: 5px;
}

@media (max-width: 768px) {
    .contenedor-principal {
        padding: 5rem 1rem 1rem 1rem;
    }
    
    .form-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
    
    .contenedor-principal h1 {
        font-size: 2rem;
    }
    
    .form-container {
        padding: 1.5rem;
    }
}
</style>
