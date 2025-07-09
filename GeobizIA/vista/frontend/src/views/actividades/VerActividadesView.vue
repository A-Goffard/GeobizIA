<template>
    <div class="contenedor-principal">
        <h1>Listado de Actividades</h1>
        <p>Consulta todas las actividades registradas, agrupadas por tipo.</p>
        
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>

        <!-- Sección de Listado de Actividades -->
        <div v-if="!errorMsg">
            <div v-if="actividades.length > 0" class="actividades-section">
                <div v-for="(grupo, tipo) in actividadesPorTipo" :key="tipo" class="tipo-bloque">
                    <h3>{{ tipo }}</h3>
                    <div class="actividades-lista">
                        <div v-for="actividad in grupo" :key="actividad.id_actividad" class="actividad-card" @click="verDetalle(actividad.id_actividad)">
                            <div class="actividad-header">
                                <h4>{{ actividad.nombre }}</h4>
                                <span class="duracion-badge">{{ actividad.duracion }}</span>
                            </div>
                            <div class="actividad-details">
                                <p><strong>Responsable:</strong> {{ actividad.responsable }}</p>
                                <p><strong>Coste:</strong> {{ formatCurrency(actividad.coste_economico) }}</p>
                                <p><strong>Facturación:</strong> {{ formatCurrency(actividad.facturacion) }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>📭 No se encontraron actividades para mostrar.</p>
                <span>Verifica si existen datos en la base de datos.</span>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const actividades = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarActividades()
})

async function cargarActividades() {
    try {
        errorMsg.value = null
        const res = await fetch('http://localhost:8000/api/actividades')
        if (res.ok) {
            actividades.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar actividades: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        actividades.value = []
        errorMsg.value = e.message
        console.error('Error cargando actividades:', e)
    }
}

// Agrupa las actividades por tipo
const actividadesPorTipo = computed(() => {
    const grupos = {}
    for (const act of actividades.value) {
        const tipo = act.tipo || 'Sin tipo'
        if (!grupos[tipo]) grupos[tipo] = []
        grupos[tipo].push(act)
    }
    return grupos
})

function verDetalle(id) {
    router.push(`/actividades/detalle/${id}`)
}

// Función para formatear moneda
function formatCurrency(value) {
    if (value === null || value === undefined) return '0€'
    return new Intl.NumberFormat('es-ES', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: 2
    }).format(value)
}
</script>
<style scoped>
.contenedor-principal {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    padding-top: 7rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 2rem;
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

.contenedor-principal h1 {
    color: #2c3e50;
    margin-bottom: 10px;
    font-size: 2.5rem;
}

.contenedor-principal > p {
    color: #7f8c8d;
    margin-bottom: 30px;
    font-size: 1.1rem;
}

/* Sección de Actividades */
.actividades-section h2 {
    color: #2c3e50;
    margin-bottom: 20px;
    font-size: 2rem;
    border-bottom: 3px solid var(--lightgreen);
    padding-bottom: 10px;
}

.tipo-bloque {
    margin-bottom: 30px;
    background: white;
    border-radius: 12px;
    padding: 25px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    border-left: 5px solid var(--shoftgreen);
}

.tipo-bloque h3 {
    color: #2c3e50;
    margin: 0 0 20px 0;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
}

.tipo-bloque h3:before {
    content: "📋";
    margin-right: 10px;
    font-size: 1.2rem;
}

.actividades-lista {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
}

.actividad-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 20px;
    border-left: 4px solid var(--lightgreen);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    cursor: pointer; /* Añadido para indicar que es clicable */
}

.actividad-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

.actividad-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.actividad-header h4 {
    margin: 0;
    color: #2c3e50;
    font-size: 1.1rem;
    flex: 1;
}

.duracion-badge {
    background: var(--lightgreen);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

.actividad-details p {
    margin: 8px 0;
    color: #5a6c7d;
    font-size: 0.9rem;
}

.actividad-details strong {
    color: #2c3e50;
}

/* Responsive Design */
@media (max-width: 768px) {
    .contenedor-principal {
        padding: 15px;
    }
    
    .contenedor-principal h1 {
        font-size: 2rem;
    }
    
    .actividades-lista {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .contenedor-principal h1 {
        font-size: 1.8rem;
    }
    
    .actividades-section h2 {
        font-size: 1.5rem;
    }
}

/* Animaciones */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.actividades-section,
.actividad-card {
    animation: fadeIn 0.6s ease-out;
}
</style>