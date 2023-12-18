from src.Movies import Movie
import pandas as pd

try:
    mov1 = Movie(title = 'titlee', genres=['horror'], year=1994, runtime=99)
except ValueError as e:
    print(f"Error: {e}")
else:
    print(mov1)
