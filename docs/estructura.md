## Estructura de los datos

### 1. Descripción general

Este conjunto de datos contiene la información de las películas calificadas por el usuario en Letterboxd. Cada registro representa una valoración individual, con metadata básica de la película y la fecha en que se registró la calificación.

### 2. Columnas del dataset

- Date: texto (str)
- Name: texto (str)
- Year: entero (int)
- Letterboxd URI: texto (str)
- Rating: decimal (float)

### 3. Tipos de datos originales

- Date llega como texto, no como fecha; por tanto, requiere conversión posterior con `pd.to_datetime()`.
- Year se almacena como entero.
- Rating se almacena como decimal.

### 4. Validación de calidad de datos

#### Rating

Los valores únicos en esta columna son los siguientes:

- 0.5
- 1.0
- 1.5
- 2.0
- 2.5
- 3.0
- 3.5
- 4.0
- 4.5
- 5.0

Esto confirma que el sistema de calificación utiliza una escala de 0.5 a 5.0, con incrementos de 0.5.

#### Duplicados

- No existen registros duplicados.
- No se identifican combinaciones repetidas de Name + Year.

#### Rango de fechas

- El rango de fechas es válido.
- No hay fechas nulas.
- No se observan fechas futuras incorrectas.
- El conjunto abarca desde 2023-10-28 hasta 2026-08-22.

### 5. ¿Qué representa cada fila?

Cada fila representa una película calificada una sola vez por el usuario, identificada por:

- su nombre,
- su año de estreno,
- la fecha de la valoración,
- la URL de la película en Letterboxd,
- y la puntuación otorgada.

En términos prácticos, cada registro corresponde a una valoración única de una película dentro del historial del usuario.

