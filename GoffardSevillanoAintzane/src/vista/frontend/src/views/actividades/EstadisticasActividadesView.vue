<template>
    <div class="general-container">
        <h1>Estadísticas de Actividades</h1>
        <p><strong>Total de actividades:</strong> {{ estadisticas.total }}</p>

        <h2>Actividades por tipo</h2>
        <div class="grafico-container">
            <canvas id="graficoTipo" width="320" height="220"></canvas>
        </div>
        <ul>
            <li v-for="(cantidad, tipo) in estadisticas.por_tipo" :key="tipo">
                {{ tipo }}: {{ cantidad }}
            </li>
        </ul>

        <h2>Actividades por responsable</h2>
        <div class="grafico-container">
            <canvas id="graficoResponsable" width="320" height="220"></canvas>
        </div>
        <ul>
            <li v-for="(cantidad, responsable) in estadisticas.por_responsable" :key="responsable">
                {{ responsable }}: {{ cantidad }}
            </li>
        </ul>
    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

const estadisticas = ref({
    total: 0,
    por_tipo: {},
    por_responsable: {}
})

onMounted(async () => {
    try {
        const res = await fetch('http://localhost:8000/api/actividades/estadisticas')
        estadisticas.value = await res.json()

        // Gráfico por tipo
        const ctxTipo = document.getElementById('graficoTipo')
        if (ctxTipo && estadisticas.value.por_tipo && Object.keys(estadisticas.value.por_tipo).length > 0) {
            new Chart(ctxTipo, {
                type: 'bar',
                data: {
                    labels: Object.keys(estadisticas.value.por_tipo),
                    datasets: [{
                        label: 'Actividades por tipo',
                        data: Object.values(estadisticas.value.por_tipo),
                        backgroundColor: '#4caf50'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    }
                }
            })
        }

        // Gráfico por responsable
        const ctxResp = document.getElementById('graficoResponsable')
        if (ctxResp && estadisticas.value.por_responsable && Object.keys(estadisticas.value.por_responsable).length > 0) {
            new Chart(ctxResp, {
                type: 'pie',
                data: {
                    labels: Object.keys(estadisticas.value.por_responsable),
                    datasets: [{
                        label: 'Actividades por responsable',
                        data: Object.values(estadisticas.value.por_responsable),
                        backgroundColor: ['#4caf50', '#2196f3', '#ff9800', '#e91e63', '#9c27b0']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { position: 'bottom' }
                    }
                }
            })
        }
    } catch (e) {
        estadisticas.value = {
            total: 0,
            por_tipo: {},
            por_responsable: {}
        }
    }
})
</script>
<style scoped>
.grafico-container {
    width: 100%;
    max-width: 350px;
    height: 220px;
    margin: 0 auto 1.5em auto;
    display: flex;
    justify-content: center;
    align-items: center;
}
canvas {
    width: 100% !important;
    height: 100% !important;
    max-width: 350px;
    max-height: 220px;
}
@media (max-width: 500px) {
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


