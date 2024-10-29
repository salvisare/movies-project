from storage.storage_csv import StorageCsv
from movie_app import MovieApp


def main():
    api_key = "23cc239c"
    storage = StorageCsv('data/movies_data.csv')  # Use CSV data
    app = MovieApp(storage, api_key)    # Pass it to MovieApp
    app.run()                                  # Run the app

if __name__ == "__main__":
    main()