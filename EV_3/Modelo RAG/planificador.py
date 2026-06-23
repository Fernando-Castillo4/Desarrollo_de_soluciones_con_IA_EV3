def planificar_tarea(consulta):
    consulta = consulta.lower()

    if "reporte" in consulta:
        return [
            "Buscar informacion",
            "Generar reporte",
            "Entregar resultado"
        ]

    elif "riesgo" in consulta:
        return [
            "Analizar antecedentes",
            "Evaluar riesgo",
            "Entregar evaluacion"
        ]

    elif "recordatorio" in consulta:
        return [
            "Registrar recordatorio",
            "Generar respuesta"
        ]
    return [
        "Buscar recomendaciones",
        "Generar respuesta"
    ]