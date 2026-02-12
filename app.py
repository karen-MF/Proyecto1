import pandas as pd 
import plotly.express as px
import streamlit as st

st.header("Análisis Exploratorio de Anuncios de Venta de Coches 🚗")

car_data = pd.read_csv("vehicles_us.csv")
st.write("Vista previa del conjunto de datos:") 
st.dataframe(car_data.head())

hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Creación de un histograma para conjunto de datos de anuncios de venta de coches")
    fig=px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Relación entre precio y odómetro")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title = "Relación entre precio y odómetro"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    