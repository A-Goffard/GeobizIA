import { createRouter, createWebHistory } from 'vue-router'

import InicioView from '../views/InicioView.vue'
import OpcionesView from '../views/OpcionesView.vue'
import ActividadesView from '../views/ActividadesView.vue'
import FacturasView from '../views/FacturasView.vue'
import PublicacionesView from '../views/PublicacionesView.vue'
import ProyectosView from '../views/ProyectosView.vue'
import EventosView from '../views/EventosView.vue'
import ParticipantesView from '../views/ParticipantesView.vue'
import DocumentosView from '../views/DocumentosView.vue'
import EmpresasView from '../views/EmpresasView.vue'
import RedesSocialesView from '../views/RedesSocialesView.vue'

const routes = [
    { path: '/', name: 'inicio', component: InicioView },
    { path: '/opciones', name: 'opciones', component: OpcionesView },
    { path: '/actividades', name: 'actividades', component: ActividadesView },
    { path: '/facturas', name: 'facturas', component: FacturasView },
    { path: '/publicaciones', name: 'publicaciones', component: PublicacionesView },
    { path: '/proyectos', name: 'proyectos', component: ProyectosView },
    { path: '/eventos', name: 'eventos', component: EventosView },
    { path: '/participantes', name: 'participantes', component: ParticipantesView },
    { path: '/documentos', name: 'documentos', component: DocumentosView },
    { path: '/empresas', name: 'empresas', component: EmpresasView },
    { path: '/redes-sociales', name: 'redes-sociales', component: RedesSocialesView },
    // ...otras rutas
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// Protección de ruta
router.beforeEach((to, from, next) => {
    const autenticado = localStorage.getItem('autenticado') === 'true'
    if (to.name === 'opciones' && !autenticado) {
        next({ name: 'inicio' })
    } else {
        next()
    }
})

export default router