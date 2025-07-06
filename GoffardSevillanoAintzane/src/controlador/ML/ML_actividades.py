import pandas as pd

def preparar_estadisticas_actividades(lista_actividades):
    if not lista_actividades:
        return {
            "total": 0,
            "por_tipo": {},
            "por_responsable": {},
            "por_mes": {},
            "coste_medio_tipo": {},
            "facturacion_por_responsable": {}
        }
    df = pd.DataFrame(lista_actividades)

    # Por tipo
    por_tipo = df["tipo"].value_counts().to_dict() if "tipo" in df else {}

    # Por responsable
    por_responsable = df["responsable"].value_counts().to_dict() if "responsable" in df else {}

    # Evolución mensual (requiere columna 'fecha_creacion' o similar)
    if "fecha_creacion" in df:
        try:
            df["mes"] = pd.to_datetime(df["fecha_creacion"], errors="coerce").dt.to_period("M").astype(str)
            por_mes = df["mes"].value_counts().sort_index().to_dict()
        except Exception:
            por_mes = {}
    else:
        por_mes = {}

    # Coste medio por tipo
    if "tipo" in df and "coste_economico" in df:
        try:
            df["coste_economico"] = pd.to_numeric(df["coste_economico"], errors="coerce")
            coste_medio_tipo = df.groupby("tipo")["coste_economico"].mean().round(2).dropna().to_dict()
        except Exception:
            coste_medio_tipo = {}
    else:
        coste_medio_tipo = {}

    # Facturación total por responsable
    if "responsable" in df and "facturacion" in df:
        try:
            df["facturacion"] = pd.to_numeric(df["facturacion"], errors="coerce")
            facturacion_por_responsable = df.groupby("responsable")["facturacion"].sum().round(2).dropna().to_dict()
        except Exception:
            facturacion_por_responsable = {}
    else:
        facturacion_por_responsable = {}

    return {
        "total": len(df),
        "por_tipo": por_tipo,
        "por_responsable": por_responsable,
        "por_mes": por_mes,
        "coste_medio_tipo": coste_medio_tipo,
        "facturacion_por_responsable": facturacion_por_responsable
    }
