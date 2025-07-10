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
        
        # Generar con IA (usando plantillas mejoradas)
        contenido = generar_contenido_ia(prompt, request, actividad, actividad_realizada)
        
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

def generar_contenido_ia(prompt, request, actividad, actividad_realizada):
    """Genera el contenido usando IA o plantillas inteligentes mejoradas"""
    
    # CONFIGURACIÓN: Cambiar a True para usar OpenAI (requiere API key)
    USAR_OPENAI = False
    
    # Opción 1: Intentar con OpenAI si está activado
    if USAR_OPENAI and OPENAI_AVAILABLE:
        contenido_openai = generar_con_openai_real(actividad, actividad_realizada, request)
        if contenido_openai:
            return contenido_openai
    
    # Opción 2: Usar plantillas inteligentes mejoradas (por defecto)
    
    # Extraer datos reales de la actividad
    nombre_actividad = actividad.nombre
    tipo_actividad = actividad.tipo or "actividad"
    descripcion = actividad.descripcion or ""
    responsable = actividad.responsable or "nuestro equipo"
    duracion = actividad.duracion or ""
    
    # Datos de la actividad realizada
    fecha = actividad_realizada.fecha if hasattr(actividad_realizada, 'fecha') else ""
    asistentes = actividad_realizada.asistentes if hasattr(actividad_realizada, 'asistentes') else ""
    observaciones = actividad_realizada.observaciones if hasattr(actividad_realizada, 'observaciones') else ""
    
    # Plantillas mejoradas por tipo de publicación
    if request.tipo_publicacion == "anuncio":
        return generar_anuncio(nombre_actividad, tipo_actividad, descripcion, responsable, duracion, request)
    elif request.tipo_publicacion == "durante":
        return generar_durante(nombre_actividad, asistentes, observaciones, request)
    elif request.tipo_publicacion == "completado":
        return generar_completado(nombre_actividad, fecha, asistentes, observaciones, request)
    
    return "Contenido generado automáticamente"

async def generar_con_openai_real(actividad, actividad_realizada, request):
    """Opción avanzada: usar OpenAI para contenido más natural"""
    
    if not OPENAI_AVAILABLE:
        return None
    
    try:
        # Configurar OpenAI (necesitas tu API key)
        # openai.api_key = os.getenv("OPENAI_API_KEY")  # Descomenta esta línea
        
        # Crear prompt contextual detallado
        contexto = f"""
        Actividad: {actividad.nombre}
        Tipo: {actividad.tipo or 'actividad ambiental'}
        Descripción: {actividad.descripcion or 'Actividad enfocada en sostenibilidad'}
        Responsable: {actividad.responsable or 'nuestro equipo'}
        """
        
        if hasattr(actividad_realizada, 'fecha'):
            contexto += f"\nFecha: {actividad_realizada.fecha}"
        if hasattr(actividad_realizada, 'asistentes'):
            contexto += f"\nAsistentes: {actividad_realizada.asistentes}"
        
        prompt = f"""
        Eres un experto en marketing digital y comunicación ambiental. 
        Crea una publicación atractiva para {request.plataforma} con tono {request.tono}.
        
        Tipo de publicación: {request.tipo_publicacion}
        
        Contexto de la actividad:
        {contexto}
        
        La publicación debe:
        - Ser auténtica y engaging
        - Usar emojis apropiados
        - Adaptarse al tono solicitado
        - Ser apropiada para {request.plataforma}
        - Motivar participación o celebrar logros
        - Incluir llamadas a la acción cuando sea apropiado
        
        Genera solo el texto de la publicación, sin hashtags.
        """
        
        # Aquí irías la llamada a OpenAI
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[{"role": "user", "content": prompt}],
        #     max_tokens=300,
        #     temperature=0.7
        # )
        # return response.choices[0].message.content.strip()
        
        # Por ahora devuelve None para usar las plantillas mejoradas
        return None
        
    except Exception as e:
        print(f"Error con OpenAI: {e}")
        return None

# Función para activar fácilmente OpenAI
def activar_openai():
    """
    Para activar OpenAI:
    1. Instala: pip install openai
    2. Configura tu API key en el archivo .env o como variable de entorno
    3. Descomenta las líneas de código de OpenAI en la función generar_con_openai_real
    4. Cambia USAR_OPENAI a True en la función generar_contenido_ia
    """
    pass

