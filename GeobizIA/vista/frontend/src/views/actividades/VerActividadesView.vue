<template>
    <div class="general-container">
        <h1>Vista de Actividades</h1>
        <p>Estadísticas y listado de actividades con análisis visual.</p>
        
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>

        <!-- Sección de Estadísticas con Gráficos -->
        <div v-if="estadisticas && !errorMsg" class="estadisticas-section">
            <h2>📊 Estadísticas de Actividades</h2>
            
            <!-- Tarjetas de Resumen -->
            <div class="tarjetas-resumen">
                <div class="tarjeta">
                    <div class="tarjeta-icon">📋</div>
                    <div class="tarjeta-content">
                        <h3>{{ estadisticas.total }}</h3>
                        <p>Total Actividades</p>
                    </div>
                </div>
                <div class="tarjeta">
                    <div class="tarjeta-icon">📈</div>
                    <div class="tarjeta-content">
                        <h3>{{ Object.keys(estadisticas.por_tipo).length }}</h3>
                        <p>Tipos Diferentes</p>
                    </div>
                </div>
                <div class="tarjeta">
                    <div class="tarjeta-icon">👥</div>
                    <div class="tarjeta-content">
                        <h3>{{ Object.keys(estadisticas.por_responsable).length }}</h3>
                        <p>Responsables</p>
                    </div>
                </div>
                <div class="tarjeta">
                    <div class="tarjeta-icon">💰</div>
                    <div class="tarjeta-content">
                        <h3>{{ formatCurrency(totalFacturacion) }}</h3>
                        <p>Facturación Total</p>
                    </div>
                </div>
            </div>
            
            <!-- Grid de Gráficos -->
            <div class="graficos-grid">
                <!-- Gráfico de Actividades por Tipo -->
                <div class="grafico-container">
                    <h3>🏷️ Actividades por Tipo</h3>
                    <div class="chart-wrapper">
                        <Doughnut 
                            v-if="chartDataTipos" 
                            :data="chartDataTipos" 
                            :options="chartOptionsDoughnut"
                        />
                    </div>
                </div>
                
                <!-- Gráfico de Actividades por Responsable -->
                <div class="grafico-container">
                    <h3>👤 Actividades por Responsable</h3>
                    <div class="chart-wrapper">
                        <Bar 
                            v-if="chartDataResponsables" 
                            :data="chartDataResponsables" 
                            :options="chartOptionsBar"
                        />
                    </div>
                </div>
                
                <!-- Gráfico de Coste Medio por Tipo -->
                <div class="grafico-container">
                    <h3>💶 Coste Medio por Tipo</h3>
                    <div class="chart-wrapper">
                        <Bar 
                            v-if="chartDataCostes" 
                            :data="chartDataCostes" 
                            :options="chartOptionsCostes"
                        />
                    </div>
                </div>
                
                <!-- Gráfico de Facturación por Responsable -->
                <div class="grafico-container">
                    <h3>💰 Facturación por Responsable</h3>
                    <div class="chart-wrapper">
                        <Pie 
                            v-if="chartDataFacturacion" 
                            :data="chartDataFacturacion" 
                            :options="chartOptionsPie"
                        />
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Sección de Listado de Actividades -->
        <div v-if="!errorMsg">
            <div v-if="actividades.length > 0" class="actividades-section">
                <h2>📝 Listado de Actividades por Tipo</h2>
                <div v-for="(grupo, tipo) in actividadesPorTipo" :key="tipo" class="tipo-bloque">
                    <h3>{{ tipo }}</h3>
                    <div class="actividades-lista">
                        <div v-for="actividad in grupo" :key="actividad.id_actividad" class="actividad-card">
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
            <div v-else-if="!estadisticas" class="no-data-container">
                <p>📭 No se encontraron actividades para mostrar.</p>
                <span>Verifica si existen datos en la base de datos.</span>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    ArcElement
} from 'chart.js'
import { Bar, Doughnut, Pie } from 'vue-chartjs'

// Registrar componentes de Chart.js
ChartJS.register(
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    ArcElement
)

const actividades = ref([])
const estadisticas = ref(null)
const errorMsg = ref(null)

