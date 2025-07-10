# 🗺️ GUÍA: Cómo Acceder al Generador de Publicaciones IA

## 🎯 **3 FORMAS DE ACCEDER AL GENERADOR**

---

## 🏠 **OPCIÓN 1: Desde el Menú Principal**

### **Pasos**:
1. 🚀 Arrancar frontend: `npm run serve` (puerto 8080)
2. 🌐 Ir a: `http://localhost:8080`
3. 🔐 Hacer login si es necesario
4. 📱 Hacer clic en **"Opciones"**
5. 🤖 Buscar la tarjeta **"🤖 Generador IA"**
6. ✨ ¡Clic y a generar!

```
Inicio → Opciones → 🤖 Generador IA
```

---

## 📝 **OPCIÓN 2: Desde Publicaciones**

### **Pasos**:
1. 📱 En el menú principal, clic en **"Opciones"**
2. 📄 Clic en **"Publicaciones"**
3. 🤖 Buscar **"🤖 Generar con IA"**
4. ✨ ¡Clic y a generar!

```
Opciones → Publicaciones → 🤖 Generar con IA
```

---

## 🎯 **OPCIÓN 3: Acceso Directo (URL)**

### **URL Directa**:
```
http://localhost:8080/ia/generador-publicaciones
```

### **Para usar**:
1. 🚀 Asegurar que frontend está ejecutándose (puerto 8080)
2. 🚀 Asegurar que backend está ejecutándose (puerto 8000)
3. 🌐 Copiar y pegar la URL en el navegador
4. ✨ ¡Listo para generar!

---

## 🔧 **Verificación de Estado**

### **Backend (Puerto 8000)**:
```bash
# Terminal 1
cd GeobizIA
python -m uvicorn GeobizIA.api.main:app --reload --port 8000
```

**✅ Debe mostrar**: `Uvicorn running on http://0.0.0.0:8000`

### **Frontend (Puerto 8080)**:
```bash
# Terminal 2
cd GeobizIA/vista/frontend
npm run serve
```

**✅ Debe mostrar**: `Local: http://localhost:8080/`

---

## 🎪 **Navegación Visual**

```
🏠 INICIO (localhost:8080)
├── 🔐 Login (si es necesario)
├── 📱 Opciones
│   ├── 📄 Publicaciones
│   │   ├── Ver Publicaciones
│   │   ├── Agregar Publicación  
│   │   └── 🤖 Generar con IA ← ¡AQUÍ!
│   ├── 🎯 Actividades
│   ├── 💰 Facturas
│   ├── ... (otros módulos)
│   └── 🤖 Generador IA ← ¡O AQUÍ!
└── 🌐 URL Directa: /ia/generador-publicaciones ← ¡O DIRECTAMENTE!
```

---

## 🎯 **¿Qué Verás en el Generador?**

### **Formulario Inteligente**:
- 📋 **Actividad**: Selector de actividades realizadas
- 📢 **Tipo**: Anuncio / Durante / Completada  
- 🎨 **Tono**: Profesional / Cercano / Motivacional
- 📱 **Plataforma**: Instagram / Facebook / Twitter
- #️⃣ **Hashtags**: Sí / No

### **Resultado**:
- 🎨 **Vista previa** como red social
- 📊 **Contador** de caracteres
- 🔧 **Acciones**: Copiar / Editar / Regenerar / Guardar

---

## 🚨 **Solución de Problemas**

### **❌ "Página no encontrada"**
- ✅ Verificar que frontend está ejecutándose
- ✅ Verificar URL: `http://localhost:8080/ia/generador-publicaciones`

### **❌ "No aparece en el menú"**
- ✅ Refrescar página (Ctrl+F5)
- ✅ Verificar que estás en `/opciones`
- ✅ Buscar la tarjeta con emoji 🤖

### **❌ "Error al generar"**
- ✅ Verificar que backend está ejecutándose (puerto 8000)
- ✅ Verificar que hay actividades realizadas en la BD

---

## 🎉 **¡Disfruta Generando Contenido Increíble!**

**El generador está ahora perfectamente integrado en la aplicación y accesible desde múltiples puntos de navegación.**
