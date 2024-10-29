from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp
from omdb_api import get_movie_details

def main():
    api_key = "23cc239c"
    storage = StorageCsv('static/movies_data.csv')  # Use CSV storage
    app = MovieApp(storage, api_key)    # Pass it to MovieApp
    app.run()                                  # Run the app

if __name__ == "__main__":
    main()