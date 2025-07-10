<template>
    <div class="general-container">
        <h1>Ver Proyectos</h1>
        <p>Listado de proyectos existentes.</p>
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <div v-if="proyectos.length > 0" class="proyectos-list">
                <div v-for="proyecto in proyectos" :key="proyecto.id_proyecto" class="proyecto-card" @click="verDetalle(proyecto.id_proyecto)">
                    <h3>{{ proyecto.nombre }}</h3>
                    <p><strong>Estado:</strong> {{ formatearEstado(proyecto.estado) }}</p>
                    <p><strong>Descripción:</strong> {{ proyecto.descripcion }}</p>
                    <p v-if="proyecto.fecha_inicio && proyecto.fecha_fin">
                        <strong>Fechas:</strong> {{ proyecto.fecha_inicio }} a {{ proyecto.fecha_fin }}
                    </p>
                    <p v-if="proyecto.responsable">
                        <strong>Responsable:</strong> {{ proyecto.responsable }}
                    </p>
                    <p v-if="proyecto.poblacion">
                        <strong>Ubicación:</strong> {{ proyecto.poblacion }}
                    </p>
                    <p v-if="proyecto.presupuesto">
                        <strong>Presupuesto:</strong> {{ formatearPresupuesto(proyecto.presupuesto) }}
                    </p>
                    <p v-if="proyecto.objetivos" class="objetivos">
                        <strong>Objetivos:</strong> {{ proyecto.objetivos }}
                    </p>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>📭 No se encontraron proyectos para mostrar.</p>
                <span>Verifica si existen datos en la base de datos o si los filtros aplicados son correctos.</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const proyectos = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarProyectos()
})

function verDetalle(id) {
    router.push(`/proyectos/detalle/${id}`)
}

async function cargarProyectos() {
    try {
        errorMsg.value = null;
        const res = await fetch('http://localhost:8000/api/proyectos')
        if (res.ok) {
            proyectos.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar proyectos: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        proyectos.value = []
        errorMsg.value = e.message
        console.error('Error cargando proyectos:', e)
    }
}

function formatearEstado(estado) {
    const estados = {
        'PLANIFICACION': 'Planificación',
        'EN_PROGRESO': 'En Progreso',
        'PAUSADO': 'Pausado',
        'COMPLETADO': 'Completado',
        'CANCELADO': 'Cancelado'
    }
    return estados[estado] || estado
}

function formatearPresupuesto(presupuesto) {
    if (presupuesto) {
        return new Intl.NumberFormat('es-ES', {
            style: 'currency',
            currency: 'EUR'
        }).format(presupuesto)
    }
    return ''
}
</script>

<style scoped>
.general-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.general-container h1 {
    margin-bottom: 10px;
    font-size: 2.5rem;
}

.general-container > p {
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

.proyectos-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.proyecto-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    cursor: pointer;
}

.proyecto-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.proyecto-card h3 {
    margin-top: 0;
    color: #333;
    font-size: 1.3rem;
}

.proyecto-card p {
    margin-bottom: 10px;
    color: #666;
    line-height: 1.4;
}

.objetivos {
    font-size: 0.9rem;
    color: #555;
    border-top: 1px solid #eee;
    padding-top: 10px;
    margin-top: 15px;
}

.objetivos strong {
    color: #333;
}
</style>