def generar_anuncio(nombre, tipo, descripcion, responsable, duracion, request):
    """Genera contenido para anunciar una actividad"""
    
    # Emojis contextuales
    emojis_tipo = {
        "taller": "🔧",
        "charla": "💬", 
        "limpieza": "🧹",
        "plantacion": "🌱",
        "reciclaje": "♻️",
        "curso": "📚",
        "evento": "🎉",
        "conferencia": "🎤"
    }
    
    emoji = "🌍"  # Default
    for key, value in emojis_tipo.items():
        if key in tipo.lower():
            emoji = value
            break
    
    # Frases motivadoras contextuales
    frases_motivadoras = {
        "reciclaje": "Dale una segunda vida a los materiales",
        "plantacion": "Cada árbol cuenta para nuestro futuro",
        "limpieza": "Juntos por un entorno más limpio",
        "energia": "El futuro es renovable",
        "agua": "Cuidemos nuestro recurso más valioso"
    }
    
    frase_motivadora = "Únete al cambio que necesita nuestro planeta"
    for key, value in frases_motivadoras.items():
        if key in (tipo + descripcion).lower():
            frase_motivadora = value
            break
    
    # Plantillas por plataforma y tono
    plantillas = {
        "instagram": {
            "profesional": f"""{emoji} PRÓXIMAMENTE: {nombre}

{frase_motivadora}

📅 Actividad: {tipo}
👨‍🏫 Con: {responsable}
⏰ Duración: {duracion}

📝 Reserva tu plaza en el enlace de bio

#GeobizIA #Sostenibilidad""",
            
            "cercano": f"""¡Hola eco-amigos! 👋

¿Listos para {nombre.lower()}? {emoji}

{frase_motivadora} 🌟

Será súper interesante y lo pasaremos genial juntos. ¡No te lo pierdas!

¿Te apuntas? 💚""",
            
            "motivacional": f"""🚨 ¡ALERTA VERDE! 🚨

{emoji} {nombre.upper()}

💪 {frase_motivadora}
🔥 Con {responsable}
⚡ Solo {duracion}

¡El planeta te NECESITA! 🌍

#CambioClimático #ActúaYa"""
        },
        
        "facebook": {
            "profesional": f"""Estimados amigos de GeobizIA,

Nos complace invitarles a {nombre}, una {tipo.lower()} que organizaremos próximamente.

{frase_motivadora}. Esta iniciativa, dirigida por {responsable}, tendrá una duración de {duracion} y promete ser muy enriquecedora.

Los detalles completos los compartiremos pronto. ¡Esperamos contar con su participación!

#MedioAmbiente #GeobizIA""",
            
            "cercano": f"""¡Hola queridos amigos! 😊

Queremos contarles sobre algo emocionante: ¡{nombre}!

{frase_motivadora} y creemos que les va a encantar participar.

{responsable} será quien nos acompañe en esta aventura verde. ¿Quién se apunta?

¡Comenten si están interesados! 💚""",
            
            "motivacional": f"""🌍 ¡ATENCIÓN TODOS! 🌍

{nombre.upper()} está llegando y va a ser ÉPICO.

{frase_motivadora} - ¡Es AHORA o NUNCA!

Con {responsable} al frente, esta {tipo.lower()} va a cambiar tu perspectiva sobre el medio ambiente.

¿ESTÁS LISTO PARA EL DESAFÍO? 💪

#CambioClimático #AcciónAhora"""
        },
        
        "twitter": {
            "profesional": f"""{emoji} Próximamente: {nombre}

{frase_motivadora}

👨‍🏫 {responsable}
⏰ {duracion}

#Sostenibilidad #GeobizIA""",
            
            "cercano": f"""¡Hey! 👋 

{nombre} está por llegar {emoji}

{frase_motivadora} ¿Te unes? 💚

#EcoLife #GeobizIA""",
            
            "motivacional": f"""🚨 {nombre.upper()} 🚨

{frase_motivadora}

¡El planeta te NECESITA! 🌍💪

#ActúaYa #CambioClimático"""
        }
    }
    
    return plantillas[request.plataforma][request.tono]

