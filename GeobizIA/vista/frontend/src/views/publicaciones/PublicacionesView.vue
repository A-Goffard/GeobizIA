<template>
    <div class="contenedor-principal">
        <h1>Publicaciones</h1>
        <div class="container">
            <div class="card" v-for="option in options" :key="option.title" @click="goTo(option.route)">
                <h2>{{ option.title }}</h2>
                <img :src="option.image" alt="Imagen de publicación">
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
    // {
    //     title: 'Ver Publicaciones',
    //     description: 'Consulta y gestiona las publicaciones registradas.',
    //     image: '/imagenes/foto.png',
    //     route: '/publicaciones/ver'
    // },
    // {
    //     title: 'Agregar Publicación',
    //     description: 'Agrega una nueva publicación.',
    //     image: '/imagenes/foto.png',
    //     route: '/publicaciones/crear'
    // },
    {
        title: '🤖 Generar con IA',
        description: 'Crea publicaciones automáticamente usando inteligencia artificial.',
        image: '/imagenes/foto.png',
        route: '/ia/generador-publicaciones'
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
