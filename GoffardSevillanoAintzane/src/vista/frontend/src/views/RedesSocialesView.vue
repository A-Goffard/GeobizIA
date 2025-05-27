<template>
    <div class="general-container">
        <h1>Redes Sociales</h1>
        <div class="container">
            <div class="card" v-for="option in options" :key="option.title">
                <h2>{{ option.title }}</h2>
                <img :src="option.image" alt="Imagen de publicación">
                <p>{{ option.description }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const options = ref([
    {
        title: 'Instagram',
        description: 'Sigue nuestras últimas novedades y publicaciones en Instagram.',
        image: '/imagenes/instagram.png',
    },
    {
        title: 'Facebook',
        description: 'Conéctate con nosotros en Facebook para más actualizaciones.',
        image: '/imagenes/facebook.png',
    },
    {
        title: 'Twitter',
        description: 'Síguenos en Twitter para noticias rápidas y actualizaciones.',
        image: '/imagenes/twitter.png',
    },
    {
        title: 'LinkedIn',
        description: 'Conéctate profesionalmente con nosotros en LinkedIn.',
        image: '/imagenes/linkedin.png',
    },
    {
        title: 'YouTube',
        description: 'Mira nuestros videos y tutoriales en YouTube.',
        image: '/imagenes/youtube.png',
    },
    {
        title: 'TikTok',
        description: 'Disfruta de nuestros contenidos divertidos y creativos en TikTok.',
        image: '/imagenes/tiktok.png',
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