def generar_durante(nombre, asistentes, observaciones, request):
    """Genera contenido mientras se realiza la actividad"""
    
    asistentes_texto = f"{asistentes} personas increíbles" if asistentes else "un grupo fantástico"
    
    plantillas = {
        "instagram": {
            "profesional": f"""🔴 EN VIVO: {nombre}

Actualmente desarrollando esta importante actividad con {asistentes_texto}.

📊 Progreso excelente
👥 Participación activa  
🎯 Objetivos en camino

#EnVivo #Sostenibilidad #GeobizIA""",
            
            "cercano": f"""¡Estamos en plena acción! 💪

{nombre} está siendo increíble con {asistentes_texto} 🔥

La energía es contagiosa y todos están súper motivados. ¡Os seguimos contando!

Stories más tarde 📸""",
            
            "motivacional": f"""🔥 ¡ESTO ESTÁ PASANDO AHORA! 🔥

{nombre.upper()} en plena acción con {asistentes_texto}

⚡ Energía AL MÁXIMO
🎯 Objetivos CUMPLIDOS
💪 Poder del equipo IMPARABLE

#LiveAction #CambioReal"""
        },
        
        "facebook": {
            "profesional": f"""📍 Actualización en tiempo real

{nombre} se está desarrollando exitosamente con la participación de {asistentes_texto}.

La respuesta ha sido excelente y estamos cumpliendo todos los objetivos planificados. Seguiremos informando sobre los avances.

#GeobizIA #MedioAmbiente""",
            
            "cercano": f"""¡Hola desde {nombre}! 👋

Estamos aquí con {asistentes_texto} pasándolo genial y aprendiendo un montón 😊

El ambiente es súper bueno y todos están muy participativos. ¡Esto es lo que necesitábamos!

¡Ya os contaremos todo! 💚""",
            
            "motivacional": f"""🚨 ¡ESTO ESTÁ OCURRIENDO AHORA MISMO! 🚨

{nombre} en PLENA ACCIÓN con {asistentes_texto}

La ENERGÍA es INCREÍBLE. Esto es lo que pasa cuando las personas se unen por el planeta 🌍

¡EL CAMBIO ES REAL Y ESTÁ PASANDO! 💪

#ChangeIsNow #PlanetAction"""
        },
        
        "twitter": {
            "profesional": f"""🔴 {nombre} en curso

{asistentes_texto} participando activamente

Excelente desarrollo 👍

#EnVivo #Sostenibilidad""",
            
            "cercano": f"""¡En plena acción! 💪

{nombre} con {asistentes_texto} 🔥

¡La energía es increíble! 💚

#EcoAction""",
            
            "motivacional": f"""🔥 ¡AHORA MISMO! 🔥

{nombre.upper()}

{asistentes_texto} CAMBIANDO EL MUNDO 🌍💪

#ActuaYa"""
        }
    }
    
    return plantillas[request.plataforma][request.tono]

def generar_completado(nombre, fecha, asistentes, observaciones, request):
    """Genera contenido celebrando actividad completada"""
    
    asistentes_texto = f"{asistentes} participantes" if asistentes else "nuestros participantes"
    logros = observaciones if observaciones else "resultados excelentes"
    
    plantillas = {
        "instagram": {
            "profesional": f"""✅ COMPLETADO: {nombre}

¡Actividad finalizada con gran éxito!

🎯 Participaron {asistentes_texto}
📈 {logros}
🌟 Objetivos superados

Gracias a todos por hacer posible este cambio positivo.

#Completado #Éxito #GeobizIA #Sostenibilidad""",
            
            "cercano": f"""¡Y eso es todo amigos! 🎉

{nombre} ha terminado y ha sido INCREÍBLE 💚

{asistentes_texto} maravillosos que han hecho que todo sea especial ✨

{logros} y muchas sonrisas después... ¡MISIÓN CUMPLIDA!

¡Gracias por la buena energía! 🤗""",
            
            "motivacional": f"""🏆 ¡MISIÓN CUMPLIDA! 🏆

{nombre.upper()} = ¡ÉXITO TOTAL!

🎉 {asistentes_texto} INCREÍBLES
💯 {logros}  
🚀 ¡Ya pensando en la SIGUIENTE!

¡ESTO ES LO QUE PASA CUANDO NOS UNIMOS! 💪🌍

#MisiónCumplida #CambioReal #Imparables"""
        },
        
        "facebook": {
            "profesional": f"""✅ {nombre} - Actividad completada exitosamente

Nos complace informar que la actividad se ha desarrollado de manera excelente, contando con la participación de {asistentes_texto}.

Destacamos: {logros}

Agradecemos profundamente a todos los participantes por su compromiso y entusiasmo. Iniciativas como esta nos demuestran que juntos podemos lograr un impacto positivo real.

¡Hasta la próxima actividad!

#GeobizIA #MedioAmbiente #Comunidad""",
            
            "cercano": f"""¡Qué día más especial hemos tenido! 😊

{nombre} se ha completado y estamos súper contentos con los resultados. {asistentes_texto} fantásticos han participado y la verdad es que hemos conseguido {logros.lower()}.

Es genial ver cómo cuando nos juntamos por una buena causa, las cosas salen increíbles 💚

¡Muchas gracias a todos! Ya estamos pensando en la próxima 😉""",
            
            "motivacional": f"""🎊 ¡BOMBAZO DE ACTIVIDAD COMPLETADA! 🎊

{nombre.upper()} ha sido un ÉXITO ROTUNDO

👏 {asistentes_texto} VALIENTES que dijeron SÍ al cambio
🔥 {logros}
💪 Demostrado: ¡JUNTOS SOMOS IMPARABLES!

Esto NO termina aquí. ¡El planeta nos necesita y NOSOTROS RESPONDEMOS!

¿QUIÉN SE APUNTA A LA SIGUIENTE REVOLUCIÓN VERDE? 🌍

#RevolucionVerde #JuntosSomosImparables"""
        },
        
        "twitter": {
            "profesional": f"""✅ {nombre} completado

{asistentes_texto} participaron
{logros}

¡Gracias por el compromiso! 💚

#Sostenibilidad #GeobizIA""",
            
            "cercano": f"""¡Ya está! 🎉

{nombre} completado con {asistentes_texto} geniales 💚

{logros} ¡Gracias equipo! 🤗

#EcoTeam""",
            
            "motivacional": f"""🏆 ¡COMPLETADO! 🏆

{nombre.upper()}

{asistentes_texto} CAMBIANDO EL MUNDO 🌍

¡IMPARABLES! 💪🔥

#CambioReal"""
        }
    }
    
    return plantillas[request.plataforma][request.tono]

