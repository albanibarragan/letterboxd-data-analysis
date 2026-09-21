import json
import os
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')
GENRES_CACHE_PATH = Path('data/tmdb_genres.json')


def get_tmdb_headers() -> dict[str, str]:
    if not TMDB_TOKEN:
        raise ValueError('Falta la variable de entorno TMDB_ACCESS_TOKEN en el archivo .env')

    return {'Authorization': f'Bearer {TMDB_TOKEN}'}


def get_movie_genres() -> dict[int, str]:
    if GENRES_CACHE_PATH.exists():
        with open(GENRES_CACHE_PATH, 'r', encoding='utf-8') as file:
            cached = json.load(file)
            if isinstance(cached, dict):
                return {int(k): v for k, v in cached.items()}

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

    GENRES_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(GENRES_CACHE_PATH, 'w', encoding='utf-8') as file:
        json.dump(genre_map, file, ensure_ascii=False, indent=2)

    return genre_map


if __name__ == '__main__':
    genre_map = get_movie_genres()
    print(genre_map)
