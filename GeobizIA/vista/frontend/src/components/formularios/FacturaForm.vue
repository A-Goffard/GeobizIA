<template>
    <div class="contenedor-principal">
        <div class="contact-container">
            <h1>{{ isEditing ? 'Editar Factura' : 'Crear Factura' }}</h1>
            <form @submit.prevent="submitForm">
                <div class="form-grid">
                    <div class="form-group">
                        <label for="id_cliente">ID Cliente:</label>
                        <input type="number" id="id_cliente" v-model.number="formData.id_cliente" required>
                    </div>
                    <div class="form-group">
                        <label for="fecha_facturacion">Fecha Facturación:</label>
                        <input type="date" id="fecha_facturacion" v-model="formData.fecha_facturacion" required>
                    </div>
                    <div class="form-group">
                        <label for="fecha_vencimiento">Fecha Vencimiento:</label>
                        <input type="date" id="fecha_vencimiento" v-model="formData.fecha_vencimiento" required>
                    </div>
                    <div class="form-group">
                        <label for="concepto">Concepto:</label>
                        <input type="text" id="concepto" v-model="formData.concepto" required>
                    </div>
                    <div class="form-group">
                        <label for="responsable">Responsable:</label>
                        <input type="text" id="responsable" v-model="formData.responsable" required>
                    </div>
                    <div class="form-group">
                        <label for="iva">IVA (%):</label>
                        <input type="number" step="0.01" id="iva" v-model.number="formData.iva" required min="0" max="100">
                    </div>
                    <div class="form-group">
                        <label for="base_imponible">Base Imponible (€):</label>
                        <input type="number" step="0.01" id="base_imponible" v-model.number="formData.base_imponible" required min="0">
                    </div>
                    <div class="form-group">
                        <label for="coste_total">Coste Total (€):</label>
                        <input type="number" step="0.01" id="coste_total" v-model.number="formData.coste_total" required min="0">
                    </div>
                    <div class="form-group">
                        <label for="numero_factura">Número Factura:</label>
                        <input type="text" id="numero_factura" v-model="formData.numero_factura" required>
                    </div>
                    <div class="form-group">
                        <label for="tipo_pago">Tipo de Pago:</label>
                        <select id="tipo_pago" v-model="formData.tipo_pago" required>
                            <option value="">Selecciona tipo de pago</option>
                            <option value="efectivo">Efectivo</option>
                            <option value="transferencia">Transferencia</option>
                            <option value="tarjeta">Tarjeta</option>
                            <option value="cheque">Cheque</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="irpf">IRPF (%):</label>
                        <input type="number" step="0.01" id="irpf" v-model.number="formData.irpf" required min="0" max="100">
                    </div>
                </div>
                <div class="center">
                    <button type="submit" :disabled="isSubmitting">
                        {{ isSubmitting ? 'Guardando...' : (isEditing ? 'Actualizar Factura' : 'Guardar Factura') }}
                    </button>
                </div>
                <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
                <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'

// Props
const props = defineProps({
    factura: {
        type: Object,
        default: null
    }
})

// Emits
const emit = defineEmits(['facturaCreada', 'facturaActualizada'])

// Reactive state
const formData = ref({
    id_cliente: '',
    fecha_facturacion: '',
    fecha_vencimiento: '',
    concepto: '',
    responsable: '',
    iva: 21,
    coste_total: '',
    base_imponible: '',
    numero_factura: '',
    tipo_pago: '',
    irpf: 15
})

const successMessage = ref('')
const errorMessage = ref('')
const isSubmitting = ref(false)

// Computed
const isEditing = computed(() => props.factura !== null)

// Watchers
watch(() => props.factura, (newFactura) => {
    if (newFactura) {
        // Cargar datos para edición
        formData.value = {
            id_cliente: newFactura.id_cliente || '',
            fecha_facturacion: newFactura.fecha_facturacion || '',
            fecha_vencimiento: newFactura.fecha_vencimiento || '',
            concepto: newFactura.concepto || '',
            responsable: newFactura.responsable || '',
            iva: newFactura.iva || 21,
            coste_total: newFactura.coste_total || '',
            base_imponible: newFactura.base_imponible || '',
            numero_factura: newFactura.numero_factura || '',
            tipo_pago: newFactura.tipo_pago || '',
            irpf: newFactura.irpf || 15
        }
    }
}, { immediate: true })

