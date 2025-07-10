<template>
    <div class="generador-container">
        <h1>🤖 Generador de Publicaciones IA</h1>
        <p class="subtitle">Crea contenido automático para redes sociales basado en tus actividades</p>
        
        <div class="form-section">
            <div class="form-grid">
                <!-- Selección de actividad -->
                <div class="form-group">
                    <label for="actividad">📋 Actividad Realizada:</label>
                    <select id="actividad" v-model="formData.id_actividad_realizada" required>
                        <option value="">Selecciona una actividad...</option>
                        <option v-for="act in actividadesRealizadas" 
                                :key="act.id_actividad_realizada" 
                                :value="act.id_actividad_realizada">
                            {{ act.nombre_actividad }} - {{ formatDate(act.fecha) }}
                        </option>
                    </select>
                </div>
                
                <!-- Tipo de publicación -->
                <div class="form-group">
                    <label>📢 Tipo de Publicación:</label>
                    <div class="radio-group">
                        <label class="radio-item">
                            <input type="radio" v-model="formData.tipo_publicacion" value="anuncio">
                            <span class="radio-custom"></span>
                            📢 Anunciar próxima actividad
                        </label>
                        <label class="radio-item">
                            <input type="radio" v-model="formData.tipo_publicacion" value="durante">
                            <span class="radio-custom"></span>
                            🎯 Durante el evento
                        </label>
                        <label class="radio-item">
                            <input type="radio" v-model="formData.tipo_publicacion" value="completado">
                            <span class="radio-custom"></span>
                            ✅ Actividad completada
                        </label>
                    </div>
                </div>
                
                <!-- Opciones de estilo -->
                <div class="form-group">
                    <label for="tono">🎨 Tono:</label>
                    <select id="tono" v-model="formData.tono">
                        <option value="profesional">👔 Profesional</option>
                        <option value="cercano">😊 Cercano</option>
                        <option value="motivacional">🔥 Motivacional</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="plataforma">📱 Plataforma:</label>
                    <select id="plataforma" v-model="formData.plataforma">
                        <option value="instagram">📷 Instagram</option>
                        <option value="facebook">👥 Facebook</option>
                        <option value="twitter">🐦 Twitter</option>
                    </select>
                </div>
                
                <!-- Opciones adicionales -->
                <div class="form-group checkbox-group">
                    <label class="checkbox-item">
                        <input type="checkbox" v-model="formData.incluir_hashtags">
                        <span class="checkbox-custom"></span>
                        #️⃣ Incluir hashtags
                    </label>
                </div>
            </div>
            
            <div class="action-section">
                <button 
                    @click="generarPublicacion" 
                    :disabled="!puedeGenerar || isGenerating"
                    class="generate-btn"
                >
                    <span v-if="isGenerating">🔄 Generando...</span>
                    <span v-else>✨ Generar Publicación IA</span>
                </button>
            </div>
        </div>
        
        <!-- Resultado -->
        <div v-if="publicacionGenerada" class="resultado-section">
            <h3>📱 Tu Publicación Generada</h3>
            <div class="publicacion-preview">
                <div class="preview-header">
                    <div class="avatar">🌱</div>
                    <div class="profile-info">
                        <strong>GeobizIA</strong>
                        <span class="plataforma-badge">{{ formData.plataforma }}</span>
                    </div>
                    <div class="timestamp">Ahora</div>
                </div>
                
                <div class="preview-content">
                    <p class="contenido-principal">{{ publicacionGenerada.contenido }}</p>
                    <p v-if="publicacionGenerada.hashtags" class="hashtags">{{ publicacionGenerada.hashtags }}</p>
                </div>
                
                <div class="preview-stats">
                    <span class="caracteres">{{ publicacionGenerada.caracteres }} caracteres</span>
                    <span class="plataforma-limite">
                        {{ getLimiteCaracteres(formData.plataforma) }}
                    </span>
                </div>
                
                <div class="preview-actions">
                    <button @click="copiarTexto" class="action-btn copy">
                        📋 Copiar
                    </button>
                    <button @click="editarPublicacion" class="action-btn edit">
                        ✏️ Editar
                    </button>
                    <button @click="regenerarPublicacion" class="action-btn regenerate">
                        🔄 Regenerar
                    </button>
                    <button @click="guardarPublicacion" class="action-btn save">
                        💾 Guardar
                    </button>
                </div>
            </div>
        </div>
        
        <!-- Modal de edición -->
        <div v-if="mostrarModalEdicion" class="modal-overlay" @click="cerrarModalEdicion">
            <div class="modal-content" @click.stop>
                <h3>✏️ Editar Publicación</h3>
                <textarea v-model="textoEditado" class="editor-textarea"></textarea>
                <div class="modal-actions">
                    <button @click="aplicarEdicion" class="btn-primary">💾 Aplicar</button>
                    <button @click="cerrarModalEdicion" class="btn-secondary">❌ Cancelar</button>
                </div>
            </div>
        </div>
        
        <!-- Mensajes -->
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <div v-if="successMessage" class="success-message">{{ successMessage }}</div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

