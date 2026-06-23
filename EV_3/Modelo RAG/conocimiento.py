Base_conocimientos={
    "ayuno": 
    """Se recomienda ayuno de 6 a 8 horas antes de una cirugía.""",

    "medicamentos": 
    """Debe consultar con su médico antes de suspender cualquier medicamento.""",

    "alergias": 
    """Es importante informar al equipo médico sobre cualquier alergia.""",

    "higiene": 
    """Se recomienda bañarse antes del procedimiento según indicaciones médicas.""",

    "alcohol": 
    """Evitar consumo de alcohol al menos 24 horas antes de la cirugía.""",

    "tiempo": 
    """Se recomienda llegar con aticipasion al centro medico"""
}

#Busqueda del contexto

def buscar_contexto(pregunta):
    contexto = []
    pregunta = pregunta.lower()

    for clave, valor in Base_conocimientos.items():
        if clave in pregunta:
            contexto.append(valor)

        if not contexto:
            contexto.append("""Siga siempre las indicaciones generales de su equipo medico""")
        return contexto