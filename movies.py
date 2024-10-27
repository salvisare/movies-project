import sys
import random
import movie_storage


MIN_RATING = 0
MAX_RATING = 10

def exit_program():
    """Exits the program"""
    print("Bye!")
    sys.exit()  # Explicitly exits the program


def list_movies():
    """Lists all the movies"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    movies_counter = len(movies)
    print(f"\n{movies_counter} movies in total:\n")
    counter = 1
    for movie, details in movies.items():
        print(f"{counter}. {movie}. Rating: {details['rating']}. Release year: {details['year']}")
        counter += 1
    back_to_main_menu()


def back_to_main_menu():
    """Navigates the user back to the main menu options"""

    trigger_back_to_main_menu = input("\nPress enter to continue:\n")
    if trigger_back_to_main_menu == "":
        list_menu()
        apply_user_nav()
    else:
        print("This is an invalid input!")
        back_to_main_menu()


def list_menu():
    """Offers the user menu options list"""
    menu_list = {
        1: "List movies",
        2: "Add movie",
        3: "Delete movie",
        4: "Update movie",
        5: "Stats",
        6: "Random movie",
        7: "Search movie",
        8: "Movies sorted by rating",
        9: "Movies sorted by year",
        0: "Exit program"
    }
    print("Menu:")
    for menu_no, action in menu_list.items():
        print(f"{menu_no}. {action}")


def add_movie():
    """Adding a movie, checking validation"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    user_enter_movie_name = input("Enter new movie name: ")
    while user_enter_movie_name == "":
        user_enter_movie_name = input("Enter a valid movie name: ")

    user_enter_movie_rating = input("Enter movie rating (0.0-10.0): ")
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

    user_enter_movie_year = input("Enter the year of release: ")
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

    movies[user_enter_movie_name] = {
        "rating": user_enter_movie_rating,
        "year": user_enter_movie_year
    }

    # Add the movie and save the data to the JSON file
    movie_storage.add_movie(user_enter_movie_name, user_enter_movie_rating, user_enter_movie_year)

    print("Thank you, the movie has been added!")
    back_to_main_menu()


def delete_movie():
    """Deleting a movie"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    movie_to_delete = input("Which movie do you want to delete?")
    while movie_to_delete not in movies:
        movie_to_delete = input("Movie not in database. Try again by typing which movie you want to delete:")
    movie_storage.delete_movie(movie_to_delete)
    print(f"Thank you! The movie '{movie_to_delete}' has been successfully deleted.")
    back_to_main_menu()


def update_movie():
    """Updating a movie"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    movie_to_update = input("Enter movie name: ")
    while movie_to_update not in movies:
        movie_to_update = input("Movie not in database. Try again by typing which movie you want to update:")

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

    movies[movie_to_update] = {
        "rating": user_enter_movie_rating,
        "year": user_enter_movie_year
    }

    movie_storage.update_movie(movie_to_update, user_enter_movie_rating, user_enter_movie_year)

    print(f"\nThank you, the movie '{movie_to_update}' has been updated!")
    back_to_main_menu()


def show_stats():
    """Showing movies statistics"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    # Get average rating
    total_rating = 0
    for titles, details in movies.items():
        total_rating += details["rating"]
    calculate_average_rating = round(total_rating / len(movies), 2)
    print(f"Average rating: {calculate_average_rating}")

    # Get median rating
    rating_list = []
    for titles, details in movies.items():
        rating_list.append(details["rating"])

    length = len(rating_list)
    if length % 2 == 1:
        median_value = rating_list[length // 2]
    else:
        median_value = (rating_list[length // 2 - 1] + rating_list[length // 2]) * 0.5
    print(f"Median rating: {median_value}")

    # Get the best movie
    best_rating = MIN_RATING
    best_movie = None
    for title, details in movies.items():
        if details["rating"] > best_rating:
            best_movie = title
            best_rating = details["rating"]
    print(f"Best movie: {best_movie}, {best_rating}")

    # Get the worst movie
    worst_rating = MAX_RATING
    worst_movie = None
    for title, details in movies.items():
        if details["rating"] < worst_rating:
            worst_movie = title
            worst_rating = details["rating"]
    print(f"Worst movie: {worst_movie}, {worst_rating}")

    back_to_main_menu()


def choose_random_movie():
    """Choosing and offering user a random movie"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    random_title = random.choice(list(movies.keys()))
    random_movie = movies[random_title]
    print(f"Random movie: '{random_title}', {random_movie['rating']} rating. Released: {random_movie['year']}.")
    back_to_main_menu()


