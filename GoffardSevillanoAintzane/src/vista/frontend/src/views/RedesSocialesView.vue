<template>
    <div class="general-container">
        <h1>Redes Sociales</h1>
        <div class="container">
            <div class="card" v-for="option in options" :key="option.title">
                <img class="icon" :src="option.image" :alt="option.title" />
                <!-- <p>{{ option.title }}</p> -->
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const options = ref([
    {
        title: 'Instagram',
        image: require('@/assets/icons/instagram.png'),
    },
    {
        title: 'Facebook',
        image: require('@/assets/icons/facebook.png'),
    },
    {
        title: 'LinkedIn',
        image: require('@/assets/icons/linkedin.png'),
    },
    {
        title: 'YouTube',
        image: require('@/assets/icons/youtube.png'),
    },
    {
        title: 'TikTok',
        image: require('@/assets/icons/tiktok.png'),
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
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 80px;
    padding: 16px 8px;
    background-color: var(--megashoftgreen);
    border: 1px solid var(--shoftgreen);
    border-radius: 0.7rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card p {
    color: var(--darkgrey);
    margin: 0.5rem 0 0 0;
    font-size: 0.95rem;
    text-align: center;
}

.icon {
    width: 50px;
    height: 50px;
    display: block;
    margin: 0;
}
</style>