def generar_hashtags(actividad, request):
    """Genera hashtags relevantes e inteligentes"""
    hashtags_base = ["#GeobizIA"]
    
    # Hashtags por tipo de actividad (análisis inteligente)
    nombre_lower = actividad.nombre.lower()
    tipo_lower = (actividad.tipo or "").lower()
    descripcion_lower = (actividad.descripcion or "").lower()
    
    todo_texto = f"{nombre_lower} {tipo_lower} {descripcion_lower}"
    
    # Categorías temáticas
    if any(palabra in todo_texto for palabra in ["reciclaje", "recicl", "residuo", "basura"]):
        hashtags_base.extend(["#Reciclaje", "#EconomiaCircular", "#ZeroWaste"])
    
    if any(palabra in todo_texto for palabra in ["planta", "árbol", "reforest", "siembra", "verde"]):
        hashtags_base.extend(["#Reforestacion", "#PlantarArboles", "#VidaVerde"])
    
    if any(palabra in todo_texto for palabra in ["limpieza", "limpiar", "basura", "residuo"]):
        hashtags_base.extend(["#LimpiezaAmbiental", "#CuidemosElPlaneta"])
    
    if any(palabra in todo_texto for palabra in ["energia", "solar", "eolica", "renovable"]):
        hashtags_base.extend(["#EnergiaRenovable", "#EnergiaLimpia", "#Sustentabilidad"])
    
    if any(palabra in todo_texto for palabra in ["agua", "hidrico", "mar", "rio", "océano"]):
        hashtags_base.extend(["#CuidarElAgua", "#RecursoHidrico", "#AguaLimpia"])
    
    if any(palabra in todo_texto for palabra in ["taller", "workshop", "curso", "formacion"]):
        hashtags_base.extend(["#Educacion", "#TallerAmbiental", "#Formacion"])
    
    if any(palabra in todo_texto for palabra in ["conferencia", "charla", "seminario"]):
        hashtags_base.extend(["#ConcienciaAmbiental", "#EducacionAmbiental"])
    
    # Hashtags temáticos generales
    hashtags_base.extend(["#MedioAmbiente", "#Sostenibilidad"])
    
    # Hashtags por tipo de publicación
    if request.tipo_publicacion == "anuncio":
        hashtags_base.extend(["#Proximamente", "#Apuntate", "#NoTeLoPierdas"])
    elif request.tipo_publicacion == "durante":
        hashtags_base.extend(["#EnVivo", "#Ahora", "#LiveAction"])
    elif request.tipo_publicacion == "completado":
        hashtags_base.extend(["#Completado", "#Exito", "#MisionCumplida"])
    
    # Hashtags específicos por plataforma
    if request.plataforma == "instagram":
        hashtags_base.extend(["#EcoFriendly", "#GreenLife", "#NaturalezaLovers", "#EcoWarrior"])
    elif request.plataforma == "twitter":
        hashtags_base.extend(["#ClimateAction", "#EcoTech", "#GreenTech"])
    elif request.plataforma == "facebook":
        hashtags_base.extend(["#ComunidadVerde", "#JuntosPorelPlaneta"])
    
    # Hashtags por tono
    if request.tono == "motivacional":
        hashtags_base.extend(["#CambioClimático", "#AccionAhora", "#Imparables"])
    elif request.tono == "cercano":
        hashtags_base.extend(["#EcoAmigos", "#VidaVerde", "#NaturalezaAmica"])
    elif request.tono == "profesional":
        hashtags_base.extend(["#ResponsabilidadSocial", "#DesarrolloSostenible"])
    
    # Eliminar duplicados y limitar cantidad
    hashtags_unicos = list(dict.fromkeys(hashtags_base))  # Preserva orden y elimina duplicados
    
    # Diferentes límites por plataforma
    limite = {
        "instagram": 10,  # Instagram permite hasta 30, pero 10 es más efectivo
        "twitter": 5,     # Twitter es más limitado en caracteres
        "facebook": 8     # Facebook prefiere menos hashtags
    }.get(request.plataforma, 8)
    
    return " ".join(hashtags_unicos[:limite])

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
