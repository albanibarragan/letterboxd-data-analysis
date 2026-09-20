import pandas as pd

# Leer CSV
ratings = pd.read_csv('data/ratings.csv')

# Convertir Date a datetime
ratings['Date'] = pd.to_datetime(ratings['Date'], errors='coerce')

# Exploración de ratings
print('Conocer la estructura de ratings:')
ratings.info()
print(ratings.head())

# Validación de ratings
print('\nValores nulos:', ratings.isnull().sum())
print('\nDuplicados:', ratings.duplicated().sum())
print('\nValores de Rating:', sorted(ratings['Rating'].unique()))

# ¿Cuántas películas he calificado?
rated_movies = len(ratings)
print('\nMovies rated:', rated_movies)

# ¿Cuál es mi calificación promedio?
average_rating = ratings['Rating'].mean()
print('Calificación promedio:', round(average_rating, 2))

# ¿Qué calificación utilizo más?
mode_rating = ratings['Rating'].mode()

if not mode_rating.empty:
    print('Calificación más utilizada:', mode_rating.iloc[0])
else:
    print('No hay calificaciones disponibles.')

diary = pd.read_csv('data/diary.csv')

print('\nConocer la estructura de diary:')
diary.info()
print(diary.head())

# Convertimos la fecha real de visualización a datetime.
diary['Watched Date'] = pd.to_datetime(diary['Watched Date'], errors='coerce')

# Extraemos el año de la visualización.
diary['view_year'] = diary['Watched Date'].dt.year

# Contamos los logs/visualizaciones por año.
view_year_counts = diary['view_year'].value_counts().sort_index()

print('\nVisualizaciones por año:')
print(view_year_counts)


# ¿Cuáles son mis películas con calificación máxima?
max_rating = ratings['Rating'].max()
print('\nCalificación máxima:', max_rating)

max_rated_movies = ratings[ratings['Rating'] == max_rating]

print('Películas con calificación máxima:')
print(max_rated_movies['Name'].tolist())

print(
    f'Cantidad de películas clasificadas con {max_rating}:',
    len(max_rated_movies)
)

# ¿Cómo se distribuyen mis calificaciones?
rating_counts = ratings['Rating'].value_counts().sort_index()

print('\nDistribución de calificaciones:')
print(rating_counts)