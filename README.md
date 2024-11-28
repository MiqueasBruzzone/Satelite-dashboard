# Predicción de Precios de Viviendas

Este proyecto utiliza Machine Learning para predecir el precio de venta de viviendas basándose en características como área habitable, calidad de construcción y año de construcción.

## Tabla de Contenidos
1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Dataset](#dataset)
3. [Metodología](#metodología)
4. [Resultados](#resultados)
5. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)

## Descripción del Proyecto

El objetivo es desarrollar un modelo de regresión que estime con precisión el precio de una vivienda, ayudando a compradores y vendedores a tomar decisiones informadas.

## Dataset

- **Fuente**: [Kaggle: Ames Housing Dataset](https://www.kaggle.com/datasets/prevek18/ames-housing-dataset)
- **Tamaño**: 2,930 filas, 82 columnas.

## Metodología

1. **Limpieza de Datos**:
   - Eliminación de valores nulos.
   - Transformación de variables categóricas.

2. **Análisis Exploratorio (EDA)**:
   - Estadísticas descriptivas.
   - Visualización de correlaciones.

3. **Entrenamiento del Modelo**:
   - Algoritmo principal: `RandomForestRegressor`.
   - Métricas de evaluación: RMSE, R^2.

4. **Resultados**:
   - Gráficos que muestran predicciones versus valores reales.

## Resultados

- RMSE: 24,000
- R²: 0.89

![Gráfico de Predicción](notebooks/resultados_grafico.png)

## Cómo Ejecutar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/predict-house-prices.git
   cd predict-house-prices