// Methods
async function submitForm() {
    try {
        isSubmitting.value = true
        successMessage.value = ''
        errorMessage.value = ''

        // Validaciones básicas
        if (!formData.value.id_cliente || !formData.value.concepto || !formData.value.numero_factura) {
            throw new Error('Todos los campos obligatorios deben estar completos')
        }

        if (isEditing.value) {
            await actualizarFactura()
        } else {
            await crearFactura()
        }
    } catch (error) {
        errorMessage.value = error.message || 'Error inesperado'
        console.error('Error en submitForm:', error)
    } finally {
        isSubmitting.value = false
    }
}

async function crearFactura() {
    // Preparar datos con fechas en formato correcto
    const datosParaEnviar = {
        ...formData.value,
        // Convertir fechas de DD/MM/YYYY a YYYY-MM-DD si es necesario
        fecha_facturacion: convertirFecha(formData.value.fecha_facturacion),
        fecha_vencimiento: convertirFecha(formData.value.fecha_vencimiento)
    }

    const response = await fetch('http://localhost:8000/api/facturas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datosParaEnviar)
    })

    if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || `Error del servidor: ${response.status}`)
    }

    successMessage.value = 'Factura creada correctamente'
    emit('facturaCreada')
    
    // Limpiar formulario
    resetForm()
}

async function actualizarFactura() {
    // Preparar datos con fechas en formato correcto
    const datosParaEnviar = {
        ...formData.value,
        fecha_facturacion: convertirFecha(formData.value.fecha_facturacion),
        fecha_vencimiento: convertirFecha(formData.value.fecha_vencimiento)
    }

    const response = await fetch(`http://localhost:8000/api/facturas/${props.factura.id_factura}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datosParaEnviar)
    })

    if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || `Error del servidor: ${response.status}`)
    }

    successMessage.value = 'Factura actualizada correctamente'
    emit('facturaActualizada')
}

function convertirFecha(fecha) {
    if (!fecha) return fecha
    
    // Si ya está en formato YYYY-MM-DD, devolverla tal como está
    if (fecha.match(/^\d{4}-\d{2}-\d{2}$/)) {
        return fecha
    }
    
    // Si está en formato DD/MM/YYYY, convertir a YYYY-MM-DD
    if (fecha.match(/^\d{2}\/\d{2}\/\d{4}$/)) {
        const [dia, mes, año] = fecha.split('/')
        return `${año}-${mes.padStart(2, '0')}-${dia.padStart(2, '0')}`
    }
    
    // Si es un objeto Date, convertir a string
    if (fecha instanceof Date) {
        return fecha.toISOString().split('T')[0]
    }
    
    return fecha
}

function resetForm() {
    formData.value = {
        id_cliente: '',
        fecha_facturacion: '',
        fecha_vencimiento: '',
        concepto: '',
        responsable: '',
        iva: 21,
        coste_total: '',
        base_imponible: '',
        numero_factura: '',
        tipo_pago: '',
        irpf: 15
    }
}

onMounted(() => {
    // Generar número de factura automático si estamos creando una nueva
    if (!isEditing.value) {
        const fecha = new Date()
        const timestamp = fecha.getTime().toString().slice(-6)
        formData.value.numero_factura = `FAC-${timestamp}`
    }
})
</script>

<style scoped>
.contenedor-principal {
    max-width: 800px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.contact-container {
    background: white;
    border-radius: 10px;
    padding: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.contact-container h1 {
    text-align: center;
    margin-bottom: 2rem;
    /* color: #2c3e50; */
    font-size: 2.5rem;
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

.center {
    text-align: center;
    margin-top: 2rem;
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
    
    .contact-container h1 {
        font-size: 2rem;
    }
}
</style>