// Estado reactivo
const actividadesRealizadas = ref([])
const publicacionGenerada = ref(null)
const isGenerating = ref(false)
const errorMessage = ref('')
const successMessage = ref('')
const mostrarModalEdicion = ref(false)
const textoEditado = ref('')

const formData = ref({
    id_actividad_realizada: '',
    tipo_publicacion: 'completado',
    tono: 'profesional',
    plataforma: 'instagram',
    incluir_hashtags: true
})

// Computed
const puedeGenerar = computed(() => {
    return formData.value.id_actividad_realizada && 
           formData.value.tipo_publicacion &&
           formData.value.tono &&
           formData.value.plataforma
})

// Métodos
onMounted(async () => {
    await cargarActividades()
})

async function cargarActividades() {
    try {
        const response = await fetch('http://localhost:8000/api/ia/actividades-realizadas')
        if (response.ok) {
            actividadesRealizadas.value = await response.json()
        } else {
            throw new Error('Error al cargar actividades')
        }
    } catch (error) {
        errorMessage.value = 'Error al cargar las actividades realizadas'
        console.error(error)
    }
}

async function generarPublicacion() {
    isGenerating.value = true
    errorMessage.value = ''
    successMessage.value = ''
    
    try {
        const response = await fetch('http://localhost:8000/api/ia/generar-publicacion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData.value)
        })
        
        if (response.ok) {
            publicacionGenerada.value = await response.json()
            successMessage.value = '✅ Publicación generada exitosamente'
        } else {
            const errorData = await response.json()
            throw new Error(errorData.detail || 'Error al generar publicación')
        }
    } catch (error) {
        errorMessage.value = error.message
        console.error(error)
    } finally {
        isGenerating.value = false
    }
}

async function regenerarPublicacion() {
    await generarPublicacion()
}

function copiarTexto() {
    const textoCompleto = publicacionGenerada.value.contenido + 
                         (publicacionGenerada.value.hashtags ? '\n\n' + publicacionGenerada.value.hashtags : '')
    
    navigator.clipboard.writeText(textoCompleto).then(() => {
        successMessage.value = '📋 Texto copiado al portapapeles'
        setTimeout(() => successMessage.value = '', 3000)
    }).catch(() => {
        errorMessage.value = 'Error al copiar el texto'
    })
}

function editarPublicacion() {
    textoEditado.value = publicacionGenerada.value.contenido
    mostrarModalEdicion.value = true
}

function cerrarModalEdicion() {
    mostrarModalEdicion.value = false
    textoEditado.value = ''
}

function aplicarEdicion() {
    if (publicacionGenerada.value) {
        publicacionGenerada.value.contenido = textoEditado.value
        publicacionGenerada.value.caracteres = textoEditado.value.length + 
                                             (publicacionGenerada.value.hashtags?.length || 0)
    }
    cerrarModalEdicion()
    successMessage.value = '✏️ Publicación editada'
    setTimeout(() => successMessage.value = '', 3000)
}

function guardarPublicacion() {
    // Aquí se implementaría la lógica para guardar en la base de datos
    successMessage.value = '💾 Publicación guardada (función pendiente de implementar)'
    setTimeout(() => successMessage.value = '', 3000)
}

function formatDate(dateString) {
    if (!dateString) return 'N/A'
    try {
        return new Date(dateString).toLocaleDateString('es-ES')
    } catch {
        return dateString
    }
}

function getLimiteCaracteres(plataforma) {
    const limites = {
        'twitter': 'Límite: 280 caracteres',
        'instagram': 'Límite: 2,200 caracteres',
        'facebook': 'Límite: 63,206 caracteres'
    }
    return limites[plataforma] || ''
}
</script>

