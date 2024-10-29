import requests


def get_movie_details(title, api_key):
    """Fetch movie details from the OMDb API by title."""
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx, 5xx)

        movie_data = response.json()

        if movie_data.get('Response') == 'True':
            return movie_data
        else:
            print(f"Movie not found: {title}")
            return None  # Explicitly return None if movie is not found

    except requests.exceptions.RequestException as e:
        # Handle network or other request-related errors
        print(f"Error connecting to OMDb API: {e}")
        return None  # Return None to indicate a failure in fetching movie data


# Usage example:
api_key = "23cc239c"  # Replace with your actual OMDb API key
movie_title = "Titanic"
movie_details = get_movie_details(movie_title, api_key)

if movie_details:
    print(movie_details)
