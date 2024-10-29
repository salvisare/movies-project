import csv
from storage.istorage import IStorage

class StorageCsv(IStorage):
    """Storage class for managing movies in a CSV file format."""

    def __init__(self, file_path):
        """Initialize the data with the file path for the CSV data."""
        self.file_path = file_path


    # def _load_movies(self):
    #     """Load movies from the CSV file into a dictionary."""
    #     movies = {}
    #     try:
    #         with open(self.file_path, mode='r', newline='') as csvfile:
    #             reader = csv.DictReader(csvfile)
    #             for row in reader:
    #                 print("Row read from CSV:", row)  # Debug: Print the entire row
    #                 # Convert rating to float and year to int
    #                 movies[row['title']] = {
    #                     "rating": float(row['rating']),
    #                     "year": int(row['year']),
    #                     "poster": row.get('poster', '')  # Default to empty string if 'poster' is missing
    #                 }
    #                 #print("Movie loaded:", movies[row['title']])  # Debug: Print the loaded movie data
    #     except FileNotFoundError:
    #         # Return an empty dictionary if file doesn't exist
    #         return {}
    #     return movies

    def _load_movies(self):
        """Load movies from the CSV file into a dictionary."""
        movies = {}
        try:
            with open(self.file_path, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    title = row.get('title', '').strip()
                    rating = float(row.get('rating', 0.0))  # Set default to 0.0 if rating missing
                    year = int(row.get('year', 0))  # Set default to 0 if year missing
                    poster = row.get('poster', '').strip()  # Default to empty string if poster missing

                    # Confirm we’re storing the data correctly
                    movies[title] = {
                        "rating": rating,
                        "year": year,
                        "poster": poster
                    }

        except FileNotFoundError:
            # Return an empty dictionary if file doesn't exist
            return {}

        return movies

    def _save_movies(self, movies):
        """Save the movies dictionary back to the CSV file."""
        with open(self.file_path, mode='w', newline='') as csvfile:
            fieldnames = ['title', 'rating', 'year', 'poster']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': details['rating'],
                    'year': details['year'],
                    'poster': details.get('poster', '')  # Include poster if available
                })

    def list_movies(self):
        """List all movies with their details."""
        return self._load_movies()

    def add_movie(self, title, rating, year, poster):
        """Add a new movie to the CSV data."""
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
        """Delete a movie from the CSV data by its title."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
            print(f"Movie '{title}' deleted successfully.")
        else:
            print(f"Movie '{title}' does not exist in the database.")

    def update_movie(self, title, rating, year, poster):
        """Update the rating or year of a movie in CSV data."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            movies[title]["year"] = year
            movies[title]["poster"] = poster
            self._save_movies(movies)
            print(f"Movie '{title}' updated successfully.")
        else:
            print(f"Movie '{title}' does not exist in the database.")
