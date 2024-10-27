# test_storage_json.py
from storage_json import StorageJson

# Create an instance of StorageJson with the path to your JSON file
storage = StorageJson('movies_data.json')

# Test listing movies
print("Listing all movies:")
print(storage.list_movies())

# Test adding a new movie
print("\nAdding a new movie:")
storage.add_movie("Inception", 8.8, 2010, "https://example.com/poster/inception.jpg")
print(storage.list_movies())

# Test updating an existing movie's rating
print("\nUpdating movie rating:")
storage.update_movie("Inception", 9.0, 2009)
print(storage.list_movies())

# Test deleting a movie
print("\nDeleting a movie:")
storage.delete_movie("Inception")
print(storage.list_movies())
