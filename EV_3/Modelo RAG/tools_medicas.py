from langchain.tools import tool
from conocimiento import buscar_contexto

@tool
def buscar_recomendacion(pregunta:str) -> str:
    """
    Busca recomendaciones medicas preoperatorias
    """

    docs = buscar_contexto(pregunta)

    return "\n".join(docs)

@tool
def generar_reporte(texto:str)-> str:
    """
    Genera un reporte resmido
    """

    return f"""
    REPORTE PREOPERATORIO
    {texto}
    """

@tool
def evaluar_riesgo(texto:str)-> str:
    """
    Evaluá riesgos simples.
    """

    texto = texto.lower()

    if "alcohol" in texto:
        return "Posible incumplimiento de indicaciones preoperatorias"
    
    if "alergia" in texto:
        return "Se detectan anteedentes de alergias"
    
    return "No se identifican riesgos relevantes."

@tool
def registro_recordatorio(texto:str):
    """
    Registra recordatorios para el paciente
    """

    return f"recordatorio registrado {texto}"