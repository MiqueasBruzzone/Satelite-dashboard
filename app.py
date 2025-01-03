import streamlit as st
import pandas as pd

# Título del Dashboard
st.title("Dashboard de Satélites (Datos Reales)")



# Mostrar una imagen inicial
st.image("images/Satelites-2.jpg", caption="Satélite en órbita", use_container_width=True)
 

 
# Cargar datos
data_path = "data/satellites_cleaned.csv"

try:
    # Cargar el archivo CSV
    df = pd.read_csv(data_path)

    # Mostrar los datos cargados
    st.subheader("Datos Generales de Satélites")
    st.dataframe(df.head())

    # Selección de filtros
    st.subheader("Filtrar Datos por País de Operación")
    countries = st.multiselect("Seleccionar Países", options=df["Country of Operator/Owner"].unique())
    if countries:
        filtered_data = df[df["Country of Operator/Owner"].isin(countries)]
        st.write(f"Datos filtrados por País: {countries}")
        st.dataframe(filtered_data)
    else:
        st.write("Selecciona al menos un país para filtrar los datos.")

    # Gráfico: Distribución por Tipo de Órbita
    st.subheader("Distribución de Satélites por Tipo de Órbita")
    orbit_counts = df["Class of Orbit"].value_counts()
    st.bar_chart(orbit_counts)

except FileNotFoundError:
    st.error(f"No se encontró el archivo de datos en {data_path}. Asegúrate de que exista.")
except KeyError:
    st.error("El dataset no contiene las columnas esperadas.")




