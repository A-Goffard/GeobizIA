import pandas as pd

def preparar_estadisticas_actividades(lista_actividades):
    if not lista_actividades:
        return {"total": 0, "por_tipo": {}, "por_responsable": {}}
    df = pd.DataFrame(lista_actividades)
    return {
        "total": len(df),
        "por_tipo": df["tipo"].value_counts().to_dict() if "tipo" in df else {},
        "por_responsable": df["responsable"].value_counts().to_dict() if "responsable" in df else {}
    }


