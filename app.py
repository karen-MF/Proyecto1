import pandas as pd 
import plotly.express as px
import streamlit as st

st.header("Análisis Exploratorio de Anuncios de Venta de Coches 🚗")

car_data = pd.read_csv("vehicles_us.csv")
st.write("Vista previa del conjunto de datos:") 
st.dataframe(car_data.head())

hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Conjunto de datos de anuncios vs odómetro")
    fig=px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title = "Relación entre precio y odómetro"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

model_price_button = st.button("Histograma de precios por modelo")
if model_price_button:
    fig_model_price = px.histogram(
        car_data,
        x="model",
        y="price",
        title="Distribucion de precios por modelo",
        histfunc="avg"
    )
    st.plotly_chart(fig_model_price, use_container_width=True)
    