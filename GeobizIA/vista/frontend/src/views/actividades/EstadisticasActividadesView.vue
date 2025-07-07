<template>
    <div class="general-container">
        <h1>Estadísticas de Actividades Realizadas</h1>

        <!-- Gráficos comparativos -->
        <div v-if="estadisticas.por_actividad && estadisticas.por_actividad.length">
            <h2>Cuantas veces se ha realizado la actividad</h2>
            <div class="grafico-container">
                <canvas id="graficoVeces"></canvas>
            </div>
            <h2>Facturación de las actividades</h2>
            <div class="grafico-container">
                <canvas id="graficoFacturacion"></canvas>
            </div>
            <h2>Beneficio de las actividades</h2>
            <div class="grafico-container">
                <canvas id="graficoBeneficio"></canvas>
            </div>
            <h2>Asistencia a las actividades</h2>
            <div class="grafico-container">
                <canvas id="graficoAsistencia"></canvas>
            </div>
        </div>

        <!-- Listado detallado -->
        <div v-if="estadisticas.por_actividad && estadisticas.por_actividad.length">
            <div v-for="actividad in estadisticas.por_actividad" :key="actividad.nombre" class="actividad-block">
                <h2>{{ actividad.nombre }}</h2>
                <ul>
                    <li><strong>Veces realizada:</strong> {{ actividad.veces_realizada }}</li>
                    <li><strong>Facturación total:</strong> {{ actividad.facturacion_total }} €</li>
                    <li><strong>Coste total:</strong> {{ actividad.coste_total }} €</li>
                    <li><strong>Beneficio total:</strong> {{ actividad.beneficio_total }} €</li>
                    <li><strong>Asistencia total:</strong> {{ actividad.asistencia_total }}</li>
                    <li><strong>Fechas:</strong> {{ actividad.fechas.join(', ') }}</li>
                    <li>
                        <strong>Observaciones:</strong>
                        <ul>
                            <li v-for="(obs, idx) in actividad.observaciones" :key="idx">{{ obs }}</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        <div v-else>
            <em>No hay datos de actividades realizadas.</em>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'
import Chart from 'chart.js/auto'

const estadisticas = ref({ por_actividad: [] })

onMounted(async () => {
    try {
        const res = await fetch('http://localhost:8000/api/actividades_realizadas/estadisticas')
        estadisticas.value = await res.json()
        await nextTick()

        // Gráfico: Veces realizada por actividad
        const ctxVeces = document.getElementById('graficoVeces')
        if (ctxVeces && estadisticas.value.por_actividad.length) {
            new Chart(ctxVeces, {
                type: 'bar',
                data: {
                    labels: estadisticas.value.por_actividad.map(a => a.nombre),
                    datasets: [{
                        label: 'Veces realizada',
                        data: estadisticas.value.por_actividad.map(a => a.veces_realizada),
                        backgroundColor: '#4caf50'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } }
                }
            })
        }

        // Gráfico: Facturación total por actividad
        const ctxFact = document.getElementById('graficoFacturacion')
        if (ctxFact && estadisticas.value.por_actividad.length) {
            new Chart(ctxFact, {
                type: 'bar',
                data: {
                    labels: estadisticas.value.por_actividad.map(a => a.nombre),
                    datasets: [{
                        label: 'Facturación total (€)',
                        data: estadisticas.value.por_actividad.map(a => a.facturacion_total),
                        backgroundColor: '#2196f3'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } }
                }
            })
        }

        // Gráfico: Beneficio total por actividad
        const ctxBen = document.getElementById('graficoBeneficio')
        if (ctxBen && estadisticas.value.por_actividad.length) {
            new Chart(ctxBen, {
                type: 'bar',
                data: {
                    labels: estadisticas.value.por_actividad.map(a => a.nombre),
                    datasets: [{
                        label: 'Beneficio total (€)',
                        data: estadisticas.value.por_actividad.map(a => a.beneficio_total),
                        backgroundColor: '#ff9800'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } }
                }
            })
        }

        // Gráfico: Asistencia total por actividad
        const ctxAsist = document.getElementById('graficoAsistencia')
        if (ctxAsist && estadisticas.value.por_actividad.length) {
            new Chart(ctxAsist, {
                type: 'bar',
                data: {
                    labels: estadisticas.value.por_actividad.map(a => a.nombre),
                    datasets: [{
                        label: 'Asistencia total',
                        data: estadisticas.value.por_actividad.map(a => a.asistencia_total),
                        backgroundColor: '#9c27b0'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } }
                }
            })
        }
    } catch (e) {
        estadisticas.value = { por_actividad: [] }
    }
})
</script>

<style scoped>
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

.grafico-container {
    width: 100%;
    max-width: 600px;
    height: 220px;
    margin: 0 auto 2em auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

canvas {
    width: 100% !important;
    height: 100% !important;
    max-width: 600px;
    max-height: 220px;
}

.actividad-block {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-bottom: 2rem;
    padding: 1rem 1.5rem;
    background: #f9f9f9;
}

ul {
    margin: 0.5em 0 0.5em 1.5em;
}

@media (max-width: 600px) {
    .grafico-container {
        max-width: 100vw;
        height: 160px;
    }

    canvas {
        max-width: 100vw;
        max-height: 160px;
    }
}
</style>