def search_movie():
    """Allowing the user to search for a movie"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    movie_search = input("Search for a movie: ").strip().lower()
    while movie_search == "":
        movie_search = input("Not a valid input. Please search for a movie: ").strip().lower()
    for title, details in movies.items():
        all_char_movies = title.lower()
        if movie_search in all_char_movies:
            print(f"We've found: '{title}', rating of {details['rating']}. Released: {details['year']}.")
    back_to_main_menu()


def sort_movies_by_rating():
    """Sorting movies by rating"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    print("\nThese are the sorted movies by rating:\n")
    sorted_movies_by_rating = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for title, details in sorted_movies_by_rating:
        print(f"{title}: Rating {details['rating']}, Year {details['year']}")
    back_to_main_menu()


def sort_movies_by_year():
    """Sorting movies by year [a] by the latest, and [b] by the oldest"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    user_sort_by = input("Do you want the latest movies first? (Y/N): ").lower()
    while user_sort_by not in ["y", "n"]:
        user_sort_by = input("Please enter 'Y' for yes or 'N' for no: ").lower()

    if user_sort_by == "y":
        print("Sorted by latest movies first:")
        sorted_movies_by_year = sorted(movies.items(), key=lambda x: x[1]["year"], reverse=True)
        for title, details in sorted_movies_by_year:
            print(f"{title}: Rating {details['rating']}, Year {details['year']}")

    elif user_sort_by == "n":
        print("Sorted by oldest movies first:")
        sorted_movies_by_year = sorted(movies.items(), key=lambda x: x[1]["year"])
        for title, details in sorted_movies_by_year:
            print(f"{title}: Rating {details['rating']}, Year {details['year']}")

    back_to_main_menu()


def apply_user_nav():
    """Applying user navigation selection and directing the action to the appropriate function"""

    # Get the data from the JSON file
    movies = movie_storage.get_movies()

    try:
        user_navigation_input = int(input("\nEnter choice (0-8): "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 8.")
        return apply_user_nav()

    if user_navigation_input == 0:
        exit_program()
    elif user_navigation_input == 1:
        list_movies()
    elif user_navigation_input == 2:
        add_movie()
    elif user_navigation_input == 3:
        delete_movie()
    elif user_navigation_input == 4:
        update_movie()
    elif user_navigation_input == 5:
        show_stats()
    elif user_navigation_input == 6:
        choose_random_movie()
    elif user_navigation_input == 7:
        search_movie()
    elif user_navigation_input == 8:
        sort_movies_by_rating()
    elif user_navigation_input == 9:
        sort_movies_by_year()
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
        apply_user_nav()


def main():
    """Storing original movies list & trigger to the menu function & applying the user selection"""
    # movies = {
    #     "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
    #     "Pulp Fiction": {"rating": 8.8, "year": 1994},
    #     "The Room": {"rating": 3.6, "year": 2003},
    #     "The Godfather": {"rating": 9.2, "year": 1972},
    #     "The Godfather: Part II": {"rating": 9.0, "year": 1974},
    #     "The Dark Knight": {"rating": 9.0, "year": 2008},
    #     "12 Angry Men": {"rating": 8.9, "year": 1957},
    #     "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
    #     "Forrest Gump": {"rating": 8.8, "year": 1994},
    #     "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
    # }

    print("********** My Movies Database **********")
    try:
        while True:  # This loop will continue until you choose to exit
            list_menu()
            apply_user_nav()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")


if __name__ == "__main__":
    main()
