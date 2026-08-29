import streamlit as st
import pandas as pd

st.title("Explorador de películas")
st.write("Predecir exito de la película")
df = pd.DataFrame({"rating": [1, 2, 3, 4, 5],
                   "duration_minutes" : [60, 70, 80, 90, 120]})
st.dataframe(df)

tipo_analisis = st.sidebar.radio('Evaluar si duración se relaciona con rating',
['Descriptivo', 'Predictivo'])
st.header(f'Resultado de la relación: {tipo_analisis}')
if tipo_analisis == 'Descriptivo':
    correlacion = df["duration_minutes"].corr(df["rating"])
    st.write(f"Correlación entre duración y rating: {correlacion:.2f}")

else:
    st.write("Análisis predictivo")

umbral = st.slider(
    "Define el Umbral de Probabilidad",
    min_value=0.1,
    max_value=0.9,
    value=0.5,
    step=0.05
)

st.write(f"El modelo filtrará con un umbral de: {umbral:.20%}")

rango_duracion = st.sidebar.slider(
    "Seleccionar duración",
    min_value=int(df["duration_minutes"].min()),
    max_value=int(df["duration_minutes"].max()),
    value=(90, 120)
)

rating_minimo = st.sidebar.slider(
    "Rating mínimo",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

# Filtrar por duración
df_filtrado = df[
    (df["duration_minutes"] >= rango_duracion[0]) &
    (df["duration_minutes"] <= rango_duracion[1])
]

# Calcular probabilidad de alcanzar el rating elegido
probabilidad = (
    (df_filtrado["rating"] >= rating_minimo).mean()
)

st.write(f"Probabilidad de obtener un rating ≥ {rating_minimo}: {probabilidad:.2%}")

# Comparar con el umbral
if probabilidad >= umbral:
    st.success("Se cumple el umbral de probabilidad")
else:
    st.warning("No se cumple el umbral de probabilidad")

estadisticas = df_filtrado.describe()

st.write("Estadísticas de los datos filtrados")
st.write(estadisticas)

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
datos_hist = np.random.normal(1, 1, 10)
ax.hist(datos_hist, bins=30, color='skyblue', edgecolor='black')
ax.set_title('Distribución de Muestra')
st.pyplot(fig)

st.subheader("Relación entre Duración y Rating")

fig, ax = plt.subplots()

ax.scatter(
    df_filtrado["duration_minutes"],
    df_filtrado["rating"]
)

ax.set_xlabel("Duración (minutos)")
ax.set_ylabel("Rating")
ax.set_title("Relación entre Duración y Rating")

st.pyplot(fig)
