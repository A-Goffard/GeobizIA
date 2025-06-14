<template>
    <div class="general-container">
        <h1>Estadísticas de Actividades</h1>
        <p>Estadísticas de las actividades.</p>
        <p>Total de actividades: {{ total }}</p>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const total = ref(12) // Ejemplo
</script>
<style scoped>
/* ...puedes reutilizar estilos de otras vistas... */
</style>
