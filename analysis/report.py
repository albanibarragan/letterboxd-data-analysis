"""Exploratory metrics and visualizations for Letterboxd exports."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / 'data'
VISUALIZATIONS_DIR = PROJECT_ROOT / 'visualizations'


def load_and_prepare_data(data_dir: Path = DATA_DIR):
    ratings = pd.read_csv(data_dir / 'ratings.csv')
    diary = pd.read_csv(data_dir / 'diary.csv')
    ratings['Date'] = pd.to_datetime(ratings['Date'], errors='coerce')
    diary['Watched Date'] = pd.to_datetime(
        diary['Watched Date'],
        errors='coerce',
    )
    ratings['rating_year'] = ratings['Date'].dt.year
    diary['view_year'] = diary['Watched Date'].dt.year
    return ratings, diary


def show_dataset_summary(name: str, frame: pd.DataFrame) -> None:
    print(f'\nEstructura de {name}:')
    frame.info()
    print(frame.head())


def show_rating_quality_checks(ratings: pd.DataFrame) -> None:
    print('\nValidación de ratings:')
    print('Valores nulos:')
    print(ratings.isnull().sum())
    print('\nDuplicados:')
    print(ratings.duplicated().sum())
    print('\nValores únicos de Rating:')
    print(sorted(ratings['Rating'].dropna().unique().tolist()))


def show_basic_metrics(ratings: pd.DataFrame) -> None:
    print('\nMétricas básicas:')
    print('Películas calificadas:', len(ratings))
    print('Calificación promedio:', round(ratings['Rating'].mean(), 2))
    mode_rating = ratings['Rating'].mode()
    if mode_rating.empty:
        print('No hay calificaciones disponibles.')
    else:
        print('Calificación más utilizada:', mode_rating.iloc[0])


def show_max_rating_movies(ratings: pd.DataFrame) -> None:
    max_rating = ratings['Rating'].max()
    movies = ratings[ratings['Rating'] == max_rating]
    print('\nPelículas con calificación máxima:')
    print(movies['Name'].tolist())
    print(f'Cantidad con {max_rating}:', len(movies))


def show_distribution(ratings: pd.DataFrame, diary: pd.DataFrame) -> None:
    print('\nDistribución de calificaciones:')
    print(ratings['Rating'].value_counts().sort_index())
    print('\nVisualizaciones por año:')
    print(diary['view_year'].value_counts().sort_index())


def plot_year_activity(
    ratings: pd.DataFrame,
    diary: pd.DataFrame,
    output_dir: Path = VISUALIZATIONS_DIR,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    activity = pd.DataFrame({
        'Películas calificadas': ratings['rating_year'].value_counts(),
        'Visualizaciones registradas': diary['view_year'].value_counts(),
    }).fillna(0)
    activity.sort_index().plot(kind='bar', figsize=(10, 6))
    plt.title('Películas calificadas y visualizaciones por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=0)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / 'activity_by_year.png', dpi=300)
    plt.close()


def plot_rating_distribution(
    ratings: pd.DataFrame,
    output_dir: Path = VISUALIZATIONS_DIR,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    ratings['Rating'].value_counts().sort_index().plot(
        kind='bar',
        figsize=(10, 6),
    )
    plt.title('Distribución de ratings')
    plt.xlabel('Rating')
    plt.ylabel('Cantidad de películas')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_dir / 'ratings_distribution.png', dpi=300)
    plt.close()


def plot_top_movies(
    ratings: pd.DataFrame,
    output_dir: Path = VISUALIZATIONS_DIR,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    top_movies = ratings.sort_values(
        by=['Rating', 'Name'],
        ascending=[False, True],
    ).head(10)
    plt.figure(figsize=(10, 6))
    plt.bar(top_movies['Name'], top_movies['Rating'], color='steelblue')
    plt.title('Top 10 películas por rating')
    plt.xlabel('Película')
    plt.ylabel('Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir / 'top_movies.png', dpi=300)
    plt.close()


def run_report() -> None:
    ratings, diary = load_and_prepare_data()
    show_dataset_summary('ratings', ratings)
    show_rating_quality_checks(ratings)
    show_basic_metrics(ratings)
    show_dataset_summary('diary', diary)
    show_max_rating_movies(ratings)
    show_distribution(ratings, diary)
    plot_year_activity(ratings, diary)
    plot_rating_distribution(ratings)
    plot_top_movies(ratings)
    print(f'\nGráficos guardados en: {VISUALIZATIONS_DIR.resolve()}')
