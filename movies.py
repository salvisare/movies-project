import random


def exit_program():
    print("Bye!")
    exit()


def list_movies(movies):
    movies_counter = len(movies)
    print(f"\n{movies_counter} movies in total:\n")
    for movie, rating in movies.items():
        print(f"{movie}. {rating}")
    back_to_main_menu(movies)


def back_to_main_menu(movies):
    trigger_back_to_main_menu = input("\nPress enter to continue:\n")
    if trigger_back_to_main_menu == "":
        list_menu(movies)
        apply_user_nav(movies)
    else:
        print("This is an invalid input!")
        back_to_main_menu(movies)


def list_menu(movies):
    menu_list = {
        0: "Exit",
        1: "List movies",
        2: "Add movie",
        3: "Delete movie",
        4: "Update movie",
        5: "Stats",
        6: "Random movie",
        7: "Search movie",
        8: "Movies sorted by rating"
    }
    print("Menu:")
    for menu_no, action in menu_list.items():
        print(f"{menu_no}. {action}")


def add_movie(movies):
    user_enter_movie_name = input("Enter new movie name: ")
    while user_enter_movie_name == "":
        user_enter_movie_name = input("Enter a valid movie name: ")
    user_enter_movie_rating = float(input("Enter new movie rating (0.0-10.0): "))
    while user_enter_movie_rating == "":
        user_enter_movie_rating = float(input("Enter a valid movie rating: "))
    movies[user_enter_movie_name] = user_enter_movie_rating
    print("Thank you! The movie has been successfully added to the database.")
    back_to_main_menu(movies)


def delete_movie(movies):
    movie_to_delete = input("Which movie do you want to delete?")
    while movie_to_delete not in movies:
        movie_to_delete = input("This movie is not in the database. Please try again by typing which movie you want to delete:")
    del movies[movie_to_delete]
    print("Thank you! The movie has been successfully deleted.")
    back_to_main_menu(movies)


def update_movie(movies):
    movie_to_update = input("Enter movie name: ")
    while movie_to_update not in movies:
        movie_to_update = input("This movie is not in the database. Please try again by entering a movie you want to update:")
    enter_new_rating = float(input("Enter movie rating (0.0-10.0): "))
    while enter_new_rating == "":
        enter_new_rating = float(input("Enter a valid movie rating (0.0-10.0): "))
    movies[movie_to_update] = enter_new_rating
    print(f"\nThanks you! The movie {movie_to_update} has been successfully updated.")
    back_to_main_menu(movies)


def show_stats(movies):
    # Get average rating
    total_rating = sum(movies.values())
    calculate_average_rating = total_rating / len(movies)
    print(f"Average rating: {calculate_average_rating}")

    # Get median rating
    rating_list = sorted(movies.values())
    length = len(rating_list)
    if length % 2 == 1:
        median_value = rating_list[length // 2]
    else:
        median_value = (rating_list[length // 2 - 1] + rating_list[length // 2]) * 0.5
    print(f"Median rating: {median_value}")

    # Get the best movie
    sorted_movies = sorted(movies.items(), key=lambda item: item[1])
    best_movie, best_rating = sorted_movies[-1]
    print(f"Best movie: {best_movie}, {best_rating}")

    # Get the worst movie
    worst_movie, worst_rating = sorted_movies[0]
    print(f"Worst movie: {worst_movie}, {worst_rating}")

    back_to_main_menu(movies)


def choose_random_movie(movies):
    movie, rating = random.choice(list(movies.items()))
    print(f"Your random movie is: {movie}, {rating}")
    back_to_main_menu(movies)


def search_movie(movies):
    movie_search = input("Search for a movie: ").strip().lower()
    while movie_search == "":
        movie_search = input("This is not a valid input. Please search for a movie: ").strip().lower()
    for movie, rating in movies.items():
        all_char_movies = movie.lower()
        if movie_search in all_char_movies:
            print(f"As per your search we've found the following movie: {movie} with {rating} rating.")
    back_to_main_menu(movies)


def sort_movies_by_rating(movies):
    print("\nThese are the sorted movies by rating:\n")
    sorted_movies_by_rating = sorted(movies.items(), key=lambda x: x[1], reverse=True)
    for movie_entries, rating in sorted_movies_by_rating:
        print(movie_entries, rating)
    back_to_main_menu(movies)


def apply_user_nav(movies):
    try:
        user_navigation_input = int(input("\nEnter choice (0-8): "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 8.")
        return apply_user_nav(movies)

    if user_navigation_input == 0:
        exit_program()
    elif user_navigation_input == 1:
        list_movies(movies)
    elif user_navigation_input == 2:
        add_movie(movies)
    elif user_navigation_input == 3:
        delete_movie(movies)
    elif user_navigation_input == 4:
        update_movie(movies)
    elif user_navigation_input == 5:
        show_stats(movies)
    elif user_navigation_input == 6:
        choose_random_movie(movies)
    elif user_navigation_input == 7:
        search_movie(movies)
    elif user_navigation_input == 8:
        sort_movies_by_rating(movies)
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
        apply_user_nav(movies)


def main():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

    print("********** My Movies Database **********")
    list_menu(movies)
    apply_user_nav(movies)


if __name__ == "__main__":
    main()
