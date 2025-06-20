<template>
    <div class="general-container">
        <h1>Eventos</h1>
        <div class="container">
            <div class="card" v-for="option in options" :key="option.title" @click="goTo(option.route)">
                <h2>{{ option.title }}</h2>
                <img :src="option.image" alt="Imagen de evento">
                <p>{{ option.description }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

function goTo(route) {
    router.push(route)
}

const options = ref([
    {
        title: 'Ver Eventos',
        description: 'Consulta y gestiona los eventos de interés para la empresa.',
        image: '/imagenes/foto.png',
        route: '/eventos/ver'
    },
    {
        title: 'Agregar Evento',
        description: 'Agrega un nuevo evento relevante.',
        image: '/imagenes/foto.png',
        route: '/eventos/crear'
    }
])
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
