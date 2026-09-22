"""TMDB API access, title matching, and movie metadata mapping."""

import json
import re
from difflib import SequenceMatcher
from typing import Any

import pandas as pd
import requests

from .config import Settings, settings

MOVIE_DATA_FIELDS = (
    'tmdb_id',
    'genres',
    'runtime',
    'release_date',
    'tmdb_rating',
    'tmdb_vote_count',
    'original_language',
    'popularity',
)


def get_tmdb_headers(config: Settings = settings) -> dict[str, str]:
    if not config.tmdb_access_token:
        raise ValueError(
            'Falta TMDB_ACCESS_TOKEN en el archivo .env o en el entorno.'
        )
    return {'Authorization': f'Bearer {config.tmdb_access_token}'}


def _request(
    path: str,
    *,
    params: dict[str, Any] | None = None,
    config: Settings = settings,
) -> dict[str, Any]:
    response = requests.get(
        f'{config.tmdb_base_url}/{path.lstrip("/")}',
        params=params,
        headers=get_tmdb_headers(config),
        timeout=config.request_timeout,
    )
    response.raise_for_status()
    return response.json()


def load_json_cache(path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open('r', encoding='utf-8') as file:
        cache = json.load(file)
    return cache if isinstance(cache, dict) else {}


def save_json_cache(path, cache: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as file:
        json.dump(cache, file, ensure_ascii=False, indent=2)


def get_movie_genres(config: Settings = settings) -> dict[int, str]:
    cached = load_json_cache(config.genres_cache_path)
    if cached:
        return {int(genre_id): name for genre_id, name in cached.items()}

    payload = _request('genre/movie/list', config=config)
    genre_map = {
        genre['id']: genre['name']
        for genre in payload.get('genres', [])
    }
    save_json_cache(config.genres_cache_path, genre_map)
    return genre_map


def normalize_title(title: str) -> str:
    title = str(title).lower().strip()
    title = title.replace(':', '').replace('-', ' ')
    return re.sub(r'\s+', ' ', title)


def title_similarity(title_a: str, title_b: str) -> float:
    return SequenceMatcher(
        None,
        normalize_title(title_a),
        normalize_title(title_b),
    ).ratio()


def select_best_movie(
    results: list[dict[str, Any]],
    title: str,
    year: int,
    require_year_match: bool,
) -> tuple[dict[str, Any] | None, float]:
    best_match = None
    best_similarity = 0.0
    best_year_distance = float('inf')

    for movie in results:
        release_year = str(movie.get('release_date', ''))[:4]
        if require_year_match and release_year != str(year):
            continue
        if not release_year.isdigit():
            continue

        similarity = title_similarity(title, movie.get('title', ''))
        year_distance = abs(year - int(release_year))
        if (
            similarity > best_similarity
            or (
                similarity == best_similarity
                and year_distance < best_year_distance
            )
        ):
            best_match = movie
            best_similarity = similarity
            best_year_distance = year_distance

    return best_match, best_similarity


def get_movie_by_title_and_year(
    title: str,
    year: Any,
    genre_map: dict[int, str],
    config: Settings = settings,
) -> dict[str, Any] | None:
    if not pd.notna(year):
        return None

    year = int(year)
    search_params = {
        'query': str(title).strip(),
        'include_adult': False,
        'year': year,
    }
    results = _request('search/movie', params=search_params, config=config).get(
        'results', []
    )
    best_match, best_similarity = select_best_movie(
        results, title, year, require_year_match=True
    )

    if best_match is None or best_similarity < 0.80:
        results = _request(
            'search/movie',
            params={'query': str(title).strip(), 'include_adult': False},
            config=config,
        ).get('results', [])
        best_match, best_similarity = select_best_movie(
            results, title, year, require_year_match=False
        )
        if best_match is None or best_similarity < 0.80:
            return None

    movie_id = best_match.get('id')
    if movie_id is None:
        return None

    details = _request(f'movie/{movie_id}', config=config)
    genres = [
        genre['name']
        for genre in details.get('genres', [])
        if genre.get('name')
    ]
    if not genres:
        genres = [
            genre_map[genre_id]
            for genre_id in best_match.get('genre_ids', [])
            if genre_id in genre_map
        ]

    return {
        'tmdb_id': movie_id,
        'title': best_match.get('title'),
        'year': year,
        'genres': genres,
        'runtime': details.get('runtime'),
        'release_date': details.get('release_date'),
        'tmdb_rating': details.get('vote_average'),
        'tmdb_vote_count': details.get('vote_count'),
        'original_language': details.get('original_language'),
        'popularity': details.get('popularity'),
        'match_similarity': round(best_similarity, 3),
    }


def has_complete_movie_data(movie_data: Any) -> bool:
    return (
        isinstance(movie_data, dict)
        and all(field in movie_data for field in MOVIE_DATA_FIELDS)
    )
