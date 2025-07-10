"""
Módulo centralizado para sanitización de datos de entrada.
Proporciona funciones para limpiar y validar datos antes de procesarlos.
"""
import re
import html
from typing import Any, Union, Optional


def sanitizar_entrada(value: Any) -> Any:
    """
    Sanitiza una entrada de datos para prevenir ataques XSS y limpiar caracteres no deseados.
    
    Args:
        value: El valor a sanitizar (puede ser str, int, float, etc.)
        
    Returns:
        El valor sanitizado
    """
    if isinstance(value, str):
        # Eliminar caracteres no imprimibles
        value = ''.join(c for c in value if c.isprintable())
        # Eliminar espacios en blanco al inicio y final
        value = value.strip()
        # Escapar caracteres HTML para prevenir XSS
        value = html.escape(value)
    return value


def sanitizar_entrada_avanzada(value: Any, max_length: Optional[int] = None, 
                              allow_html: bool = False, 
                              strip_special_chars: bool = False) -> Any:
    """
    Sanitización avanzada con opciones adicionales.
    
    Args:
        value: El valor a sanitizar
        max_length: Longitud máxima permitida
        allow_html: Si True, no escapa caracteres HTML
        strip_special_chars: Si True, elimina caracteres especiales
        
    Returns:
        El valor sanitizado
    """
    if not isinstance(value, str):
        return value
    
    # Eliminar caracteres no imprimibles
    value = ''.join(c for c in value if c.isprintable())
    
    # Eliminar espacios en blanco
    value = value.strip()
    
    # Eliminar caracteres especiales si se solicita
    if strip_special_chars:
        value = re.sub(r'[^\w\s\-\.\@áéíóúÁÉÍÓÚüÜñÑ]', '', value)
    
    # Truncar si excede la longitud máxima
    if max_length and len(value) > max_length:
        value = value[:max_length]
    
    # Escapar HTML si no se permite
    if not allow_html:
        value = html.escape(value)
    
    return value


def sanitizar_email(email: str) -> str:
    """
    Sanitiza específicamente direcciones de email.
    """
    if not isinstance(email, str):
        return ""
    
    email = email.strip().lower()
    # Eliminar caracteres no válidos en emails
    email = re.sub(r'[^\w\@\.\-\+]', '', email)
    return email


def sanitizar_telefono(telefono: str) -> str:
    """
    Sanitiza números de teléfono.
    """
    if not isinstance(telefono, str):
        return ""
    
    # Eliminar todo excepto números, espacios, guiones y paréntesis
    telefono = re.sub(r'[^\d\s\-\(\)\+]', '', telefono)
    return telefono.strip()


def sanitizar_numero(value: Any) -> Union[float, int, None]:
    """
    Sanitiza y convierte valores numéricos.
    """
    if value is None or value == "":
        return None
    
    try:
        # Si es string, limpiar caracteres no numéricos (excepto punto y coma)
        if isinstance(value, str):
            value = re.sub(r'[^\d\.\,\-\+]', '', value.strip())
            # Reemplazar coma por punto para decimales
            value = value.replace(',', '.')
        
        # Intentar convertir a número
        if '.' in str(value):
            return float(value)
        else:
            return int(value)
    except (ValueError, TypeError):
        return None


def validar_longitud_campo(valor: str, min_length: int = 0, max_length: int = 255) -> tuple[bool, str]:
    """
    Valida la longitud de un campo.
    """
    if not isinstance(valor, str):
        return False, "El valor debe ser una cadena de texto"
    
    if len(valor) < min_length:
        return False, f"El campo debe tener al menos {min_length} caracteres"
    
    if len(valor) > max_length:
        return False, f"El campo no puede exceder {max_length} caracteres"
    
    return True, ""


def sanitizar_dict(data: dict, campos_a_sanitizar: list = None) -> dict:
    """
    Sanitiza todos los valores string de un diccionario.
    
    Args:
        data: Diccionario con los datos
        campos_a_sanitizar: Lista de campos específicos a sanitizar. Si es None, sanitiza todos.
        
    Returns:
        Diccionario con valores sanitizados
    """
    if not isinstance(data, dict):
        return data
    
    data_sanitizada = data.copy()
    
    for key, value in data_sanitizada.items():
        # Si se especifican campos, solo sanitizar esos
        if campos_a_sanitizar is not None and key not in campos_a_sanitizar:
            continue
            
        data_sanitizada[key] = sanitizar_entrada(value)
    
    return data_sanitizada
