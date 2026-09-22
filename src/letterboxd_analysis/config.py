"""Application configuration loaded from environment variables."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / '.env')


@dataclass(frozen=True)
class Settings:
    project_root: Path = PROJECT_ROOT
    tmdb_base_url: str = os.getenv(
        'TMDB_BASE_URL',
        'https://api.themoviedb.org/3',
    ).rstrip('/')
    tmdb_access_token: str | None = os.getenv('TMDB_ACCESS_TOKEN')
    ratings_path: Path = PROJECT_ROOT / 'data' / 'ratings.csv'
    genres_cache_path: Path = PROJECT_ROOT / 'data' / 'tmdb_genres.json'
    movies_cache_path: Path = PROJECT_ROOT / 'data' / 'tmdb_movies.json'
    output_path: Path = PROJECT_ROOT / 'processed' / 'ratings_enriched.csv'
    request_timeout: int = 20


settings = Settings()
