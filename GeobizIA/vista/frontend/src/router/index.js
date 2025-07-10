import { createRouter, createWebHistory } from 'vue-router'

import InicioView from '../views/InicioView.vue'
import OpcionesView from '../views/OpcionesView.vue'

import ActividadesView from '../views/actividades/ActividadesView.vue'
import CrearActividadView from '../views/actividades/CrearActividadView.vue'
import CrearActividadRealizadaView from '../views/actividades/CrearActividadRealizadaView.vue'
import VerActividadesView from '../views/actividades/VerActividadesView.vue'
import PrediccionActividadView from '@/views/actividades/PrediccionActividadView.vue'
import EstadisticasActividadesView from '../views/actividades/EstadisticasActividadesView.vue'
import ActividadDetalleView from '@/views/actividades/ActividadDetalleView.vue'

import FacturasView from '../views/facturas/FacturasView.vue'
import CrearFacturaView from '../views/facturas/CrearFacturaView.vue'
import VerFacturasView from '../views/facturas/VerFacturasView.vue'

import PublicacionesView from '../views/publicaciones/PublicacionesView.vue'
import CrearPublicacionView from '../views/publicaciones/CrearPublicacionView.vue'
import VerPublicacionesView from '../views/publicaciones/VerPublicacionesView.vue'

import ProyectosView from '../views/proyectos/ProyectosView.vue'
import CrearProyectoView from '../views/proyectos/CrearProyectoView.vue'
import VerProyectosView from '../views/proyectos/VerProyectosView.vue'
import ProyectoDetalleView from '../views/proyectos/ProyectoDetalleView.vue'

import EventosView from '../views/eventos/EventosView.vue'
import CrearEventosView from '../views/eventos/CrearEventosView.vue'
import VerEventosView from '../views/eventos/VerEventosView.vue'
import EventoDetalleView from '../views/eventos/EventoDetalleView.vue'

import ParticipantesView from '../views/participantes/ParticipantesView.vue'
import CrearParticipanteView from '../views/participantes/CrearParticipanteView.vue'
import VerParticipantesView from '../views/participantes/VerParticipantesView.vue'

import DocumentosView from '../views/documentos/DocumentosView.vue'
import CrearDocumentoView from '../views/documentos/CrearDocumentoView.vue'
import VerDocumentosView from '../views/documentos/VerDocumentosView.vue'

import EmpresasView from '../views/empresas/EmpresasView.vue'
import CrearEmpresaView from '../views/empresas/CrearEmpresaView.vue'
import VerEmpresasView from '../views/empresas/VerEmpresasView.vue'
import EmpresaDetalleView from '../views/empresas/EmpresaDetalleView.vue'

import RedesSocialesView from '../views/redessociales/RedesSocialesView.vue'
import CrearRedSocialView from '../views/redessociales/CrearRedSocialView.vue'
import VerRedesSocialesView from '../views/redessociales/VerRedesSocialesView.vue'

import ClientesView from '../views/clientes/ClientesView.vue'
import CrearClienteView from '../views/clientes/CrearClienteView.vue'
import VerClientesView from '../views/clientes/VerClientesView.vue'
import ClienteDetalleView from '../views/clientes/ClienteDetalleView.vue'

const routes = [
    { path: '/', name: 'inicio', component: InicioView },
    { path: '/opciones', name: 'opciones', component: OpcionesView },

    { path: '/actividades', name: 'actividades', component: ActividadesView,},
    { path: '/actividades/crear', name: 'crear-actividad', component: CrearActividadView },
    { path: '/actividades/ver', name: 'ver-actividades', component: VerActividadesView },
    { path: '/actividades/estadisticas', name: 'estadisticas-actividades', component: EstadisticasActividadesView },
    { path: '/actividades/actividad_realizada', name: 'actividad_realizada', component: CrearActividadRealizadaView },
    { path: '/actividades/prediccion_actividad', name: 'prediccion_actividad', component: PrediccionActividadView },
    { path: '/actividades/detalle/:id', name: 'actividad_detalle', component: ActividadDetalleView },

    { path: '/facturas', name: 'facturas', component: FacturasView },
    { path: '/facturas/crear', name: 'crear-factura', component: CrearFacturaView },
    { path: '/facturas/ver', name: 'ver-facturas', component: VerFacturasView },
    
    { path: '/publicaciones', name: 'publicaciones', component: PublicacionesView },
    { path: '/publicaciones/crear', name: 'crear-publicacion', component: CrearPublicacionView },
    { path: '/publicaciones/ver', name: 'ver-publicaciones', component: VerPublicacionesView },
    
    { path: '/proyectos', name: 'proyectos', component: ProyectosView },
    { path: '/proyectos/crear', name: 'crear-proyecto', component: CrearProyectoView },
    { path: '/proyectos/ver', name: 'ver-proyectos', component: VerProyectosView },
    { path: '/proyectos/detalle/:id', name: 'proyecto-detalle', component: ProyectoDetalleView },

    { path: '/eventos', name: 'eventos', component: EventosView },
    { path: '/eventos/crear', name: 'crear-eventos', component: CrearEventosView },
    { path: '/eventos/ver', name: 'ver-eventos', component: VerEventosView },
    { path: '/eventos/detalle/:id', name: 'evento-detalle', component: EventoDetalleView },

    { path: '/participantes', name: 'participantes', component: ParticipantesView },
    { path: '/participantes/crear', name: 'crear-participante', component: CrearParticipanteView },
    { path: '/participantes/ver', name: 'ver-participantes', component: VerParticipantesView },
    
    { path: '/documentos', name: 'documentos', component: DocumentosView },
    { path: '/documentos/crear', name: 'crear-documento', component: CrearDocumentoView },
    { path: '/documentos/ver', name: 'ver-documentos', component: VerDocumentosView },
    
    { path: '/empresas', name: 'empresas', component: EmpresasView },
    { path: '/empresas/crear', name: 'crear-empresa', component: CrearEmpresaView },
    { path: '/empresas/ver', name: 'ver-empresas', component: VerEmpresasView },
    { path: '/empresas/detalle/:id', name: 'empresa-detalle', component: EmpresaDetalleView },
    
    { path: '/redes-sociales', name: 'redes-sociales', component: RedesSocialesView },
    { path: '/redes-sociales/crear', name: 'crear-red-social', component: CrearRedSocialView },
    { path: '/redes-sociales/ver', name: 'ver-redes-sociales', component: VerRedesSocialesView },

    { path: '/clientes', name: 'clientes', component: ClientesView },
    { path: '/clientes/crear', name: 'crear-cliente', component: CrearClienteView },
    { path: '/clientes/ver', name: 'ver-clientes', component: VerClientesView },
    { path: '/clientes/detalle/:id', name: 'cliente-detalle', component: ClienteDetalleView },
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