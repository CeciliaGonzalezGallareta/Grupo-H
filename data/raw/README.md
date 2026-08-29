Análisis de Datos de Películas

Actividades Requeridas del Proyecto

El proyecto se divide en dos fases principales:

  Primera fase: realizada en notebooks/practice.ipynb, donde se lleva a cabo la carga, limpieza y análisis exploratorio 
del dataset.
  Segunda fase: realizada en app.py, donde se desarrolla una aplicación interactiva utilizando Streamlit.

El proyecto utiliza un dataset de películas con información relacionada con sus características y calificaciones.

La pregunta guía que orienta el análisis es:
¿Es posible predecir el éxito de una película a estrenar, medido a través de su rating, de acuerdo con su género y otras 
características disponibles en el dataset?

Primera Fase
En el archivo notebooks/practice.ipynb se realiza el proceso de preparación y análisis de los datos.

Dataset
Se seleccionó un dataset relacionado con películas, que fue incorporado al directorio: data/raw/
Esta carpeta conserva los datos originales sin modificaciones.

Carga y Estructura
Se carga el dataset desde data/raw utilizando Pandas y se convierte en un DataFrame para facilitar su procesamiento 
y análisis.

Durante esta etapa se revisan:
    cantidad de registros;
    cantidad de columnas;
    tipos de datos;
    valores faltantes;
    valores duplicados;
    estructura general del dataset.

Análisis Exploratorio de Datos (EDA)
Se realiza un Análisis Exploratorio de Datos (EDA) utilizando Pandas y diferentes herramientas de visualización.
Como parte de la limpieza se realizan transformaciones sobre los datos para obtener un DataFrame preparado para el 
análisis.
Entre los análisis realizados se encuentra el estudio de la relación entre diferentes características de las películas y
su rating.
Uno de los análisis principales fue estudiar la relación entre la duración de las películas y su calificación.
También se analizó el rating promedio según el género, buscando identificar si determinados géneros presentan mejores 
calificaciones promedio.

Resultado del análisis de correlación
Para estudiar la relación entre la duración y el rating se utilizó el coeficiente de correlación de Pearson.
Como criterio de referencia: Si el coeficiente de correlación es mayor a 0.4, se considera que existe una correlación
positiva moderada o fuerte, indicando que las películas más largas tienden a presentar mejores puntuaciones. Sin 
embargo, n nuestro análisis se obtuvo:
Coeficiente de correlación de Pearson: 0.16
Este resultado indica que existe una correlación positiva muy débil o casi inexistente entre la duración de una película
y su rating.
Por lo tanto, concluimos que:
La duración de la película no parece influir significativamente en su calificación.
Este resultado permite descartar la duración como un factor relevante para explicar por sí sola el éxito de una película,
y refuerza la necesidad de analizar otras características, como el género y otros atributos disponibles en el dataset.
Grabación

Una vez finalizada la limpieza y preparación, el DataFrame resultante se guarda como un nuevo archivo CSV dentro de:
data/processed/   siendo este:  data/processed/final_dataset_limpio.csv
De esta manera se mantiene separado el dataset original (raw) del dataset procesado.
 
Segunda Fase — Aplicación Interactiva con Streamlit
En el archivo app.py se desarrolla una aplicación interactiva utilizando Streamlit, a partir del dataset procesado en la
primera fase.
El objetivo es explorar los datos de películas y analizar la posibilidad de predecir su éxito, utilizando el rating como
indicador, considerando características como el género y la duración.

Análisis Descriptivo Interactivo
La aplicación cuenta con una barra lateral y diferentes controles que permiten al usuario seleccionar los valores sobre
los cuales realizar el análisis.
Se incorporan filtros y estadísticas descriptivas para analizar los datos seleccionados, incluyendo:
  Media.
  Mediana.
  Desviación estándar.
  Cuartiles.
  Rango.

Correlación entre variables.
También se incluye un gráfico de dispersión para analizar la relación entre duración de la película y rating, 
acompañado de una línea de tendencia.
En el análisis realizado se obtuvo una correlación de 0.96 entre duración y rating, indicando una relación positiva 
fuerte entre ambas variables dentro del dataset utilizado.

Análisis Predictivo
La aplicación incorpora un análisis predictivo orientado a estimar la probabilidad de que una película alcance un 
rating igual o superior a 7.0, considerado como referencia para determinar un posible éxito.

El usuario puede definir mediante un st.slider un umbral de probabilidad entre 10% y 90%.

El modelo calcula la probabilidad de obtener: Rating ≥ X, y la compara con el umbral seleccionado por el usuario.
Por ejemplo, si se establece un umbral del 50%, la aplicación determina si la probabilidad calculada alcanza dicho valor
y muestra si se cumple o no el umbral de probabilidad.
Este análisis permite utilizar los patrones encontrados en los datos históricos para realizar una estimación sobre 
el posible éxito de una película.

Visualización Dinámica
Los gráficos y resultados se actualizan automáticamente al modificar los filtros y parámetros seleccionados por el 
usuario. De esta forma, Streamlit permite combinar el análisis descriptivo y predictivo en una única aplicación 
interactiva.
 
Pregunta y Conclusión del Proyecto
El análisis parte de la siguiente pregunta guía:
¿Podemos anticipar el éxito de una película a estrenar, medido mediante su rating, a partir de su género y otras 
características disponibles?
El análisis exploratorio permite observar que no todas las características de una película tienen la misma capacidad 
para explicar su rating.
En particular, el análisis de la duración obtuvo un coeficiente de Pearson de 0.16, por lo que la relación entre 
duración y rating es muy débil.
Por este motivo, no podemos considerar que una película más larga vaya a obtener necesariamente una mejor calificación.
El análisis del género permite avanzar en la búsqueda de características que puedan estar relacionadas con mejores 
ratings promedio y, de esta manera, aportar información para evaluar qué características podrían estar asociadas al 
éxito de una película.
Es importante aclarar que estos resultados permiten identificar relaciones y patrones en los datos, pero no garantizan
que sea posible predecir con certeza el rating de una película futura.
 