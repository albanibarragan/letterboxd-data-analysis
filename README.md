# Letterboxd Data Analysis

Proyecto en Python para analizar los datos de Letterboxd y convertirlos en información útil sobre mis hábitos cinematográficos.

## ¿Qué problema resolvemos?

Tengo los datos registrados de Letterboxd, pero por sí solos no permiten entender claramente mis hábitos de consumo y calificación. Con casi 500 películas registradas, quiero transformar esa información en métricas y visualizaciones que me ayuden a responder preguntas relevantes sobre mi actividad.

## Objetivo

Realizar un análisis exploratorio de mis datos de Letterboxd para responder preguntas simples sobre:

- cuántas películas he calificado,
- mi calificación promedio,
- la calificación que uso más,
- cuántas películas he calificado por año,
- y cuáles son mis películas con calificación máxima.

## Preguntas principales

- [ ] ¿Cuántas películas he calificado?
- [ ] ¿Cuál es mi calificación promedio?
- [ ] ¿Qué calificación utilizo más?
- [ ] ¿Cuántas películas he calificado por año?
- [ ] ¿Cuáles son mis películas con calificación máxima?

## Stack tecnológico

- Python
- Pandas
- Jupyter Notebook o scripts de análisis
- Matplotlib / Seaborn para visualizaciones

## Estructura del proyecto

```text
letterboxd-data-analysis/
├── data/
│   ├── ratings.csv
│   ├── diary.csv
│   ├── watched.csv
│   └── ...
├── analysis.py
├── visualizations/
│   ├── ratings_distribution.png
│   ├── activity_by_year.png
│   └── top_movies.png
├── README.md
├── .gitignore
└── docs/
    ├── contexto.md
    ├── questions.md
    ├── estructura.md
    └── Roadmap.md
```

## Requisitos

- Python 3.x
- pip

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate   # En Linux/macOS
.venv\Scripts\activate      # En Windows
pip install pandas matplotlib seaborn jupyter
```

## Uso

1. Copiar `.env.example` como `.env` y completar `TMDB_ACCESS_TOKEN`.
2. Colocar los CSV originales de Letterboxd en `data/`.
3. Ejecutar `python main.py` para generar el dataset enriquecido.
4. Ejecutar `python -m analysis` para generar métricas y visualizaciones.

## Estructura de ejecución

- `main.py`: entrada mínima del pipeline de enriquecimiento.
- `src/letterboxd_analysis/config.py`: configuración y rutas.
- `src/letterboxd_analysis/tmdb.py`: API, matching y metadatos de TMDB.
- `src/letterboxd_analysis/enrichment.py`: combinación de Letterboxd y TMDB.
- `src/letterboxd_analysis/pipeline.py`: orquestación de la exportación.
- `analysis/`: análisis exploratorio y generación explícita de gráficos.

Los directorios `processed/` y `visualizations/` se generan localmente y no
se versionan. El caché de TMDB permanece en `data/` junto a los datos locales.

## Nota

Este proyecto está pensado como un ejercicio de análisis de datos personales y exploración de hábitos de visualización cinematográfica.
