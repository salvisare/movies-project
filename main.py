from storage_json import StorageJson
from storage_csv import StorageCsv
from movie_app import MovieApp

def main():
    #storage = StorageJson('static/movies_data.json')  # Create a StorageJson instance
    storage = StorageCsv('static/movies_data.csv')  # Use CSV storage
    app = MovieApp(storage)                    # Pass it to MovieApp
    app.run()                                  # Run the app

if __name__ == "__main__":
    main()