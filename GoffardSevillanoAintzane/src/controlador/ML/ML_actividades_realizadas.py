import pandas as pd

def preparar_estadisticas_actividades(lista_actividades, id_to_nombre):
    if not lista_actividades:
        return {"por_actividad": []}

    df = pd.DataFrame(lista_actividades)

    # Validaciones mínimas
    if "id_actividad" not in df or "id_actividad_realizada" not in df:
        return {"por_actividad": []}

    # Reemplazar IDs por nombres
    df["nombre"] = df["id_actividad"].map(id_to_nombre).fillna("Actividad desconocida")

    # Agrupación por nombre
    agrupado = df.groupby("nombre").agg(
        veces_realizada=("id_actividad_realizada", "count"),
        facturacion_total=("facturacion", "sum"),
        coste_total=("coste_economico", "sum"),
        asistencia_total=("asistentes", "sum"),
        fechas=("fecha", lambda x: sorted(set(x.dropna()))),
        observaciones=("observaciones", lambda x: [str(o).strip() for o in x.dropna() if str(o).strip()])
    ).reset_index()

    # Cálculo de beneficio
    agrupado["beneficio_total"] = agrupado["facturacion_total"] - agrupado["coste_total"]

    # Redondeo
    for col in ["facturacion_total", "coste_total", "beneficio_total"]:
        agrupado[col] = agrupado[col].round(2)

    return {"por_actividad": agrupado.to_dict(orient="records")}
