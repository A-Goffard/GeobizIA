<template>
    <div class="contenedor-principal">
        <h1>Ver Clientes</h1>
        <p>Listado de clientes registrados.</p>
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <div v-if="clientes.length > 0" class="clientes-list">
                <div v-for="cliente in clientes" :key="cliente.id_cliente" class="cliente-card" @click="verDetalle(cliente.id_cliente)">
                    <h3>{{ cliente.razon_social || `${cliente.nombre || ''} ${cliente.apellido || ''}`.trim() || 'Cliente' }}</h3>
                    <p><strong>Tipo:</strong> {{ cliente.tipo || 'No especificado' }}</p>
                    <p v-if="cliente.nif"><strong>NIF:</strong> {{ cliente.nif }}</p>
                    <p v-if="cliente.dni"><strong>DNI:</strong> {{ cliente.dni }}</p>
                    <p v-if="cliente.email"><strong>Email:</strong> {{ cliente.email }}</p>
                    <p v-if="cliente.telefono"><strong>Teléfono:</strong> {{ cliente.telefono }}</p>
                    <p v-if="cliente.fecha_registro"><strong>Fecha Registro:</strong> {{ cliente.fecha_registro }}</p>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>📭 No se encontraron clientes para mostrar.</p>
                <span>Verifica si existen datos en la base de datos o si los filtros aplicados son correctos.</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const clientes = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarClientes()
})

function verDetalle(id) {
    router.push(`/clientes/detalle/${id}`)
}

async function cargarClientes() {
    try {
        errorMsg.value = null;
        const res = await fetch('http://localhost:8000/api/clientes')
        if (res.ok) {
            clientes.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar clientes: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        clientes.value = []
        errorMsg.value = e.message
        console.error('Error cargando clientes:', e)
    }
}
</script>

<style scoped>
.contenedor-principal {
    max-width: 1200px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.contenedor-principalr h1 {
    margin-bottom: 10px;
    font-size: 2.5rem;
}

.contenedor-principal > p {
    margin-bottom: 30px;
    font-size: 1.1rem;
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

.no-data-container {
    background-color: #f0f8ff;
    border: 1px solid #d1e7fd;
    border-left: 5px solid #0d6efd;
    color: #333;
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
    text-align: center;
}

.no-data-container p {
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0 0 10px 0;
}

.no-data-container span {
    font-size: 1rem;
    color: #555;
}

.error-container h2 {
    color: #cc0000;
    margin-top: 0;
}

.clientes-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.cliente-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    cursor: pointer;
}

.cliente-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.cliente-card h3 {
    margin-top: 0;
    color: #333;
    font-size: 1.2rem;
}

.cliente-card p {
    margin-bottom: 8px;
    color: #666;
    font-size: 0.95rem;
}

.cliente-card p:last-child {
    margin-bottom: 0;
}
</style>