from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from datetime import datetime

# Importación opcional de OpenAI (solo si está instalado)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from GeobizIA.controlador.gestores.actividades_realizadas import ActividadesRealizadas
from GeobizIA.controlador.gestores.actividades import Actividades

router = APIRouter()

class GenerarPublicacionRequest(BaseModel):
    id_actividad_realizada: int
    tipo_publicacion: str  # "anuncio", "durante", "completado"
    tono: str  # "profesional", "cercano", "motivacional"
    plataforma: str  # "instagram", "facebook", "twitter"
    incluir_hashtags: bool = True

class PublicacionGenerada(BaseModel):
    contenido: str
    hashtags: str
    caracteres: int
    plataforma: str

@router.post("/generar-publicacion")
def generar_publicacion_ia(request: GenerarPublicacionRequest) -> PublicacionGenerada:
    try:
        # Obtener datos de la actividad realizada
        gestor_realizadas = ActividadesRealizadas()
        gestor_actividades = Actividades()
        
        actividad_realizada = gestor_realizadas.buscar(request.id_actividad_realizada)
        if not actividad_realizada:
            raise HTTPException(status_code=404, detail="Actividad realizada no encontrada")
        
        actividad = gestor_actividades.buscar(actividad_realizada.id_actividad)
        if not actividad:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")
        
        # Crear prompt personalizado
        prompt = crear_prompt_publicacion(actividad, actividad_realizada, request)
        
        # Generar con IA (usando un modelo simple por ahora)
        contenido = generar_contenido_ia(prompt, request)
        
        # Generar hashtags
        hashtags = generar_hashtags(actividad, request) if request.incluir_hashtags else ""
        
        return PublicacionGenerada(
            contenido=contenido,
            hashtags=hashtags,
            caracteres=len(contenido + hashtags),
            plataforma=request.plataforma
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar publicación: {str(e)}")

def crear_prompt_publicacion(actividad, actividad_realizada, request):
    """Crea un prompt específico para la generación de contenido"""
    
    prompts_base = {
        "anuncio": f"""Crea una publicación para anunciar la próxima actividad:
        Actividad: {actividad.nombre}
        Tipo: {actividad.tipo}
        Descripción: {actividad.descripcion or 'Actividad ambiental'}
        Duración: {actividad.duracion}
        Responsable: {actividad.responsable}
        
        La publicación debe ser para {request.plataforma} con tono {request.tono}.
        Debe generar expectación y motivar a participar.""",
        
        "durante": f"""Crea una publicación mientras se realiza la actividad:
        Actividad: {actividad.nombre}
        Fecha: {actividad_realizada.fecha}
        Asistentes: {actividad_realizada.asistentes or 'varios participantes'}
        
        La publicación debe ser para {request.plataforma} con tono {request.tono}.
        Debe mostrar el evento en vivo y la participación.""",
        
        "completado": f"""Crea una publicación celebrando que la actividad se completó:
        Actividad: {actividad.nombre}
        Fecha: {actividad_realizada.fecha}
        Asistentes: {actividad_realizada.asistentes or 'participantes'}
        Observaciones: {actividad_realizada.observaciones or 'Actividad exitosa'}
        
        La publicación debe ser para {request.plataforma} con tono {request.tono}.
        Debe celebrar el éxito y agradecer la participación."""
    }
    
    return prompts_base.get(request.tipo_publicacion, prompts_base["completado"])

def generar_contenido_ia(prompt, request):
    """Genera el contenido usando IA o plantillas inteligentes"""
    
    # Por ahora, usamos plantillas inteligentes
    # Más adelante se puede integrar con OpenAI o modelos locales
    
    plantillas = {
        "instagram": {
            "profesional": "🌱 En GeobizIA nos complace anunciar: {contenido}\n\n📍 Únete a nosotros en esta iniciativa sostenible.\n\n#Sostenibilidad #MedioAmbiente",
            "cercano": "¡Hola! 👋 Queremos contarte sobre: {contenido}\n\n¿Te apuntas? 🌍✨\n\n#EcoFriendly #Naturaleza",
            "motivacional": "🚀 ¡Es momento de actuar! {contenido}\n\n💪 Cada pequeña acción cuenta para nuestro planeta.\n\n#CambioClimático #Acción"
        },
        "facebook": {
            "profesional": "Estimados seguidores,\n\n{contenido}\n\nLes invitamos a participar en esta importante iniciativa medioambiental.",
            "cercano": "¡Hola amigos! 😊\n\n{contenido}\n\n¿Quién se apunta a cuidar nuestro planeta juntos?",
            "motivacional": "¡ATENCIÓN! 📢\n\n{contenido}\n\nEl planeta nos necesita. ¡Seamos el cambio que queremos ver!"
        },
        "twitter": {
            "profesional": "📢 {contenido}\n\n#Sostenibilidad #GeobizIA",
            "cercano": "🌱 {contenido} ¿Te unes? 😊\n\n#EcoLife",
            "motivacional": "🔥 {contenido}\n\n¡Actúa AHORA! 💪 #CambioClimático"
        }
    }
    
    plantilla = plantillas[request.plataforma][request.tono]
    
    # Aquí iría la lógica más sofisticada de generación
    # Por simplicidad, usamos la plantilla base
    contenido_base = "una increíble actividad medioambiental"
    
    return plantilla.format(contenido=contenido_base)

def generar_hashtags(actividad, request):
    """Genera hashtags relevantes"""
    hashtags_base = ["#GeobizIA", "#MedioAmbiente", "#Sostenibilidad"]
    
    # Agregar hashtags específicos según el tipo de actividad
    if "reciclaje" in actividad.nombre.lower():
        hashtags_base.extend(["#Reciclaje", "#EconomiaCircular"])
    elif "plantacion" in actividad.nombre.lower() or "arbol" in actividad.nombre.lower():
        hashtags_base.extend(["#Reforestacion", "#PlantarArboles"])
    elif "limpieza" in actividad.nombre.lower():
        hashtags_base.extend(["#LimpiezaAmbiental", "#CuidemosElPlaneta"])
    
    # Hashtags específicos por plataforma
    if request.plataforma == "instagram":
        hashtags_base.extend(["#EcoFriendly", "#GreenLife", "#NaturalezaLovers"])
    elif request.plataforma == "twitter":
        hashtags_base.extend(["#ClimateAction", "#EcoTech"])
    
    return " ".join(hashtags_base[:8])  # Máximo 8 hashtags

@router.get("/actividades-realizadas")
def listar_actividades_para_ia():
    """Obtiene las actividades realizadas para el selector"""
    try:
        gestor_realizadas = ActividadesRealizadas()
        gestor_actividades = Actividades()
        
        realizadas = gestor_realizadas.mostrar_todos_los_elem()
        resultado = []
        
        for realizada in realizadas:
            actividad = gestor_actividades.buscar(realizada.id_actividad)
            if actividad:
                resultado.append({
                    "id_actividad_realizada": realizada.id_actividad_realizada,
                    "nombre_actividad": actividad.nombre,
                    "fecha": realizada.fecha,
                    "asistentes": realizada.asistentes,
                    "tipo": actividad.tipo
                })
        
        return resultado
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener actividades: {str(e)}")
