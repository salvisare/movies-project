import json


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    """Loads movie data from the JSON file and returns it as a dictionary."""
    with open("movies_data.json", "r") as file:
        return json.load(file)


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("movies_data.json", "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, rating, year):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    # Check if the movie already exists
    if title in movies:
        print(f"Movie '{title}' already exists.")
        return

    movies[title] = {
        "rating": rating,
        "year": year
    }

    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    # Ensure `title` is treated as a string and check if it exists in the movies
    if title in movies:
        del movies[title]
        save_movies(movies)
    else:
        print(f"Movie '{title}' does not exist in the database.")


def update_movie(title, rating, year):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()

    # Check if the movie already exists
    if title not in movies:
        print(f"Movie '{title}' doesn't exist.")
        return

    movies[title] = {
        "rating": rating,
        "year": year
    }

    save_movies(movies)
