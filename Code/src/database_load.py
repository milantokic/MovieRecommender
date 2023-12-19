from Movies import Movie
import pandas as pd

movies = pd.read_csv(r"C:\Users\Toka\GIT\MovieRecommender\Code\Data\data_small.csv")
for index, row in movies.iterrows():
    Movie(title=row['primaryTitle'], year=row['startYear'], genres=row['genres'].split(','), runtime=row['runtimeMinutes'])
