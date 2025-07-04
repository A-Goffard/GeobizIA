<template>
    <div class="general-container">
        <h1>Ver Actividades</h1>
        <p>Listado de actividades agrupadas por tipo.</p>
        <div v-for="(grupo, tipo) in actividadesPorTipo" :key="tipo" class="tipo-bloque">
            <h2>{{ tipo }}</h2>
            <ul>
                <li v-for="actividad in grupo" :key="actividad.id_actividad">
                    {{ actividad.nombre }} – {{ actividad.duracion }}
                </li>
            </ul>
        </div>
    </div>
</template>
<script setup>
import { ref, computed, onMounted } from 'vue'
const actividades = ref([])

onMounted(async () => {
    try {
        const res = await fetch('http://localhost:8000/api/actividades')
        if (res.ok) {
            actividades.value = await res.json()
        } else {
            actividades.value = []
        }
    } catch (e) {
        actividades.value = []
    }
})

// Agrupa las actividades por tipo
const actividadesPorTipo = computed(() => {
    const grupos = {}
    for (const act of actividades.value) {
        const tipo = act.tipo || 'Sin tipo'
        if (!grupos[tipo]) grupos[tipo] = []
        grupos[tipo].push(act)
    }
    return grupos
})
</script>
<style scoped>

</style>
