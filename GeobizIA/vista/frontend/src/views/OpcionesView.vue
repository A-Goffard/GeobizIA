<template>
    <div class="general-container">
        <h1>Opciones</h1>
        <div class="container">
            <div class="card" v-for="option in options" :key="option.title" @click="goToDetail(option.link)">
                <div>
                    <h2>{{ option.title }}</h2>
                    <p>{{ option.description }}</p>
                </div>
                <div>
                    <img :src="option.image" alt="Imagen del proyecto">
                </div>
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
        title: 'Actividades',
        description: 'Aquí puedes ver las actividades realizadas, programar nuevas actividades, y gestionar las existentes.',
        link: '/actividades',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Facturas',
        description: 'Aquí puedes ver y gestionar todas las facturas generadas y generar nuevas.',
        link: '/facturas',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Publicaciones',
        description: 'Aquí puedes ver las publicaciones realizadas, programar nuevas publicaciones, y gestionar las existentes.',
        link: '/publicaciones',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Proyectos',
        description: 'Aquí puedes ver los proyectos realizados, programar nuevos proyectos, y gestionar los existentes.',
        link: '/proyectos',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Eventos',
        description: 'Aquí puedes ver los eventos que pueden ser interesantes para la empresa para participar, agregar nuevos eventos, y gestionar los existentes.',
        link: '/eventos',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Participantes',
        description: 'Aquí puedes ver los participantes de las actividades, eventos y proyectos, y gestionar sus datos.',
        link: '/participantes',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Documentos',
        description: 'Aquí puedes ver los documentos importantes de la empresa, agregar nuevos documentos, y gestionar los existentes.',
        link: '/documentos',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Empresas',
        description: 'Aquí puedes ver las empresas con las que colaboramos, agregar nuevas empresas, y gestionar las existentes.',
        link: '/empresas',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Redes Sociales',
        description: 'Aquí puedes ver las redes sociales de la empresa, agregar nuevas redes sociales, y gestionar las existentes.',
        link: '/redes-sociales',
        image: '/imagenes/foto.png',
    },
    {
        title: 'Clientes',
        description: 'Aquí puedes ver los clientes de la empresa, agregar nuevos clientes, y gestionar los existentes.',
        link: '/clientes',
        image: '/imagenes/foto.png',
    }
])

const goToDetail = (link) => {
    router.push(link)
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