<template>
    <div class="general-container">
        <h1>Ver Actividades</h1>
        <p>Listado de actividades existentes.</p>
            <ul>
      <li v-for="actividad in actividades" :key="actividad.id_actividad">
        {{ actividad.nombre }} – {{ actividad.fecha_ejecucion }}
      </li>
    </ul>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const actividades = ref([
    // Ejemplo de datos
    { id_actividad: 1, nombre: 'Taller de reciclaje', fecha_ejecucion: '2024-06-01' },
    { id_actividad: 2, nombre: 'Salida al monte', fecha_ejecucion: '2024-06-10' }
])
</script>
<style scoped>
/* ...puedes reutilizar estilos de otras vistas... */
</style>
