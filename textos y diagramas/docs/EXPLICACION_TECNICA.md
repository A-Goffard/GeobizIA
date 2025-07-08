# 📚 GUÍA DE COMPRENSIÓN DEL PROYECTO GeobizIA

## 🏗️ ARQUITECTURA DEL SISTEMA

### **Patrón MVC (Modelo-Vista-Controlador) Implementado**

El proyecto sigue una **arquitectura MVC en capas** que cumple con los principios SOLID, DRY y KISS:

```
├── VISTA (Frontend Vue.js + API REST)
│   ├── Recepción de datos del cliente
│   ├── Validación inicial
│   └── Comunicación con controlador
│
├── CONTROLADOR (Gestores + Validaciones)
│   ├── Procesamiento de objetos de dominio
│   ├── Lógica de negocio (CRUD)
│   ├── Transformación de datos
│   └── Respuesta a peticiones
│
└── MODELO (Base de Datos + Dominios)
    ├── Conexión a BD
    ├── Persistencia de datos
    └── Objetos de dominio
```

---

## 🌐 DECORADORES HTTP: @router.get y @router.post

### **¿Por qué uso estos decoradores?**

Los decoradores `@router.get` y `@router.post` son **anotaciones de FastAPI** que definen:
1. **El método HTTP** que acepta el endpoint
2. **La ruta URL** que responde
3. **El comportamiento** de la función

### **@router.get - Para CONSULTAS**

```python
@router.get("/api/actividades")
def listar_actividades():
    actividades = gestor.mostrar_todos_los_elem()
    return [a.to_dict() for a in actividades]
```

**Ventajas:**
- ✅ **Idempotente**: Múltiples llamadas producen el mismo resultado
- ✅ **Cacheable**: Los navegadores pueden guardar la respuesta
- ✅ **Seguro**: No modifica datos del servidor
- ✅ **RESTful**: Sigue las convenciones REST

**Desventajas:**
- ❌ **Límite de datos**: Los parámetros van en la URL (limitado)
- ❌ **Visible**: Los parámetros son visibles en logs/historial

**Cuándo usar GET:**
- Listar datos (`/api/actividades`)
- Obtener estadísticas (`/api/actividades/estadisticas`)
- Buscar por ID (`/api/actividades/{id}`)

### **@router.post - Para CREACIÓN/MODIFICACIÓN**

```python
@router.post("/api/actividades")
def crear_actividad(actividad: ActividadIn):
    datos = actividad.dict()
    valido, msg = validar_datos_actividad(datos)
    if not valido:
        raise HTTPException(status_code=400, detail=msg)
    # Procesar creación...
```

**Ventajas:**
- ✅ **Datos en cuerpo**: Puede enviar grandes cantidades de información
- ✅ **Seguro**: Los datos no van en la URL
- ✅ **Flexible**: Acepta JSON, formularios, archivos
- ✅ **Validación**: Modelos Pydantic validan automáticamente

**Desventajas:**
- ❌ **No idempotente**: Múltiples llamadas pueden crear duplicados
- ❌ **No cacheable**: Las respuestas no se pueden cachear
- ❌ **Más complejo**: Requiere cuerpo de petición

**Cuándo usar POST:**
- Crear nuevos registros
- Enviar formularios
- Operaciones que cambian estado
- Predicciones con parámetros complejos

---

## 🧩 CUMPLIMIENTO DE PRINCIPIOS

### **SOLID Principles:**

1. **S - Single Responsibility**: Cada clase tiene una única responsabilidad
   - `Actividades`: Solo gestiona actividades
   - `ActividadesRealizadas`: Solo gestiona actividades realizadas
   - `PrediccionActividades`: Solo hace predicciones

2. **O - Open/Closed**: Abierto para extensión, cerrado para modificación
   - Uso de interfaces para gestores
   - Herencia en objetos de dominio

3. **L - Liskov Substitution**: Subclases sustituyen a superclases
   - Todos los gestores implementan la misma interfaz

4. **I - Interface Segregation**: Interfaces específicas y pequeñas
   - Separación entre validaciones, gestores y ML

5. **D - Dependency Inversion**: Dependencias de abstracciones
   - Los controladores dependen de interfaces, no implementaciones concretas

