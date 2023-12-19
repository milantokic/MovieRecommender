import sqlite3


def create_connection():
    return sqlite3.connect(r'C:\Users\Toka\GIT\MovieRecommender\Code\src\movie_database.db')


def setup_movie_table(connection):
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
            id INT NOT NULL,
            title TEXT NOT NULL,
            genres TEXT NOT NULL,
            year INTEGER NOT NULL,
            runtime INTEGER NOT NULL
        )
    ''')
    connection.commit()


def setup_user_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
    id INT NOT NULL,
    username TEXT NOT NULL
    )
    ''')
    connection.commit()


def setup_user_watched_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_watched (
    user_id INT NOT NULL,
    movie_id INT NOT NULL
    )
    ''')
    connection.commit()


def setup_rating_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rating (
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    score FLOAT,
    review VARCHAR
    )
    ''')
