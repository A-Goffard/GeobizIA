<template>
    <div class="general-container">
        <h1>Ver Eventos</h1>
        <p>Listado de eventos existentes.</p>
            <ul>
      <li v-for="evento in eventos" :key="evento.id_evento">
        {{ evento.nombre }} – {{ evento.fecha_comienzo }} a {{ evento.fecha_final }}
      </li>
    </ul>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const eventos = ref([
    // Ejemplo de datos
    { id_evento: 1, nombre: 'Sopela Kosta Fest', fecha_comienzo: '2024-06-01', fecha_final: '2024-06-02' },
    { id_evento: 2, nombre: 'Getxo Aste Berdea', fecha_comienzo: '2024-06-10', fecha_final: '2024-06-12' },
])
</script>
<style scoped>
/* ...puedes reutilizar estilos de otras vistas... */
</style>
