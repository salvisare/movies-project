from abc import ABC, abstractmethod


class IStorage(ABC):
    """Interface for data operations on movies data."""
    @abstractmethod
    def list_movies(self):
        """List all movies from data."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Add a new movie to data with title, year, rating, and poster URL."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Delete a movie by title from data."""
        pass

    @abstractmethod
    def update_movie(self, title, rating, year, poster):
        """"Update a movie's rating or year in data by title."""
        pass
