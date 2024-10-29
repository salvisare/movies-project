import random
import sys
from omdb_api import get_movie_details


class MovieApp:
    """Main class for the movie application to handle menu, commands, and logic."""
    def __init__(self, storage, api_key):
        """Initialize the movie app with a storage instance."""
        self._storage = storage
        self.api_key = api_key


    def _command_list_movies(self):
        """List all movies stored in the database."""
        movies = self._storage.list_movies()
        movies_counter = len(movies)
        print(f"\n{movies_counter} movies in total:\n")
        counter = 1
        for movie, details in movies.items():
            print(f"{counter}. {movie}. Rating: {details['rating']}. Release year: {details['year']}. Poster: {details['poster']}")
            counter += 1

        self.back_to_main_menu()


    def _command_movie_stats(self):
        """Display statistics about the movies in the database."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in the database.")
            return

        # Average rating
        ratings = [details["rating"] for details in movies.values()]
        avg_rating = sum(ratings) / len(ratings)

        # Median rating
        rating_list = []
        for titles, details in movies.items():
            rating_list.append(details["rating"])
        length = len(rating_list)
        if length % 2 == 1:
            median_rating = rating_list[length // 2]
        else:
            median_rating = (rating_list[length // 2 - 1] + rating_list[length // 2]) * 0.5

        # Highest and lowest rated movies
        highest_rated = max(movies, key=lambda x: movies[x]["rating"])
        lowest_rated = min(movies, key=lambda x: movies[x]["rating"])

        print(f"\nMovie Statistics:")
        print(f"Average Rating: {avg_rating:.2f}")
        print(f"Median Rating: {median_rating:.2f}")
        print(f"Highest Rated Movie: {highest_rated} - {movies[highest_rated]['rating']}")
        print(f"Lowest Rated Movie: {lowest_rated} - {movies[lowest_rated]['rating']}")

        self.back_to_main_menu()


    def _command_add_movie(self):
        """Add a new movie by title and fetch details from OMDb API."""
        title = input("Enter movie title: ").strip()

        # Fetch movie data using OMDb API
        movie_data = get_movie_details(title, self.api_key)

        if movie_data:
            # Retrieve relevant details
            title = movie_data.get('Title')
            rating = float(movie_data.get('imdbRating', 0))
            year = int(movie_data.get('Year', 0))
            poster = movie_data.get('Poster', '')

            # Save movie details in storage
            self._storage.add_movie(title, rating, year, poster)
            print(f"Movie '{title}' added successfully!")
        else:
            print(f"Could not add movie: '{title}'. It may not be found in the OMDb database or there was an API issue.")

        self.back_to_main_menu()


    def _command_delete_movie(self):
        """Delete a movie from the database."""
        title = input("Enter the title of the movie to delete: ")

        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully.")

        self.back_to_main_menu()


    def _command_update_movie(self):
        """Update an existing movie with the rating or year"""
        movies = self._storage.list_movies()

        # Get movie by name
        movie_to_update = input("Enter movie name: ")
        while movie_to_update not in movies:
            movie_to_update = input("Movie not in database. Try again by typing which movie you want to update:")

        # Movie rating
        user_enter_movie_rating = input("Enter the updated movie rating (0.0-10.0): ")
        # Check if the rating is valid
        valid_rating = False
        while not valid_rating:
            try:
                user_enter_movie_rating = float(user_enter_movie_rating)
                if 0.0 <= user_enter_movie_rating <= 10.0:
                    valid_rating = True
                else:
                    user_enter_movie_rating = input("Rating must be between 0.0 and 10.0. Try again: ")
            except ValueError:
                user_enter_movie_rating = input("Enter a valid movie rating (0.0-10.0): ")

        # Movie year
        user_enter_movie_year = input("Enter the updated year of release: ")
        # Check if the year is valid
        valid_year = False
        while not valid_year:
            if user_enter_movie_year.isdigit():  # Check if the year is a number
                user_enter_movie_year = int(user_enter_movie_year)
                if user_enter_movie_year >= 1900:
                    valid_year = True
                else:
                    user_enter_movie_year = input("Year must be 1900 or later. ")
            else:
                user_enter_movie_year = input("Enter a valid year (after 1900): ")

        # Update poster URL
        user_enter_poster_url = input("Enter URL for movie poster: ")

        movies[movie_to_update] = {
            "rating": user_enter_movie_rating,
            "year": user_enter_movie_year,
            "poster": user_enter_poster_url
        }

        self._storage.update_movie(movie_to_update, user_enter_movie_rating, user_enter_movie_year, user_enter_poster_url)
        print(f"Movie '{movie_to_update}' updated successfully.")

        self.back_to_main_menu()


    def _command_choose_random_movie(self):
        """Choosing and offering user a random movie"""
        movies = self._storage.list_movies()

        random_title = random.choice(list(movies.keys()))
        random_movie = movies[random_title]
        print(f"Random movie: '{random_title}', {random_movie['rating']} rating. Released: {random_movie['year']}.")

        self.back_to_main_menu()


    def _command_search_movie(self):
        """Allowing the user to search for a movie"""
        movies = self._storage.list_movies()

        while True:
            movie_search = input("Search for a movie: ").strip().lower()

            # Ensure the input is not empty
            while not movie_search:
                movie_search = input("Not a valid input. Please search for a movie: ").strip().lower()

            # Flag to track if any movies were found
            found_any_movie = False

            # Search through the movies
            for title, details in movies.items():
                if movie_search in title.lower():
                    print(f"We've found: '{title}', rating: {details['rating']}, Released: {details['year']}.")
                    found_any_movie = True  # Set flag to True if a match is found
                    break  # Exit the search loop if a match is found

            # If a movie was found, exit to main menu
            if found_any_movie:
                break

            # Notify the user if no movies were found
            print(
                f"No movies found for '{movie_search}'. Try again.")

        self.back_to_main_menu()


    def _command_sort_movies_by_rating(self):
        """Sorting movies by rating"""
        movies = self._storage.list_movies()

        print("\nThese are the sorted movies by rating:\n")
        sorted_movies_by_rating = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
        for title, details in sorted_movies_by_rating:
            print(f"Rating: {details['rating']} | Movie: {title} | Year: {details['year']}")

        self.back_to_main_menu()


    def _command_sort_movies_by_year(self):
        """Sorting movies by year"""
        movies = self._storage.list_movies()

        user_sort_by = input("Do you want the latest movies first? (Y/N): ").lower()
        while user_sort_by not in ["y", "n"]:
            user_sort_by = input("Please enter 'Y' for yes or 'N' for no: ").lower()

        if user_sort_by == "y":
            print("Sorted by latest movies first:")
            sorted_movies_by_year = sorted(movies.items(), key=lambda x: x[1]["year"], reverse=True)
            for title, details in sorted_movies_by_year:
                print(f"Year: {details['year']} | Movie: {title} | Rating: {details['rating']}")

        elif user_sort_by == "n":
            print("Sorted by oldest movies first:")
            sorted_movies_by_year = sorted(movies.items(), key=lambda x: x[1]["year"])
            for title, details in sorted_movies_by_year:
                print(f"Year: {details['year']} | Movie: {title} | Rating: {details['rating']}")

        self.back_to_main_menu()


    def _command_generate_website(self):
        """Generate a static website showcasing the movies."""
        movies = self._storage.list_movies()
        html_content = "<html><head><title>The Ultimate Movie Collection</title></head><body>"
        html_content += "<h1>The Ultimate Movie Collection</h1><ul>"
        for title, details in movies.items():
            html_content += (
                f"<li><strong>{title}</strong> - Rating: {details['rating']} - "
                f"Year: {details['year']}<br><img src='{details.get('poster', '')}' width='100'></li>"
            )
        html_content += "</ul></body></html>"

        with open("static/movies.html", "w") as f:
            f.write(html_content)
        print("Website generated as 'movies.html' within the 'static' directory.")

        self.back_to_main_menu()


    def back_to_main_menu(self):
        """Navigates the user back to the main menu options"""
        while True:
            trigger_back_to_main_menu = input("\nPress Enter to continue:\n")
            if trigger_back_to_main_menu == "":
                break
            else:
                print("Invalid input! Please press Enter to return to the main menu.")

    def exit_program(self):
        """Exits the program"""
        print("Bye!")
        sys.exit()  # Explicitly exits the program


    def run(self):
        """Main menu to handle user commands and execute the selected option."""
        while True:
            print("\n--- Movie App Menu ---")
            print("1. List all movies")
            print("2. Add movie")
            print("3. Delete a movie")
            print("4. Update movie")
            print("5. Show movie statistics")
            print("6. Choose a random movie")
            print("7. Search for a movie")
            print("8. Sort movies by rating")
            print("9. Sort movies by year")
            print("10. Generate website")
            print("0. Exit\n")

            choice = input("Enter choice (0-10): ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                self._command_choose_random_movie()
            elif choice == "7":
                self._command_search_movie()
            elif choice == "8":
                self._command_sort_movies_by_rating()
            elif choice == "9":
                self._command_sort_movies_by_year()
            elif choice == "10":
                self._command_generate_website()
            elif choice == "0":
                self.exit_program()
            else:
                print("Invalid choice. Please select a valid option.")
