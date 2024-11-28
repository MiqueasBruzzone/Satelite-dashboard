# Satelites
Proyecto de análisis y predicción de satélites en órbita con dashboard interactivo
# Satelite Dashboard 🚀

Este es un proyecto de análisis y predicción de satélites lanzados al espacio, utilizando datos simulados y técnicas de Machine Learning. Además, incluye un **dashboard interactivo** para explorar los datos de manera visual y dinámica.

## Descripción del Proyecto

Este proyecto tiene dos objetivos principales:
1. Analizar datos históricos de satélites (masa, tipo de órbita, país de lanzamiento, etc.).
2. Utilizar un modelo de Machine Learning para predecir el tipo de misión de un satélite basado en sus características.

El proyecto también incluye un dashboard interactivo desarrollado con **Streamlit**, que permite:
- Filtrar los datos por país, tipo de órbita y estado (activo/inactivo).
- Visualizar gráficos como histogramas y líneas de tiempo.
- Descargar y explorar los datos directamente.

- ## Requisitos
Asegúrate de tener instalados:
- Python 3.8 o superior
- Streamlit
- Pandas
- Matplotlib

---

## Contenido del Repositorio

Satelite-dashboard/
├── data/
│   ├── satellites_cleaned.csv      # Datos del proyecto
├── notebooks/
│   ├── 01-eda.ipynb                # Análisis exploratorio
│   ├── 02-predict-model.ipynb      # Desarrollo del modelo predictivo
├── src/
│   ├── app.py                      # Código del dashboard
│   ├── train_model.py              # Código para entrenar el modelo
├── README.md                       # Descripción del proyecto
├── requirements.txt                # Lista de dependencias necesarias
├── .gitignore                      # Archivos y carpetas a ignorar por Git

---



