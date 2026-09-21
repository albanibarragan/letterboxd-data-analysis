import json
import os
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv


# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

load_dotenv()

TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')

RATINGS_PATH = Path('data/ratings.csv')
GENRES_CACHE_PATH = Path('data/tmdb_genres.json')
MOVIES_CACHE_PATH = Path('data/tmdb_movies.json')
OUTPUT_PATH = Path('processed/ratings_enriched.csv')


# --------------------------------------------------
# AUTENTICACIÓN
# --------------------------------------------------

def get_tmdb_headers() -> dict[str, str]:
    """
    Crea las cabeceras necesarias para autenticarnos con TMDB.
    """

    if not TMDB_TOKEN:
        raise ValueError(
            'Falta la variable de entorno TMDB_ACCESS_TOKEN '
            'en el archivo .env'
        )

    return {
        'Authorization': f'Bearer {TMDB_TOKEN}'
    }


# --------------------------------------------------
# GÉNEROS
# --------------------------------------------------

def get_movie_genres() -> dict[int, str]:
    """
    Obtiene el catálogo de géneros de películas de TMDB.

    Si ya tenemos los géneros guardados localmente,
    utilizamos el archivo en lugar de hacer otra petición.
    """

    if GENRES_CACHE_PATH.exists():

        with open(
            GENRES_CACHE_PATH,
            'r',
            encoding='utf-8'
        ) as file:

            cached = json.load(file)

        if isinstance(cached, dict):

            return {
                int(genre_id): genre_name
                for genre_id, genre_name in cached.items()
            }

    response = requests.get(
        f'{TMDB_BASE_URL}/genre/movie/list',
        headers=get_tmdb_headers(),
        timeout=20,
    )

    response.raise_for_status()

    genres = response.json().get('genres', [])

    genre_map = {
        genre['id']: genre['name']
        for genre in genres
    }

    GENRES_CACHE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        GENRES_CACHE_PATH,
        'w',
        encoding='utf-8'
    ) as file:

        json.dump(
            genre_map,
            file,
            ensure_ascii=False,
            indent=2
        )

    return genre_map


# --------------------------------------------------
# CACHÉ DE PELÍCULAS
# --------------------------------------------------

def load_movies_cache() -> dict[str, Any]:
    """
    Carga las películas que ya hemos consultado a TMDB.
    """

    if not MOVIES_CACHE_PATH.exists():
        return {}

    with open(
        MOVIES_CACHE_PATH,
        'r',
        encoding='utf-8'
    ) as file:

        cache = json.load(file)

    if isinstance(cache, dict):
        return cache

    return {}


def save_movies_cache(
    movies_cache: dict[str, Any]
) -> None:
    """
    Guarda el caché de películas en disco.
    """

    MOVIES_CACHE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        MOVIES_CACHE_PATH,
        'w',
        encoding='utf-8'
    ) as file:

        json.dump(
            movies_cache,
            file,
            ensure_ascii=False,
            indent=2
        )


# --------------------------------------------------
# BUSCAR UNA PELÍCULA EN TMDB
# --------------------------------------------------

def normalize_title(title: str) -> str:
    return (
        str(title)
        .lower()
        .strip()
        .replace(':', '')
        .replace('-', ' ')
        .replace('  ', ' ')
    )


def title_similarity(title_a: str, title_b: str) -> float:
    normalized_a = normalize_title(title_a)
    normalized_b = normalize_title(title_b)

    return SequenceMatcher(
        None,
        normalized_a,
        normalized_b,
    ).ratio()


def get_movie_by_title_and_year(
    title: str,
    year: Any,
    genre_map: dict[int, str],
) -> dict[str, Any] | None:
    """
    Busca una película en TMDB utilizando título y año.

    El año es obligatorio para reducir falsos positivos.
    El título se compara con un margen de similitud flexible.
    """

    if not pd.notna(year):
        return None

    search_params = {
        'query': str(title).strip(),
        'include_adult': False,
        'year': int(year),
    }

    response = requests.get(
        f'{TMDB_BASE_URL}/search/movie',
        params=search_params,
        headers=get_tmdb_headers(),
        timeout=20,
    )

    response.raise_for_status()

    results = response.json().get('results', [])

    if not results:
        return None

    for movie in results:
        movie_title = movie.get('title', '')
        release_date = movie.get('release_date', '')

        year_matches = (
            str(release_date).startswith(str(int(year)))
        )

        if not year_matches:
            continue

        similarity = title_similarity(
            title,
            movie_title,
        )

        if similarity < 0.80:
            continue

        genre_ids = movie.get('genre_ids', [])
        genres = [
            genre_map[genre_id]
            for genre_id in genre_ids
            if genre_id in genre_map
        ]

        return {
            'tmdb_id': movie.get('id'),
            'title': movie.get('title'),
            'year': int(year),
            'genres': genres,
        }

    return None


# --------------------------------------------------
# PROCESAR RATINGS
# --------------------------------------------------

def enrich_ratings(
    ratings: pd.DataFrame,
    genre_map: dict[int, str],
) -> pd.DataFrame:
    """
    Añade los géneros de TMDB a nuestro ratings.csv.
    """

    movies_cache = load_movies_cache()

    enriched_rows = []

    total_movies = len(ratings)

    for index, row in ratings.iterrows():

        title = str(row['Name']).strip()
        year = row['Year']

        cache_key = f'{title}|{int(year)}'

        print(
            f'[{index + 1}/{total_movies}] {title} ({int(year)})'
        )

        # ------------------------------------------
        # 1. Buscar primero en caché
        # ------------------------------------------

        if cache_key in movies_cache:

            movie_data = movies_cache[cache_key]

            print('  → Usando caché')

        else:

            # --------------------------------------
            # 2. Si no existe, consultar TMDB
            # --------------------------------------

            print('  → Consultando TMDB...')

            movie_data = get_movie_by_title_and_year(
                title,
                year,
                genre_map,
            )

            # --------------------------------------
            # 3. Guardar respuesta en caché
            # --------------------------------------

            if movie_data is not None:

                movies_cache[cache_key] = movie_data

                save_movies_cache(movies_cache)

                print('  → Guardado en caché')

            else:

                print('  → No encontrada en TMDB')

                movies_cache[cache_key] = None

                save_movies_cache(movies_cache)

        # ------------------------------------------
        # 4. Crear nueva fila
        # ------------------------------------------

        new_row = row.copy()

        if movie_data:

            genres = movie_data.get(
                'genres',
                []
            )

            new_row['Genres'] = '|'.join(genres)

            new_row['TMDB ID'] = movie_data.get(
                'tmdb_id'
            )

        else:

            new_row['Genres'] = ''
            new_row['TMDB ID'] = None

        enriched_rows.append(new_row)

    return pd.DataFrame(enriched_rows)



def main():
    print('Leyendo ratings.csv...')
    ratings = pd.read_csv(RATINGS_PATH)
    print(f'Películas encontradas: {len(ratings)}')
    print('\nObteniendo géneros de TMDB...')

    genre_map = get_movie_genres()

    print(
        f'Géneros disponibles: {len(genre_map)}'
    )

    print('\nEnriqueciendo películas...\n')

    enriched_ratings = enrich_ratings(
        ratings,
        genre_map,
    )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    enriched_ratings.to_csv(
        OUTPUT_PATH,
        index=False
    )

    print('\nProceso terminado.')
    print(
        f'Dataset guardado en: {OUTPUT_PATH}'
    )


if __name__ == '__main__':
    main()