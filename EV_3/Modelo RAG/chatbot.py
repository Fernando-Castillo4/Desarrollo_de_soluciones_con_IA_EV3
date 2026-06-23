from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

import os
import time

from dotenv import load_dotenv

load_dotenv()

from conocimiento import buscar_contexto
from planificador import planificar_tarea

from conocimiento import buscar_contexto
from planificador import planificar_tarea

from tools_medicas import(
    buscar_recomendacion,
    generar_reporte,
    evaluar_riesgo,
    registro_recordatorio
)

from observabilidad import(
    registrar_log,
    obtener_metricas
)

historial_chat=[]

llm= ChatOpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("GITHUB_TOKEN"),
    model="gpt-4.1",
    temperature=0,
    streaming=True
)

agent = create_agent(
    model=llm,
    tools = [
        buscar_recomendacion,
        generar_reporte,
        evaluar_riesgo,
        registro_recordatorio
    ],
    system_prompt="""
        Eres un asistente de una clinica el cual esta especilizado en recomendaciones preoperatorias. 
        Tienes que seguir el siguiente reglamento:
            -Solo dar recomendaciones generales.
            -NO puedes recomendar medicamentos ni dosis.
            -NO realizar diagnosticos.
            -Si te piden realizar un diagnostico debes rechazarlo y explicar el pq no debes.
        
        Tu funcion principal es orientar a los pacientes antes de una cirugia utilizando las herramientas
        disponibles cuando sean necesarias y Nunca inventes información médica.
    """
)

datos_sensibles = [
    "rut",
    "contraseña",
    "clave",
    "tarjeta"
]

def ChatBot_Medico3():
    print("==ChatBot preoperatorio==")
    print("Escribe 'salir' para terminar la conversación\\n")

    while True:

        print("--------- ChatBot preoperatorio Titirilquen ---------")

        while True:

            pregunta = input("\nUsuario:")

            if pregunta.lower()=="salir":
                print("Gracias por utilizar: ChatBot clinica titirilquen")
                break

            if any(
                palabra in pregunta.lower()
                for palabra in datos_sensibles
            ):
                print("\n No puedo procesar informacion sensible")
                continue

            documentos = buscar_contexto(pregunta)

            contexto = "\n".join(documentos)

            plan = planificar_tarea(pregunta)

            plan_texto = "\n".join(plan)

            mensaje_usuario = f"""
            Plan de acción:

            {plan_texto}

            Contexto recuperado: {contexto}

            Consulta del paciente: {pregunta}
            """

            historial_chat.append(
                {
                    "role": "user",
                    "content": mensaje_usuario
                }
            )

            try:

                inicio = time.time()

                resultado = agent.invoke(
                    {
                        "messages":historial_chat
                    }
                )

                respuesta = resultado["messages"][-1].content

                fin = time.time()

                latencia = (
                    fin - inicio
                )

                metricas = (
                    obtener_metricas()
                )

                registrar_log(
                    pregunta,
                    respuesta,
                    latencia,
                    metricas["cpu"],
                    metricas["ram"]
                )

                print("\nAsistente: ")
                print(respuesta)

                historial_chat.append(
                {
                    "role": "assistant",
                    "content": respuesta
                }
            )

            except Exception as e:

                registrar_log(
                    str(e),
                    0,
                    0,
                    0,
                    True
                )

                print(f"\nError: {e}")

ChatBot_Medico3()  