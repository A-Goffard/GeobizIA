<template>
    <div class="general-container">
        <h1>Actividades</h1>
        <div class="container">
            <div
                class="card"
                v-for="option in options"
                :key="option.title"
                @click="goTo(option.route)"
            >
                <h2>{{ option.title }}</h2>
                <img :src="option.image" alt="Imagen de actividad">
                <p>{{ option.description }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const options = ref([
    {
        title: 'Crear Actividad',
        description: 'Crea una nueva actividad para la empresa.',
        image: '/imagenes/foto.png',
        route: '/actividades/crear'
    },
    {
        title: 'Ver Actividades',
        description: 'Consulta y gestiona todas las actividades realizadas.',
        image: '/imagenes/foto.png',
        route: '/actividades/ver'
    },
    {
        title: 'Estadísticas',
        description: 'Visualiza estadísticas de las actividades.',
        image: '/imagenes/foto.png',
        route: '/actividades/estadisticas'
    },
    {
        title: 'Añadir actividad realizada',
        description: 'Añadir una actividad realizada.',
        image: '/imagenes/foto.png',
        route: '/actividades/actividad_realizada'
    },
    {
        title: 'Predicción de nueva actividad',
        description: 'Predecir resultados y estadísticas de nueva actividad.',
        image: '/imagenes/foto.png',
        route: '/actividades/prediccion_actividad'
    }
])

function goTo(route) {
    router.push(route)
}
</script>

<style scoped>
.container {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    justify-content: center;
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

.card {
    width: 300px;
    padding: 20px;
    background-color: var(--megashoftgreen);
    border: 1px solid var(--shoftgreen);
    border-radius: 0.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card h2 {
    margin-top: 0;
}

.card p {
    color: var(--darkgrey);
}

img {
    width: 100%;
    border-radius: 0.5rem;
}
</style>
