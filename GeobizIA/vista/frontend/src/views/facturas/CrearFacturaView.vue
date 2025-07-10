<template>
    <div>
        <FacturaForm @facturaCreada="onFacturaCreada" />
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import FacturaForm from '../../components/formularios/FacturaForm.vue'

const router = useRouter()

function onFacturaCreada() {
    // Opcional: redirigir a la lista después de crear
    setTimeout(() => {
        router.push('/facturas/ver')
    }, 2000)
}
</script>
