# Inventario de fuentes de datos

## 1. Fuente y propósito

- Fuente: Letterboxd
- Tipo: exportación de datos en CSV
- Uso: analizar las películas calificadas y vistas por el usuario
- Fuente principal del análisis: ratings.csv
- Uso: Analizar las películas calificadas por el usuario.

## 2. Documentos disponibles

### Archivos principales

1. `profile.csv`
2. `comments.csv`
3. `diary.csv`
4. `ratings.csv`
5. `reviews.csv`
6. `watched.csv`
7. `watchlist.csv`
8. `likes/films.csv`
9. `likes/reviews.csv`
10. `likes/lists.csv`

### Archivos de contexto y limpieza

- `deleted/comments.csv`
- `deleted/diary.csv`
- `deleted/reviews.csv`
- `deleted/lists/priority-list-1.csv`
- `orphaned/comments.csv`
- `orphaned/diary.csv`
- `orphaned/reviews.csv`
- `lists/*.csv`

## 3. Volumen de registros

| Archivo | Filas (sin encabezado) |
| --- | ---: |
| watched.csv | 789 |
| diary.csv | 535 |
| ratings.csv | 496 |
| watchlist.csv | 306 |
| reviews.csv | 151 |
| comments.csv | 46 |

### Observación clave

Hay 789 títulos únicos vistos en `watched.csv`, de los cuales 496 tienen calificación explícita y 151 incluyen reseña escrita. Esto deja 293 películas vistas sin calificación.

## 4. Estructura de columnas clave

| Columna | Aparece en | Tipo | Significado |
| --- | --- | --- | --- |
| Date | todos | fecha (string → date) | Fecha del registro o log en Letterboxd; no siempre coincide con la fecha de visionado |
| Watched Date | diary, reviews | fecha | Fecha real en que se vio la película; más confiable que `Date` |
| Name, Year | casi todos | texto / entero | Título y año de estreno |
| Letterboxd URI | casi todos | URL | Identificador único de la entrada en Letterboxd |
| Rating | diary, ratings, reviews | float (0.5–5.0, pasos de 0.5) | Calificación del usuario |
| Rewatch | diary, reviews | `Yes` / vacío | Indica si fue un rewatch |
| Tags | diary, reviews | texto libre separado por comas | Etiquetas personales, por ejemplo: `con leila` |
| Review | reviews.csv | texto largo | Reseña escrita |

## 5. Calidad de los datos

### Valores faltantes

- `diary.csv`: 7 filas sin `Rating`; 475 de 535 sin `Rewatch` (es normal, porque el valor vacío significa “no fue rewatch”); 477 sin `Tags`.
- `watchlist.csv`: 2 filas sin `Year` (películas sin año catalogado todavía en Letterboxd, por ejemplo: “Untitled Rom-Com Film”).

### Duplicados

- Hay 2 pares de filas duplicadas en `diary.csv` con el mismo título, año y fecha de visionado.
- Parecen duplicados accidentales, como en los casos de “Robot Dreams” y “Taylor Swift: The Eras Tour”, ambos registrados en 2024-03.

### Valores extraños o casos límite

- No se detectan valores fuera de rango en la escala de calificación.
- Los archivos bajo `deleted/` y `orphaned/` corresponden a contenido eliminado o películas retiradas del catálogo, no a datos adicionales relevantes.
- Los “huérfanos” son casos donde la película fue eliminada de la base de Letterboxd y quedó sin `URI`.

### Consistencia entre archivos

- `watched.csv` tiene 789 registros y `diary.csv` tiene 535.
- Esta diferencia es normal, porque `watched.csv` incluye películas marcadas como vistas sin necesidad de que hayan pasado por el diario cronológico.

### Rango de calificaciones

- La escala es correcta: entre 0.5 y 5.0 en incrementos de 0.5.
- No hay valores fuera del rango estándar de Letterboxd.

## 6. Limitaciones del dataset

- No contamos con datos demográficos de otros usuarios.
- No hay información de géneros, directores, duración ni metadatos adicionales de las películas; Letterboxd no los exporta en este formato.
- Si se quiere enriquecer la base, habría que cruzarla con fuentes como TMDB u OMDB.
- No se tienen “me gusta” recibidos en las reseñas propias.
- El formato de exportación de Letterboxd presenta diferencias importantes:
  - `Date` no siempre coincide con `Watched Date`; el primero indica cuándo se registró la entrada, no necesariamente cuándo se vio la película.
  - `deleted/` y `orphaned/` reflejan idiosincrasias del sistema de Letterboxd y no son datos “reales” adicionales.
  - Los `Tags` son texto libre y no están normalizados; por ejemplo, `con leila` puede escribirse de formas distintas en diferentes filas.

