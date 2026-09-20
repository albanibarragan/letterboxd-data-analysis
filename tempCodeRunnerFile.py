import pandas as pd

# leer csv
ratings = pd.read_csv('data/ratings.csv') 

print(ratings.head())
print('Conocer la estructura')
print(ratings.info())
# ¿Cuántas películas he calificado?
print('He calificado:', len(ratings))

# ¿Cuál es mi calificación promedio?
rating = ratings['Rating']
print(rating)