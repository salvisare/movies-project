from abc import ABC, abstractmethod


class IStorage(ABC):
    """Interface for storage operations on movies data."""
    @abstractmethod
    def list_movies(self):
        """List all movies from storage."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Add a new movie to storage with title, year, rating, and poster URL."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Delete a movie by title from storage."""
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """"Update a movie's rating or year in storage by title."""
        pass
