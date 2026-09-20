# Resumen

> Datos exportados el 20 de septiembre de 2026. Estos datos están sujetos a cambios si se generan nuevos exports de Letterboxd en el futuro.

## Principales resultados

* Se analizaron 502 películas calificadas.
* La calificación promedio fue de 3.38.
* La calificación más utilizada fue 4.0.
* Se registraron 542 visualizaciones en el diario.
* El año con más visualizaciones registradas fue 2025, con 184.
* La mayor concentración de valoraciones se encuentra entre 3.5 y 4.0.
* 24 películas recibieron la calificación máxima de 5.0.

## Interpretación

Los resultados muestran que las calificaciones se concentran principalmente entre 3.5 y 4.0. La calificación promedio fue de 3.38 y la más frecuente fue 4.0, lo que permite observar cómo se distribuyen las valoraciones realizadas por el usuario.

En cuanto a las visualizaciones registradas en el diario, 2025 fue el año con mayor cantidad de registros, con 184 visualizaciones. Los registros muestran 107 visualizaciones en 2023, 162 en 2024, 184 en 2025 y 89 en 2026. La cifra de 2026 debe interpretarse con precaución porque corresponde a un periodo que todavía no está completo.

La comparación entre las calificaciones y las visualizaciones permite analizar dos aspectos diferentes del comportamiento registrado en Letterboxd: la cantidad de visualizaciones registradas y la forma en que fueron calificadas las películas.

## Limitaciones

* El análisis está centrado en los datos exportados de Letterboxd y no incluye información externa como género, director, duración o contexto de cada película.
* `diary.csv` representa registros de visualizaciones y puede incluir varias filas para un mismo título si una película fue vista más de una vez. Por lo tanto, no representa necesariamente la cantidad de películas únicas vistas.
* En `diary.csv`, 542 registros existen en total, pero solo 535 tienen `Rating` no nulo. Eso significa que no todas las visualizaciones cuentan con una calificación asociada, algo que debe considerarse al comparar visualizaciones y valoraciones.
* El análisis es descriptivo y no inferencial: no se buscan correlaciones más complejas ni modelos predictivos.
* Las columnas de texto libre de algunos CSV pueden requerir limpieza adicional si se quiere realizar un análisis semántico de las reseñas o comentarios.
* Aún no se ha explotado semánticamente el contenido de `reviews.csv`, que incluye reseñas de texto libre y puede aportar información cualitativa adicional sobre gustos, opiniones y patrones de consumo.

## Conclusión

El análisis permitió identificar patrones en el historial cinematográfico registrado en Letterboxd. Se analizaron 502 películas calificadas y 542 registros de visualizaciones, encontrando una calificación promedio de 3.38 y una mayor frecuencia de valoraciones de 4.0.

Las visualizaciones registradas alcanzaron su mayor cantidad en 2025, con 184 registros. Además, la distribución de ratings y las visualizaciones por año permiten observar diferentes dimensiones del comportamiento cinematográfico registrado por el usuario.

Este proyecto demuestra cómo un conjunto de archivos CSV puede transformarse en información útil mediante un proceso de exploración, preparación, análisis, creación de métricas y visualización de datos.
