<template>
    <div class="contenedor-principal">
        <h1>Ver Empresas</h1>
        <p>Listado de empresas registradas en el sistema.</p>
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <div v-if="empresas.length > 0" class="empresas-list">
                <div v-for="empresa in empresas" :key="empresa.id_empresa" class="empresa-card" @click="verDetalle(empresa.id_empresa)">
                    <h3>{{ empresa.nombre }}</h3>
                    <p><strong>Sector:</strong> {{ empresa.sector }}</p>
                    <p><strong>Ubicación:</strong> {{ empresa.ubicacion }}</p>
                    <p v-if="empresa.logo" class="logo-info">
                        <strong>Logo:</strong> 
                        <img :src="empresa.logo" :alt="empresa.nombre" class="empresa-logo" />
                    </p>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>🏢 No se encontraron empresas para mostrar.</p>
                <span>Verifica si existen datos en la base de datos o crea una nueva empresa.</span>
            </div>
        </div>

        <!-- Botón flotante para crear nueva empresa -->
        <div class="floating-action">
            <router-link to="/empresas/crear" class="fab-button" title="Crear Nueva Empresa">
                +
            </router-link>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const empresas = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarEmpresas()
})

function verDetalle(id) {
    router.push(`/empresas/detalle/${id}`)
}

async function cargarEmpresas() {
    try {
        errorMsg.value = null;
        const res = await fetch('http://localhost:8000/api/empresas')
        if (res.ok) {
            empresas.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar empresas: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        empresas.value = []
        errorMsg.value = e.message
        console.error('Error cargando empresas:', e)
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

.empresas-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.empresa-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    cursor: pointer;
}

.empresa-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.empresa-card h3 {
    margin-top: 0;
    color: #333;
    font-size: 1.3rem;
}

.empresa-card p {
    margin-bottom: 10px;
    color: #666;
    line-height: 1.4;
}

.empresa-logo {
    max-height: 30px;
    max-width: 100px;
    object-fit: contain;
    margin-left: 10px;
    vertical-align: middle;
}

.floating-action {
    position: fixed;
    bottom: 30px;
    right: 30px;
}

.fab-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    background: #007bff;
    color: white;
    border-radius: 50%;
    text-decoration: none;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
    transition: all 0.3s ease;
}

.fab-button:hover {
    background: #0056b3;
    transform: scale(1.1);
    box-shadow: 0 6px 16px rgba(0, 123, 255, 0.4);
}
</style>