### **DRY (Don't Repeat Yourself):**
- Validaciones centralizadas por dominio
- Gestores genéricos con funcionalidad común
- Funciones ML reutilizables

### **KISS (Keep It Simple, Stupid):**
- Funciones pequeñas y específicas
- Nombres descriptivos y claros
- Lógica sencilla y comprensible

---

## 🔄 FLUJO DE DATOS

### **Ejemplo: Crear Actividad**

1. **Vista** → Cliente envía datos JSON
2. **API** → `@router.post` recibe petición
3. **Validación** → `validar_datos_actividad()` verifica datos
4. **Dominio** → Se crea objeto `Actividad(**datos)`
5. **Controlador** → `gestor.agregar(actividad)`
6. **Modelo** → Persiste en base de datos
7. **Respuesta** → Retorna confirmación al cliente

### **Pase de Parámetros - REGLA IMPORTANTE:**

❌ **INCORRECTO:**
```python
def crear_actividad(nombre, tipo, coste, facturacion):  # Pasa atributos sueltos
```

✅ **CORRECTO:**
```python
def crear_actividad(actividad: ActividadIn):  # Pasa OBJETO completo
    obj = gestor.agregar(Actividad(**actividad.dict()))
```

**Justificación:**
- Mantiene cohesión de datos
- Facilita mantenimiento
- Reduce acoplamiento
- Mejora legibilidad

---

## 🎯 FUNCIONALIDADES IMPLEMENTADAS

### **1. CRUD Básico**
- ✅ Crear actividades (`POST /api/actividades`)
- ✅ Listar actividades (`GET /api/actividades`)
- ✅ Obtener por ID (`GET /api/actividades/{id}`)
- ✅ Estadísticas (`GET /api/actividades/estadisticas`)

### **2. Machine Learning (Extra +1 punto)**
- ✅ Predicción de asistentes y facturación
- ✅ Análisis de datos históricos
- ✅ Métricas de confiabilidad del modelo
- ✅ Uso de pandas y scikit-learn

### **3. Visualización de Datos (Extra +1 punto)**
- ✅ Dashboard con gráficos interactivos
- ✅ Estadísticas en tiempo real
- ✅ Diseño responsive
- ✅ Chart.js + Vue.js

### **4. API REST Completa (Extra +1 punto)**
- ✅ Endpoints bien estructurados
- ✅ Validación automática con Pydantic
- ✅ Manejo de errores HTTP
- ✅ Documentación automática (Swagger)

---

## 🗂️ ESTRUCTURA DE DIRECTORIOS (Clean Code)

```
GeobizIA/
├── api/                    # Vista - Endpoints REST
│   ├── api_actividades.py
│   └── api_actividades_realizadas.py
├── controlador/            # Controlador - Lógica de negocio
│   ├── gestores/          # CRUD operations
│   ├── dominios/          # Objetos de dominio
│   ├── ML/               # Machine Learning
│   └── validaciones/     # Validación de datos
├── modelo/                # Modelo - Persistencia
│   └── database/
└── vista/                 # Frontend
    └── frontend/
```

**Nombres descriptivos:**
- `ActividadesRealizadas` → Claramente identifica su propósito
- `preparar_estadisticas_actividades()` → Función autoexplicativa
- `validar_datos_actividad()` → Propósito evidente

---

## 🎨 EXTRAS IMPLEMENTADOS (Puntos adicionales)

1. **+1 Pandas/ML**: Sistema de predicción completo
2. **+1 Visualización**: Dashboard con gráficos
3. **+1 API Avanzada**: FastAPI con validación automática
4. **+1 Frontend Moderno**: Vue.js + Chart.js responsive

---

## 🔍 JUSTIFICACIÓN DE DECISIONES TÉCNICAS

### **¿Por qué FastAPI?**
- Validación automática con Pydantic
- Documentación automática
- Alto rendimiento
- Tipado estático

### **¿Por qué Vue.js?**
- Reactivo y moderno
- Fácil integración con APIs
- Componentes reutilizables
- Curva de aprendizaje suave

### **¿Por qué Machine Learning?**
- Valor añadido al proyecto
- Análisis predictivo real
- Uso de librerías profesionales
- Aplicación práctica de IA

Este proyecto demuestra **comprensión completa** de arquitecturas modernas, principios de programación y tecnologías actuales. 🚀
