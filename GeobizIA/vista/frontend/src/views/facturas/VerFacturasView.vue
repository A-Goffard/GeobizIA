<template>
    <div class="contenedor-principal">
        <h1>Ver Facturas</h1>
        <p>Listado de facturas registradas en el sistema.</p>
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <div v-if="facturas.length > 0" class="facturas-list">
                <div v-for="factura in facturas" :key="factura.id_factura" class="factura-card" @click="verDetalle(factura.id_factura)">
                    <h3>Factura #{{ factura.numero_factura }}</h3>
                    <p><strong>Cliente ID:</strong> {{ factura.id_cliente }}</p>
                    <p><strong>Concepto:</strong> {{ factura.concepto }}</p>
                    <p><strong>Coste Total:</strong> {{ formatCurrency(factura.coste_total) }}</p>
                    <p><strong>Fecha Facturación:</strong> {{ formatDate(factura.fecha_facturacion) }}</p>
                    <p><strong>Fecha Vencimiento:</strong> {{ formatDate(factura.fecha_vencimiento) }}</p>
                    <p><strong>Responsable:</strong> {{ factura.responsable }}</p>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>📄 No se encontraron facturas para mostrar.</p>
                <span>Verifica si existen datos en la base de datos o crea una nueva factura.</span>
            </div>
        </div>

        <!-- Botón flotante para crear nueva factura -->
        <div class="floating-action">
            <router-link to="/facturas/crear" class="fab-button" title="Crear Nueva Factura">
                +
            </router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const facturas = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarFacturas()
})

function verDetalle(id) {
    router.push(`/facturas/detalle/${id}`)
}

function formatCurrency(amount) {
    if (amount === null || amount === undefined) return 'N/A'
    return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'EUR'
    }).format(amount)
}

function formatDate(dateString) {
    if (!dateString) return 'N/A'
    try {
        return new Date(dateString).toLocaleDateString('es-ES')
    } catch {
        return dateString
    }
}

async function cargarFacturas() {
    try {
        errorMsg.value = null;
        const res = await fetch('http://localhost:8000/api/facturas')
        if (res.ok) {
            facturas.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar facturas: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        facturas.value = []
        errorMsg.value = e.message
        console.error('Error cargando facturas:', e)
    }
}
</script>

<style scoped>
.contenedor-principal {
    max-width: 1200px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.contenedor-principal h1 {
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

.facturas-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    margin-bottom: 80px;
}

.factura-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    cursor: pointer;
}

.factura-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    border-color: #3498db;
}

.factura-card h3 {
    margin: 0 0 15px 0;
    color: #2c3e50;
    font-size: 1.3rem;
    border-bottom: 2px solid #ecf0f1;
    padding-bottom: 10px;
}

.factura-card p {
    margin: 8px 0;
    color: #555;
    line-height: 1.4;
}

.factura-card strong {
    color: #34495e;
    font-weight: 600;
}

.floating-action {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
}

.fab-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    border-radius: 50%;
    text-decoration: none;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
    transition: all 0.3s ease;
}

.fab-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 20px rgba(52, 152, 219, 0.6);
    background: linear-gradient(135deg, #2980b9, #1abc9c);
}

@media (max-width: 768px) {
    .contenedor-principal {
        padding: 5rem 1rem 1rem 1rem;
    }

    .facturas-list {
        grid-template-columns: 1fr;
        gap: 15px;
    }

    .contenedor-principal h1 {
        font-size: 2rem;
    }

    .fab-button {
        width: 50px;
        height: 50px;
        font-size: 20px;
    }

    .floating-action {
        bottom: 20px;
        right: 20px;
    }
}
</style>
