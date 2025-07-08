-- Limpieza de datos de GeobizIAPruebas
-- Este archivo elimina todos los datos pero mantiene la estructura de las tablas

-- ⚠️ ADVERTENCIA: Esta operación eliminará TODOS los datos de la base de datos
-- La estructura de las tablas se mantendrá intacta

-- Desactivar restricciones de clave foránea temporalmente
EXEC sp_MSforeachtable 'ALTER TABLE ? NOCHECK CONSTRAINT ALL';

-- Eliminar datos en orden inverso a las dependencias (de hijas a padres)
-- Esto evita errores de clave foránea

-- Tablas con relaciones múltiples (eliminar primero)
DELETE FROM actividad_realizada WHERE 1=1;
DELETE FROM actividad_evento WHERE 1=1;
DELETE FROM actividad_fecha WHERE 1=1;
DELETE FROM factura_actividad WHERE 1=1;
DELETE FROM proyecto_actividad WHERE 1=1;
DELETE FROM publicacion_tag WHERE 1=1;
DELETE FROM documento_tag WHERE 1=1;
DELETE FROM tema_ambiental_tag WHERE 1=1;
DELETE FROM tipo_publicacion_redsocial WHERE 1=1;
DELETE FROM plantilla_tipo_publicacion WHERE 1=1;
DELETE FROM auditoria_publicacion WHERE 1=1;
DELETE FROM log_sistema WHERE 1=1;
DELETE FROM participante WHERE 1=1;
DELETE FROM programacion WHERE 1=1;

-- Tablas principales (eliminar después)
DELETE FROM actividad WHERE 1=1;
DELETE FROM evento WHERE 1=1;
DELETE FROM proyecto WHERE 1=1;
DELETE FROM publicacion WHERE 1=1;
DELETE FROM documento WHERE 1=1;
DELETE FROM plantilla WHERE 1=1;
DELETE FROM recurso_multimedia WHERE 1=1;
DELETE FROM tag WHERE 1=1;
DELETE FROM tema_ambiental WHERE 1=1;
DELETE FROM tipo_publicacion WHERE 1=1;
DELETE FROM redsocial WHERE 1=1;
DELETE FROM factura WHERE 1=1;
DELETE FROM generadoria WHERE 1=1;
DELETE FROM fecha_actividad WHERE 1=1;

-- Tablas base (eliminar al final)
DELETE FROM cliente WHERE 1=1;
DELETE FROM empresa WHERE 1=1;
DELETE FROM persona WHERE 1=1;
DELETE FROM usuario WHERE 1=1;
DELETE FROM rol WHERE 1=1;

-- Reactivar restricciones de clave foránea
EXEC sp_MSforeachtable 'ALTER TABLE ? CHECK CONSTRAINT ALL';

-- Opcional: Reiniciar contadores de identidad
-- Descomenta las líneas siguientes si quieres que los IDs empiecen desde 1 otra vez

-- DBCC CHECKIDENT('actividad_realizada', RESEED, 0);
-- DBCC CHECKIDENT('actividad', RESEED, 0);
-- DBCC CHECKIDENT('evento', RESEED, 0);
-- DBCC CHECKIDENT('proyecto', RESEED, 0);
-- DBCC CHECKIDENT('publicacion', RESEED, 0);
-- DBCC CHECKIDENT('documento', RESEED, 0);
-- DBCC CHECKIDENT('plantilla', RESEED, 0);
-- DBCC CHECKIDENT('recurso_multimedia', RESEED, 0);
-- DBCC CHECKIDENT('tag', RESEED, 0);
-- DBCC CHECKIDENT('tema_ambiental', RESEED, 0);
-- DBCC CHECKIDENT('tipo_publicacion', RESEED, 0);
-- DBCC CHECKIDENT('redsocial', RESEED, 0);
-- DBCC CHECKIDENT('factura', RESEED, 0);
-- DBCC CHECKIDENT('generadoria', RESEED, 0);
-- DBCC CHECKIDENT('fecha_actividad', RESEED, 0);
-- DBCC CHECKIDENT('cliente', RESEED, 0);
-- DBCC CHECKIDENT('empresa', RESEED, 0);
-- DBCC CHECKIDENT('persona', RESEED, 0);
-- DBCC CHECKIDENT('usuario', RESEED, 0);
-- DBCC CHECKIDENT('rol', RESEED, 0);

-- Mensaje de confirmación
PRINT 'Limpieza de datos completada. La estructura de las tablas se mantiene.';
