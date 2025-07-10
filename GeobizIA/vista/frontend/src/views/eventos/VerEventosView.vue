<template>
    <div class="general-container">
        <h1>Ver Eventos</h1>
        <p>Listado de eventos existentes.</p>
        <div v-if="errorMsg" class="error-container">
            <h2>⚠️ Ha ocurrido un error</h2>
            <p>{{ errorMsg }}</p>
        </div>
        <div v-else>
            <div v-if="eventos.length > 0" class="eventos-list">
                <div v-for="evento in eventos" :key="evento.id_evento" class="evento-card" @click="verDetalle(evento.id_evento)">
                    <h3>{{ evento.nombre }}</h3>
                    <p><strong>Tipo:</strong> {{ evento.tipo }}</p>
                    <p><strong>Lugar:</strong> {{ evento.lugar }}</p>
                    <p><strong>Fechas:</strong> {{ evento.fecha_comienzo }} a {{ evento.fecha_final }}</p>
                    <p><strong>Población:</strong> {{ evento.poblacion }}</p>
                    <p><strong>Temática:</strong> {{ evento.tematica }}</p>
                </div>
            </div>
            <div v-else class="no-data-container">
                <p>📭 No se encontraron eventos para mostrar.</p>
                <span>Verifica si existen datos en la base de datos o si los filtros aplicados son correctos.</span>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const eventos = ref([])
const errorMsg = ref(null)

onMounted(async () => {
    await cargarEventos()
})

function verDetalle(id) {
    router.push(`/eventos/detalle/${id}`)
}

async function cargarEventos() {
    try {
        errorMsg.value = null;
        const res = await fetch('http://localhost:8000/api/eventos')
        if (res.ok) {
            eventos.value = await res.json()
        } else {
            throw new Error(`Error del servidor al cargar eventos: ${res.status} ${res.statusText}`)
        }
    } catch (e) {
        eventos.value = []
        errorMsg.value = e.message
        console.error('Error cargando eventos:', e)
    }
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

.eventos-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.evento-card {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    cursor: pointer;
}

.evento-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.evento-card h3 {
    margin-top: 0;
    color: #333;
}

.evento-card p {
    margin-bottom: 0;
    color: #666;
}
</style>
