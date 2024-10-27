import json
from istorage import IStorage


class StorageJson(IStorage):
    """Storage class for managing movies in a JSON file."""

    def __init__(self, file_path):
        """Initialize the storage with the file path for the JSON data."""
        self.file_path = file_path

    def _load_movies(self):
        """Load movies from the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_movies(self, movies):
        """Save the updated movies dictionary back to the JSON file."""
        with open(self.file_path, 'w') as f:
            json.dump(movies, f, indent=4)

    def list_movies(self):
        """List all movies with their details."""
        return self._load_movies()

    def add_movie(self, title, rating, year, poster):
        """Add a new movie to the JSON storage."""
        movies = self._load_movies()
        if title in movies:
            print(f"Movie '{title}' already exists.")
            return
        movies[title] = {
            "rating": rating,
            "year": year,
            "poster": poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """Delete a movie from JSON storage by its title."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
        else:
            print(f"Movie '{title}' does not exist in the database.")

    def update_movie(self, title, rating, year):
        """Update the rating or year of a movie."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            movies[title]["year"] = year
            self._save_movies(movies)
        else:
            print(f"Movie '{title}' does not exist in the database.")