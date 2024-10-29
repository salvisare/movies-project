# 🎬 Movie Collection App

This Movie Collection App is a Python-based CLI application that allows users to manage a collection of movies with details fetched directly from the OMDb API. Users can add movies to their collection by title, list all stored movies, and delete movies from the collection. The app supports both JSON and CSV storage formats, making it flexible and easy to use.

## 📝 Project Overview

- **Purpose**: The app allows users to store, list, and delete movies with real data sourced from the OMDb API, including details like title, year, rating, and poster image URL.
- **Data Storage**: Users can choose between storing data in JSON (`movies_data.json`) or CSV (`movies_data.csv`) formats, providing versatility in data management.
- **OMDb Integration**: By fetching data from the OMDb API, users get accurate movie information without needing to enter it manually.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.7+
- An OMDb API key, which you can get for free by signing up on the OMDb website: http://www.omdbapi.com/apikey.aspx.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/salvisare/movies-project.git
   cd movies-project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   - Update `main.py` to include your OMDb API key:
     ```python
     api_key = "YOUR_OMDB_API_KEY"
     ```

## 🚀 Usage Guide

### Running the App

Run the following command to start the app:
```bash
python main.py
```

### Commands and Features

1. **Add a Movie**:
   - Enter a movie title, and the app will retrieve its details (title, year, rating, poster URL) from the OMDb API.
   - **Example**:
     ```bash
     Enter movie title: Mad Max
     ```
   - **Error Handling**:
     - If the movie is not found or there’s an API connectivity issue, the app will notify you with an appropriate message.

2. **List All Movies**:
   - Displays all stored movies with their details (title, year, rating, and poster URL).
   
3. **Delete a Movie**:
   - Enter a movie title to delete it from your collection.
   - **Example**:
     ```bash
     Enter the title of the movie to delete: Mad Max
     ```

### Configuration Options

By default, the app uses CSV for data storage. To change storage format:

1. In `main.py`, switch between JSON and CSV storage by changing the relevant line:
   ```python
   storage = StorageCsv('static/movies_data.csv')  # Use CSV data
   # or
   storage = StorageJson('static/movies_data.json')  # Use JSON data
   ```

## 🛡️ Error Handling

The app manages several potential issues gracefully:
- **Movie Not Found**: If a movie is not in OMDb, you’ll receive a notification.
- **API Connection Error**: If there’s an issue connecting to the API (e.g., network error), the app will inform you and allow retrying when connectivity is restored.


## 📚 Additional Information

- **OMDb API Documentation**: For further details about OMDb API and its parameters, see [OMDb API Documentation](http://www.omdbapi.com/).
- **Supported Python Versions**: This app requires Python 3.7 or higher.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! To contribute:

1. Fork the repository.
2. Create a new branch with your feature or improvement.
3. Make your changes and submit a pull request.

## 📝 License

This project is open-source and available under the MIT License.

---