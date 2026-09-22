"""Enrich Letterboxd ratings while preserving source columns."""

from typing import Any

import pandas as pd

from .config import Settings, settings
from .tmdb import (
    get_movie_by_title_and_year,
    has_complete_movie_data,
    load_json_cache,
    save_json_cache,
)

TMDB_OUTPUT_COLUMNS = (
    'Genres',
    'TMDB ID',
    'Runtime',
    'Release Date',
    'TMDB Rating',
    'TMDB Vote Count',
    'Original Language',
    'Popularity',
)


def enrich_ratings(
    ratings: pd.DataFrame,
    genre_map: dict[int, str],
    config: Settings = settings,
) -> pd.DataFrame:
    movies_cache = load_json_cache(config.movies_cache_path)
    enriched_rows = []

    for index, row in ratings.iterrows():
        title = str(row['Name']).strip()
        year = row['Year']
        cache_key = f'{title}|{int(year)}'
        print(f'[{index + 1}/{len(ratings)}] {title} ({int(year)})')

        movie_data = movies_cache.get(cache_key)
        if has_complete_movie_data(movie_data):
            print('  -> Usando cache')
        else:
            print('  -> Consultando TMDB...')
            movie_data = get_movie_by_title_and_year(
                title,
                year,
                genre_map,
                config,
            )
            if movie_data is not None:
                movies_cache[cache_key] = movie_data
                save_json_cache(config.movies_cache_path, movies_cache)
                print('  -> Guardado en cache')
            else:
                print('  -> No encontrada en TMDB')

        new_row = row.copy()
        metadata = movie_data or {}
        new_row['Genres'] = '|'.join(metadata.get('genres', []))
        new_row['TMDB ID'] = metadata.get('tmdb_id')
        new_row['Runtime'] = metadata.get('runtime')
        new_row['Release Date'] = metadata.get('release_date')
        new_row['TMDB Rating'] = metadata.get('tmdb_rating')
        new_row['TMDB Vote Count'] = metadata.get('tmdb_vote_count')
        new_row['Original Language'] = metadata.get('original_language')
        new_row['Popularity'] = metadata.get('popularity')
        enriched_rows.append(new_row)

    enriched = pd.DataFrame(enriched_rows)
    preferred_original_columns = [
        column for column in ('Name', 'Year', 'Letterboxd URI', 'Rating')
        if column in ratings.columns
    ]
    other_original_columns = [
        column
        for column in ratings.columns
        if column not in preferred_original_columns
    ]
    output_columns = (
        preferred_original_columns
        + other_original_columns
        + list(TMDB_OUTPUT_COLUMNS)
    )
    return enriched[output_columns]
