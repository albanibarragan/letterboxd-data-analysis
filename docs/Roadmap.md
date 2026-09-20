## Objetivo

Mini proyecto para analizar mis datos de Letterboxd para conocer mejor mis hábitos y gustos cinematográficos además estará enfocado en aprender los conceptos básicos de análisis de datos.

El objetivo será analizar mis hábitos cinematográficos y obtener algunas conclusiones sobre las películas que veo y cómo las califico.
## 🛠️ Herramientas

- Python
- pandas
- matplotlib

## Fase 1 — Entender el contexto del analisis

## Problema

Tengo un historial de películas en Letterboxd, pero los datos por sí solos no me permiten conocer fácilmente mis hábitos cinematográficos.

## Objetivo del análisis

Convertir esos datos en información que me permita responder preguntas sencillas sobre mi actividad y mis calificaciones.

## Preguntas principales

- ¿Cuántas películas he calificado?
- ¿Cuál es mi calificación promedio?
- ¿Qué calificación utilizo más?
- ¿Cuántas películas califico por año?
- ¿Cuáles son mis 10 películas mejor calificadas?

## Usuario del análisis

¿Quién va a ser el interesado de la visualizacion y analisis de estos datos?

## Resultado esperado

Un pequeño análisis exploratorio con algunas visualizaciones y conclusiones.

## Fase 2 — Delimitar el alcance

## Incluido

- Datos personales exportados desde Letterboxd.
- Analisis de los datos que puedo exportar de letterboxd sin API
- Análisis de películas calificadas.
- Exploración y limpieza básica.
- Métricas: total, promedio, mediana, moda, por año, top calificadas.
- 3 visualizaciones.
- Conclusiones.
## Fuera de alcance

- API de Letterboxd.
- SQL, DuckDB, Power BI.
- Machine Learning / recomendaciones.
- Análisis avanzado de reseñas.
- Datos externos sobre películas (género, director, TMDB).

## Fase 3 — Inventariar las fuentes
- ¿Cuál es la fuente principal?
### Revisión de la fuente

- **Período cubierto** 
- **Valores faltantes
- **Duplicados**
- **Rango de calificaciones**
- **Limitación conocida**
- **Limitación de cobertura**

## Fase 4 — Diseñar el flujo de datos (Opcional si se quiere)

Diseñar en mermaid un diagrama de flujo de datos.

Importante: Conocer como se compone un diagrama de flujo de datos.

### Fase 5 — Analizar la estructura de los datos

- **Columnas:** `Date` (texto), `Name` (texto), `Year` (entero), `Letterboxd URI` (texto), `Rating` (decimal).
- **Tipos originales:** `Date` llega como texto (`str`), no como fecha — requiere conversión.
- **Valores únicos en `Rating`:** 10 valores posibles (0.5 a 5.0 en pasos de 0.5).
- **Duplicados:** 0.
- **Rango de fechas:** válido, sin fechas futuras erróneas ni nulas.

### ¿Qué representa cada fila?

> Cada fila representa **una película calificada por mí una única vez**, identificada por su nombre, año de estreno y la fecha en la que registré la calificación.

## Fase 6 — Preparar los datos

Aprender a:

- Seleccionar columnas.
- Filtrar filas.
- Ordenar datos.
- Contar valores.
- Revisar valores faltantes.

## Transformaciones aplicadas

- Convertir `Date` de texto a fecha real con `pd.to_datetime()`.
- Crear una columna derivada `Year_rated` (`Date.dt.year`) para poder agrupar por año de calificación — distinto del `Year` de estreno de la película.
- No se necesitó imputar nulos (no existen).
- No se necesitó eliminar duplicados (no existen).

Cada transformación es reproducible: ejecutar el notebook de nuevo sobre el mismo CSV da el mismo resultado.

##  Fase 7 —  Validar la calidad

|Validación|Resultado|
|---|---|
|¿Hay películas duplicadas?
|¿Hay calificaciones faltantes?
|¿Las calificaciones están en rango (0.5–5.0)?
|¿Las fechas son válidas?
|¿La cantidad de registros tiene sentido?
|¿Coincide con una revisión manual?

##  Fase 8 —  Analizar datos

Responder estas preguntas:

1. ¿Cuántas películas he calificado?
2. ¿Cuál es mi rating promedio?
3. ¿Qué rating utilizo más?
4. ¿Cuántas películas he visto por año?
5. ¿Cuáles son mis películas mejor calificadas?
6. ¿Datos sensibles que me dan en los csv?

## Fase 9 — Crear las métricas

| Métrica                                 | Valor |
| --------------------------------------- | ----- |
| Total de películas calificadas          |       |
| Calificación promedio                   |       |
| Calificación mediana                    |       |
| Calificación más frecuente (moda)       |       |
| Películas calificadas por año           |       |
| Películas con calificación máxima (5.0) |       |


## Fase 10 — Crear las visualizaciones

Crear solamente 3 gráficos:

-  1. Películas por año: Mostrar cuántas películas he visto/calificado cada año.
-  2. Distribución de ratings: Mostrar cuántas películas tienen cada rating.
- 3. Top películas: Mostrar mis películas con mayor calificación.

## Fase 11 — Comunicar los resultados

Escribir algunas conclusiones sobre los datos.

Por ejemplo:

- ¿En qué años vi más películas?
- ¿Cuál es mi rating más habitual?
- ¿Suelo puntuar alto o bajo?
- ¿Qué películas considero mis favoritas?

