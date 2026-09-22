"""Top-level enrichment workflow."""

import pandas as pd

from .config import Settings, settings
from .enrichment import enrich_ratings
from .tmdb import get_movie_genres


def run_enrichment(config: Settings = settings) -> None:
    print('Leyendo ratings.csv...')
    ratings = pd.read_csv(config.ratings_path)
    print(f'Películas encontradas: {len(ratings)}')
    print('\nObteniendo géneros de TMDB...')
    genre_map = get_movie_genres(config)
    print(f'Géneros disponibles: {len(genre_map)}')
    print('\nEnriqueciendo películas...\n')

    enriched_ratings = enrich_ratings(ratings, genre_map, config)
    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    enriched_ratings.to_csv(config.output_path, index=False)

    print('\nProceso terminado.')
    print(f'Dataset guardado en: {config.output_path}')