<style scoped>
.generador-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 7rem 2rem 2rem 2rem;
}

.generador-container h1 {
    text-align: center;
    margin-bottom: 0.5rem;
    font-size: 2.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #666;
    margin-bottom: 3rem;
    font-size: 1.1rem;
}

.form-section {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
}

.form-group {
    display: flex;
    flex-direction: column;
}

.form-group label {
    margin-bottom: 0.8rem;
    font-weight: 600;
    color: #2c3e50;
    font-size: 1.1rem;
}

.form-group select,
.form-group input {
    padding: 1rem;
    border: 2px solid #e1e8ed;
    border-radius: 10px;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group select:focus,
.form-group input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.radio-group {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.radio-item {
    display: flex;
    align-items: center;
    padding: 1rem;
    border: 2px solid #e1e8ed;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.radio-item:hover {
    border-color: #667eea;
    background-color: #f8f9ff;
}

.radio-item input[type="radio"] {
    margin-right: 0.8rem;
    transform: scale(1.2);
}

.checkbox-group .checkbox-item {
    display: flex;
    align-items: center;
    padding: 1rem;
    border: 2px solid #e1e8ed;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.checkbox-item input[type="checkbox"] {
    margin-right: 0.8rem;
    transform: scale(1.2);
}

.action-section {
    text-align: center;
}

.generate-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 1.2rem 3rem;
    border-radius: 25px;
    font-size: 1.2rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

.generate-btn:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.generate-btn:disabled {
    background: #bdc3c7;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.resultado-section {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.resultado-section h3 {
    text-align: center;
    margin-bottom: 2rem;
    color: #2c3e50;
}

.publicacion-preview {
    max-width: 500px;
    margin: 0 auto;
    border: 1px solid #e1e8ed;
    border-radius: 15px;
    overflow: hidden;
    background: white;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.preview-header {
    display: flex;
    align-items: center;
    padding: 1rem;
    border-bottom: 1px solid #e1e8ed;
    background: #f8f9fa;
}

.avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-right: 1rem;
}

.profile-info {
    flex: 1;
}

.profile-info strong {
    display: block;
    font-size: 1.1rem;
}

.plataforma-badge {
    display: inline-block;
    background: #667eea;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 12px;
    font-size: 0.8rem;
    margin-top: 0.2rem;
}

.timestamp {
    color: #657786;
    font-size: 0.9rem;
}

.preview-content {
    padding: 1.5rem;
}

.contenido-principal {
    margin: 0 0 1rem 0;
    line-height: 1.6;
    font-size: 1rem;
}

.hashtags {
    margin: 1rem 0 0 0;
    color: #1da1f2;
    font-weight: 500;
}

.preview-stats {
    padding: 0 1.5rem;
    display: flex;
    justify-content: space-between;
    font-size: 0.9rem;
    color: #657786;
    margin-bottom: 1rem;
}

.preview-actions {
    display: flex;
    border-top: 1px solid #e1e8ed;
    background: #f8f9fa;
}

.action-btn {
    flex: 1;
    padding: 0.8rem;
    border: none;
    background: transparent;
    cursor: pointer;
    transition: background-color 0.3s ease;
    font-size: 0.9rem;
}

.action-btn:hover {
    background-color: #e6f3ff;
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    max-width: 600px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
}

.editor-textarea {
    width: 100%;
    min-height: 200px;
    border: 2px solid #e1e8ed;
    border-radius: 10px;
    padding: 1rem;
    font-size: 1rem;
    resize: vertical;
    margin: 1rem 0;
}

.modal-actions {
    display: flex;
    gap: 1rem;
    justify-content: flex-end;
}

.btn-primary {
    background: #667eea;
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
}

.btn-secondary {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
}

.success-message {
    background: #d4edda;
    color: #155724;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    text-align: center;
}

.error-message {
    background: #f8d7da;
    color: #721c24;
    padding: 1rem;
    border-radius: 8px;
    margin-top: 1rem;
    text-align: center;
}

@media (max-width: 768px) {
    .generador-container {
        padding: 5rem 1rem 1rem 1rem;
    }
    
    .form-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .radio-group {
        gap: 0.8rem;
    }
    
    .generate-btn {
        padding: 1rem 2rem;
        font-size: 1rem;
    }
}
</style>
