import streamlit as st
import pandas as pd

st.title("Dashboard ChatBot Medico")

df = pd.read_csv("logs_chatbot.csv")

st.metric(
    "Consultas",
    len(df)
)

st.metric(
    "Latencia promedio",
    round(df["latencia"].mean(),2)
)

st.metric(
    "Errores",
    int(df["latencia"].mean(), 2)
)

st.metric(
    "CPU promedio",
    int(df["CPU"].mean(), 2)
)

st.metric(
    "RAM promedio",
    int(df["ram"].mean(), 2)
)

st.subheader("CPU")

st.bar_chart(
    df["cpu"]
)

st.subheader("RAM")

st.bar_chart(
    df["ram"]
)

st.subheader("Últimos registros")

st.dataframe(
    df.tail(20)
)