# Nivel 2 — análisis avanzado

## Objetivo

Subir el nivel del proyecto para ir más allá del análisis descriptivo básico y responder preguntas más complejas sobre patrones de consumo, valoración y comportamiento cinematográfico.

## Preguntas interesantes para analizar

### 1. ¿Cuál es la distribución real de mis calificaciones?
- ¿Estoy concentrado en puntuaciones altas, medias o bajas?
- ¿Existe un pico claro en 4.0 o 3.5?
- ¿Mi escala es más bien conservadora o más bien generosa?

### 2. ¿He visto más películas que las que he calificado?
- ¿Qué proporción de visualizaciones quedan sin puntuación?
- ¿Existe un patrón temporal donde ve películas y luego las califica más tarde?
- ¿Cuándo hago más valoraciones respecto a cuándo veo películas?

### 3. ¿Qué años tienen un comportamiento más intenso?
- ¿2025 fue el año con más registros, o solo con más datos disponibles?
- ¿La diferencia entre años refleja actividad real o simplemente un periodo más completo?
- ¿Hay un patrón de acumulación por temporada o por meses?

### 4. ¿Hay películas que vuelvo a ver?
- ¿Cuántos títulos aparecen más de una vez en el diario?
- ¿Qué películas tienen más rewatch?
- ¿Los rewatch tienen una calificación distinta a las primeras visualizaciones?

### 5. ¿Qué tipo de películas me gusta más?
- ¿Hay una tendencia hacia comedias, dramas, animación o películas de terror?
- ¿Mis mejores puntuaciones coinciden con ciertos tipos de contenido?
- ¿Elijo más títulos de cierto estilo según el momento del año?

### 6. ¿Qué patrones hay en la temporalidad?
- ¿Veo más durante ciertos meses?
- ¿Hay meses con más actividad de cine y meses con menos?
- ¿Califico más en determinadas épocas del año?

### 7. ¿Hay diferencias entre lo que veo y lo que califico?
- ¿Las mejores películas también son las que más veo?
- ¿Hay películas con muchas visualizaciones pero pocas valoraciones?
- ¿Las películas con reseñas o tags reciben un trato distinto?

### 8. ¿Qué películas considero mis favoritas de forma consistente?
- ¿Hay títulos que aparecen repetidamente en el top por año?
- ¿Qué películas tienen mejor mediana de puntuación?
- ¿Algunas películas se repiten en diferentes periodos con calificaciones estables?

### 9. ¿Existe una relación entre el año de la película y mi valoración?
- ¿Califico mejor películas antiguas o más recientes?
- ¿Hay una preferencia clara por títulos de cierta época?
- ¿Veo más cine clásico, contemporáneo o reciente?

### 10. ¿Qué pasa con los datos de reseñas y tags?
- ¿Qué palabras aparecen con más frecuencia en mis reseñas?
- ¿Hay frases o temas recurrentes en lo que escribo?
- ¿Las películas con más tags o comentarios suelen tener mejor nota?

## Tipos de análisis posibles

### A. Análisis temporal
- Conteo por mes y por año.
- Tendencias de visualización.
- Comparación de actividad entre 2023, 2024, 2025 y 2026.

### B. Análisis de puntuaciones
- Distribución completa de ratings.
- Moda, mediana y rango.
- Comparación entre años de calificación.

### C. Análisis de repetición
- Rewatch por título.
- Frecuencia de visualización por película.
- Diferencias entre primera vista y rewatch.

### D. Análisis de contenido
- Identificar patrones en tags.
- Extraer palabras clave de reseñas.
- Detectar temas recurrentes en mis valoraciones.

### E. Análisis comparativo
- Películas vistas vs. películas calificadas.
- Películas más vistas vs. mejor valoradas.
- Perfil de evaluación según año o temporada.

## Preguntas a priorizar

Si se quiere avanzar con un enfoque práctico, las preguntas más útiles serían:

1. ¿Cuántas películas veo pero no califico?
2. ¿Qué año tiene más actividad real de cine?
3. ¿Qué películas aparecen más de una vez en el diario?
4. ¿Hay una diferencia clara entre mis visualizaciones y mis puntuaciones?
5. ¿Qué tipos de películas reciben mejor nota?

## Siguiente paso recomendado

Antes de entrar en análisis más avanzados, conviene:

- limpiar y validar `diary.csv`,
- identificar la diferencia entre `Date`, `Watched Date` y `Year`,
- confirmar la regla de conteo para visualizaciones repetidas,
- y decidir si se analiza en términos de registros o de títulos únicos.

Esto permitirá que los análisis de nivel 2 sean más robustos y no se basen en suposiciones sobre el grano de los datos.