onMounted(async () => {
    await cargarActividades()
    await cargarEstadisticas()
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

async function cargarEstadisticas() {
    try {
        errorMsg.value = null
        const res = await fetch('http://localhost:8000/api/actividades/estadisticas')
        if (res.ok) {
            estadisticas.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar estadísticas: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        estadisticas.value = null
        errorMsg.value = e.message
        console.error('Error cargando estadísticas:', e)
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

// Paleta de colores para gráficos
const coloresPaleta = [
    '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', 
    '#9966FF', '#FF9F40', '#FF6384', '#C9CBCF',
    '#4BC0C0', '#FF6384', '#36A2EB', '#FFCE56'
]

// Datos para gráfico de actividades por tipo
const chartDataTipos = computed(() => {
    if (!estadisticas.value?.por_tipo) return null
    
    const labels = Object.keys(estadisticas.value.por_tipo)
    const data = Object.values(estadisticas.value.por_tipo)
    
    return {
        labels,
        datasets: [{
            data,
            backgroundColor: coloresPaleta.slice(0, labels.length),
            borderWidth: 2,
            borderColor: '#fff'
        }]
    }
})

// Datos para gráfico de actividades por responsable
const chartDataResponsables = computed(() => {
    if (!estadisticas.value?.por_responsable) return null
    
    const labels = Object.keys(estadisticas.value.por_responsable)
    const data = Object.values(estadisticas.value.por_responsable)
    
    return {
        labels,
        datasets: [{
            label: 'Cantidad de Actividades',
            data,
            backgroundColor: '#36A2EB',
            borderColor: '#36A2EB',
            borderWidth: 1
        }]
    }
})

// Datos para gráfico de costes medios por tipo
const chartDataCostes = computed(() => {
    if (!estadisticas.value?.coste_medio_tipo) return null
    
    const labels = Object.keys(estadisticas.value.coste_medio_tipo)
    const data = Object.values(estadisticas.value.coste_medio_tipo)
    
    return {
        labels,
        datasets: [{
            label: 'Coste Medio (€)',
            data,
            backgroundColor: '#FFCE56',
            borderColor: '#FFCE56',
            borderWidth: 1
        }]
    }
})

// Datos para gráfico de facturación por responsable
const chartDataFacturacion = computed(() => {
    if (!estadisticas.value?.facturacion_por_responsable) return null
    
    const labels = Object.keys(estadisticas.value.facturacion_por_responsable)
    const data = Object.values(estadisticas.value.facturacion_por_responsable)
    
    return {
        labels,
        datasets: [{
            data,
            backgroundColor: coloresPaleta.slice(0, labels.length),
            borderWidth: 2,
            borderColor: '#fff'
        }]
    }
})

// Opciones para gráficos
const chartOptionsDoughnut = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'bottom',
            labels: {
                padding: 20,
                usePointStyle: true
            }
        },
        tooltip: {
            callbacks: {
                label: function(context) {
                    const total = context.dataset.data.reduce((a, b) => a + b, 0)
                    const percentage = ((context.parsed * 100) / total).toFixed(1)
                    return `${context.label}: ${context.parsed} (${percentage}%)`
                }
            }
        }
    }
}

const chartOptionsBar = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false
        }
    },
    scales: {
        y: {
            beginAtZero: true,
            ticks: {
                stepSize: 1
            }
        }
    }
}

const chartOptionsCostes = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false
        }
    },
    scales: {
        y: {
            beginAtZero: true,
            ticks: {
                callback: function(value) {
                    return value + '€'
                }
            }
        }
    }
}

const chartOptionsPie = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'bottom',
            labels: {
                padding: 20,
                usePointStyle: true
            }
        },
        tooltip: {
            callbacks: {
                label: function(context) {
                    return `${context.label}: ${context.parsed}€`
                }
            }
        }
    }
}

// Calcular facturación total
const totalFacturacion = computed(() => {
    if (!estadisticas.value?.facturacion_por_responsable) return 0
    return Object.values(estadisticas.value.facturacion_por_responsable).reduce((a, b) => a + b, 0)
})

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

h3 {
    color:white
}
.general-container {
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

.general-container h1 {
    color: #2c3e50;
    margin-bottom: 10px;
    font-size: 2.5rem;
}

.general-container > p {
    color: #7f8c8d;
    margin-bottom: 30px;
    font-size: 1.1rem;
}

.estadisticas-section {
    margin-bottom: 40px;
}

.estadisticas-section h2 {
    color: #2c3e50;
    margin-bottom: 20px;
    font-size: 2rem;
    border-bottom: 3px solid var(--lightgreen);
    padding-bottom: 10px;
}

/* Tarjetas de Resumen */
.tarjetas-resumen {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.tarjeta {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    display: flex;
    align-items: center;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tarjeta:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
}

.tarjeta:nth-child(2) {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.tarjeta:nth-child(3) {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.tarjeta:nth-child(4) {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
}

.tarjeta-icon {
    font-size: 3rem;
    margin-right: 20px;
}

.tarjeta-content h3 {
    font-size: 2.2rem;
    font-weight: bold;
    margin: 0;
}

.tarjeta-content p {
    margin: 5px 0 0 0;
    opacity: 0.9;
    font-size: 1rem;
}

/* Grid de Gráficos */
.graficos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
    gap: 25px;
    margin-bottom: 40px;
}

.grafico-container {
    background: white;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e8ecef;
}

.grafico-container h3 {
    color: #2c3e50;
    margin: 0 0 20px 0;
    font-size: 1.3rem;
    text-align: center;
    padding-bottom: 10px;
    border-bottom: 2px solid #ecf0f1;
}

.chart-wrapper {
    height: 300px;
    position: relative;
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
    .general-container {
        padding: 15px;
    }
    
    .general-container h1 {
        font-size: 2rem;
    }
    
    .graficos-grid {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .grafico-container {
        padding: 20px;
    }
    
    .chart-wrapper {
        height: 250px;
    }
    
    .tarjetas-resumen {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
    }
    
    .tarjeta {
        padding: 20px;
    }
    
    .tarjeta-icon {
        font-size: 2.5rem;
        margin-right: 15px;
    }
    
    .tarjeta-content h3 {
        font-size: 1.8rem;
    }
    
    .actividades-lista {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .general-container h1 {
        font-size: 1.8rem;
    }
    
    .estadisticas-section h2,
    .actividades-section h2 {
        font-size: 1.5rem;
    }
    
    .tarjetas-resumen {
        grid-template-columns: 1fr;
    }
    
    .chart-wrapper {
        height: 200px;
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

.estadisticas-section,
.actividades-section,
.grafico-container,
.actividad-card {
    animation: fadeIn 0.6s ease-out;
}
</style>
