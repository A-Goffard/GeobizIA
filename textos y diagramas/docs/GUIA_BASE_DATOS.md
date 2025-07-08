# 🗄️ GUÍA DE GESTIÓN DE BASE DE DATOS

## 📋 Resumen

Esta guía explica cómo gestionar completamente la base de datos de GeobizIA usando los scripts Python proporcionados.

---

## 🏗️ CREAR BASE DE DATOS

### 1. Crear estructura completa

```bash
python GeobizIA/modelo/database/create/create_db_tables.py
```

**¿Qué hace?**
- Crea la base de datos `GeobizIAPruebas` (si no existe)
- Crea todas las tablas según el MER
- Configura las relaciones y restricciones
- Normalización 3FN aplicada

**Salida esperada:**
```
Tablas creadas/verificadas.
```

---

## 📊 INSERTAR DATOS DE PRUEBA

### 2. Poblar con datos de ejemplo

```bash
python GeobizIA/modelo/database/create/insertar_datos_prueba.py
```

**¿Qué hace?**
- Inserta datos de ejemplo en todas las tablas
- Datos coherentes para testing
- Permite probar la API inmediatamente

**Salida esperada:**
```
Datos de prueba insertados correctamente.
```

---

## 🗑️ ELIMINAR BASE DE DATOS

### 3. Gestión de eliminación

```bash
python GeobizIA/modelo/database/create/eliminar_base_datos.py
```

**¿Qué hace?**
- **Opción 1**: Elimina la base de datos completa (IRREVERSIBLE)
- **Opción 2**: Limpia solo los datos (mantiene estructura)
- **Opción 3**: Cancelar operación

**Menú interactivo:**
```
🗑️  GESTIÓN DE ELIMINACIÓN - GeobizIA
====================================
1. 💥 Eliminar base de datos completa (IRREVERSIBLE)
2. 🧹 Limpiar solo datos (mantiene estructura)
3. ❌ Cancelar y salir
```

### ⚠️ ADVERTENCIAS DE SEGURIDAD

- **Eliminación completa**: Requiere escribir `ELIMINAR` para confirmar
- **Limpieza de datos**: Requiere escribir `LIMPIAR` para confirmar
- **Backups**: Siempre haz backup antes de eliminar

---

## 🔄 FLUJOS DE TRABAJO TÍPICOS

### 🏃 Inicio rápido (primera vez):

```bash
# 1. Crear base de datos y tablas
python GeobizIA/modelo/database/create/create_db_tables.py

# 2. Insertar datos de prueba
python GeobizIA/modelo/database/create/insertar_datos_prueba.py

# 3. Arrancar la API
cd GeobizIA/api
uvicorn main:app --reload
```

### 🔄 Resetear datos (conservar estructura):

```bash
# 1. Limpiar datos existentes
python GeobizIA/modelo/database/create/eliminar_base_datos.py
# Seleccionar opción 2 (limpiar datos)

# 2. Insertar datos frescos
python GeobizIA/modelo/database/create/insertar_datos_prueba.py
```

### 🆕 Empezar desde cero:

```bash
# 1. Eliminar base de datos completa
python GeobizIA/modelo/database/create/eliminar_base_datos.py
# Seleccionar opción 1 (eliminar todo)

# 2. Recrear estructura
python GeobizIA/modelo/database/create/create_db_tables.py

# 3. Insertar datos de prueba
python GeobizIA/modelo/database/create/insertar_datos_prueba.py
```

---

## 📁 ARCHIVOS INVOLUCRADOS

### Scripts Python:
- `create_db_tables.py` - Crear BD y tablas
- `insertar_datos_prueba.py` - Insertar datos de ejemplo
- `eliminar_base_datos.py` - Eliminar BD o datos

### Archivos SQL:
- `queries_creacion_tablas.sql` - Estructura de tablas
- `queries_ejemplo_pruebas.sql` - Datos de ejemplo
- `queries_limpiar_datos.sql` - Limpieza de datos

### Configuración:
- `config/constantes_conexion.py` - Configuración de conexión
- `db_conexion.py` - Gestión de conexiones

---

## 🛠️ SOLUCIÓN DE PROBLEMAS

### Error: "Database does not exist"
```bash
# Ejecutar primero:
python GeobizIA/modelo/database/create/create_db_tables.py
```

### Error: "Foreign key constraint"
```bash
# Los datos pueden tener dependencias. Usar:
python GeobizIA/modelo/database/create/eliminar_base_datos.py
# Opción 2 (limpiar datos) - respeta las dependencias
```

### Error: "Connection refused"
```bash
# Verificar configuración en:
GeobizIA/modelo/database/config/constantes_conexion.py
```

### Error: "Table already exists"
```bash
# Es normal - el script ignora tablas existentes
# No es un error, es protección
```

### Error: "El nombre de objeto 'tabla' no es válido"
```bash
# Es normal - el script intenta eliminar todas las tablas posibles
# Las que no existen generan este error, pero no es problemático
# El script continúa limpiando las tablas que sí existen
```

### Verificar qué tablas existen realmente
```bash
# El script mejorado muestra automáticamente las tablas encontradas
# y solo opera sobre las que realmente existen
```

---

## 🎯 PARA LA DEFENSA

### Preguntas esperadas:

**P: "¿Cómo gestionas la base de datos?"**
**R:** "Tengo scripts separados para crear, poblar y eliminar. Cada uno con su responsabilidad específica, siguiendo el principio de responsabilidad única."

**P: "¿Qué pasa si ejecuto el script dos veces?"**
**R:** "Los scripts son idempotentes. `create_db_tables.py` solo crea si no existe, `insertar_datos_prueba.py` maneja duplicados."

**P: "¿Cómo reseteas los datos para testing?"**
**R:** "Uso `eliminar_base_datos.py` opción 2 para limpiar datos manteniendo estructura, luego `insertar_datos_prueba.py` para datos frescos."

---

## 📊 VENTAJAS DEL ENFOQUE

✅ **Automatización completa**: Sin SQL manual  
✅ **Seguridad**: Confirmaciones para operaciones destructivas  
✅ **Flexibilidad**: Eliminar todo o solo datos  
✅ **Mantenibilidad**: Scripts modulares y reutilizables  
✅ **Documentación**: Cada script explica qué hace  
✅ **Idempotencia**: Ejecutar múltiples veces no causa problemas  

---

## 🔗 ARCHIVOS RELACIONADOS

- `README.md` - Documentación principal del proyecto
- `EXPLICACION_TECNICA.md` - Detalles técnicos completos
- `ARQUITECTURA_SOLID.md` - Principios de arquitectura aplicados
