import time
import psutil
import pandas as pd
from datetime import datetime

LOG_FILE ="logs_chatbot.csv"

def obtener_metricas():
    return {
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent
    }

def registrar_log(
        pregunta,
        respuesta,
        latencia,
        cpu,
        ram,
        error=False
):
    fila = {
        "fecha": datetime.now(),
        "pregunta": pregunta,
        "respuesta":respuesta,
        "latencia":latencia,
        "cpu":cpu,
        "ram":ram,
        "error":error
    }

    df = pd.DataFrame([fila])

    try:
        df.to_csv(
            LOG_FILE,
            mode="a",
            index=False,
            header=False
        )

    except:
        df.to_csv(
            LOG_FILE,
            index=False
        )