from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


VISUALIZATIONS_DIR = Path('visualizations')
VISUALIZATIONS_DIR.mkdir(exist_ok=True)


def load_and_prepare_data():
    ratings = pd.read_csv('data/ratings.csv')
    diary = pd.read_csv('data/diary.csv')

    ratings['Date'] = pd.to_datetime(ratings['Date'], errors='coerce')
    ratings['rating_year'] = ratings['Date'].dt.year

    diary['Watched Date'] = pd.to_datetime(diary['Watched Date'], errors='coerce')
    diary['view_year'] = diary['Watched Date'].dt.year

    return ratings, diary


def show_dataset_summary(name, df):
    print(f'\nConocer la estructura de {name}:')
    df.info()
    print(df.head())


def show_rating_quality_checks(ratings):
    print('\nValidación de ratings:')
    print('Valores nulos:')
    print(ratings.isnull().sum())

    print('\nDuplicados:')
    print(ratings.duplicated().sum())

    print('\nValores únicos de Rating:')
    print(sorted(ratings['Rating'].unique().tolist()))


def show_basic_metrics(ratings):
    print('\nMétricas básicas:')
    print('Películas calificadas:', len(ratings))
    print('Calificación promedio:', round(ratings['Rating'].mean(), 2))

    mode_rating = ratings['Rating'].mode()
    if not mode_rating.empty:
        print('Calificación más utilizada:', mode_rating.iloc[0])
    else:
        print('No hay calificaciones disponibles.')


def show_max_rating_movies(ratings):
    max_rating = ratings['Rating'].max()
    max_rated_movies = ratings[ratings['Rating'] == max_rating]

    print('\nPelículas con calificación máxima:')
    print(max_rated_movies['Name'].tolist())
    print(f'Cantidad de películas clasificadas con {max_rating}:', len(max_rated_movies))


def show_distribution(ratings, diary):
    rating_counts = ratings['Rating'].value_counts().sort_index()
    view_year_counts = diary['view_year'].value_counts().sort_index()

    print('\nDistribución de calificaciones:')
    print(rating_counts)

    print('\nVisualizaciones por año:')
    print(view_year_counts)


def plot_year_activity(ratings, diary):
    rating_year_counts = ratings['rating_year'].value_counts().sort_index()
    view_year_counts = diary['view_year'].value_counts().sort_index()

    year_activity = pd.DataFrame({
        'Películas calificadas': rating_year_counts,
        'Visualizaciones registradas': view_year_counts
    }).fillna(0)

    year_activity.plot(kind='bar', figsize=(10, 6))
    plt.title('Películas calificadas y visualizaciones por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=0)
    plt.legend()
    plt.tight_layout()
    plt.savefig(VISUALIZATIONS_DIR / 'activity_by_year.png', dpi=300)
    plt.close()


def plot_rating_distribution(ratings):
    rating_counts = ratings['Rating'].value_counts().sort_index()

    rating_counts.plot(kind='bar', figsize=(10, 6))
    plt.title('Distribución de ratings')
    plt.xlabel('Rating')
    plt.ylabel('Cantidad de películas')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(VISUALIZATIONS_DIR / 'ratings_distribution.png', dpi=300)
    plt.close()


def plot_top_movies(ratings):
    top_movies = ratings.sort_values(by=['Rating', 'Name'], ascending=[False, True]).head(10)

    plt.figure(figsize=(10, 6))
    plt.bar(top_movies['Name'], top_movies['Rating'], color='steelblue')
    plt.title('Top 10 películas por rating')
    plt.xlabel('Película')
    plt.ylabel('Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(VISUALIZATIONS_DIR / 'top_movies.png', dpi=300)
    plt.close()


def show_top_movies(ratings):
    top_movies = ratings.sort_values(by=['Rating', 'Name'], ascending=[False, True])
    print('\nTop 10 películas:')
    print(top_movies[['Name', 'Rating']].head(10))


if __name__ == '__main__':
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
    show_top_movies(ratings)

    print(f'\nGráficos guardados en: {VISUALIZATIONS_DIR.resolve()}')