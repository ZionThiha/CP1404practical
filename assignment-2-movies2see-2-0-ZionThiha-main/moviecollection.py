import json
from movie import Movie

class MovieCollection:
    """
    A class representing a collection of movies.
    """
    def __init__(self):
        """
        Initializes a new MovieCollection instance.
        """
        self.movies = []

    def add_movie(self, movie):
        """
        Adds a single Movie object to the collection.
        
        :param movie: Movie, the Movie object to add
        """
        if isinstance(movie, Movie):
            self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
        """
        Returns the number of unwatched movies in the collection.
        """
        return sum(1 for movie in self.movies if not movie.watched)

    def get_number_of_watched_movies(self):
        """
        Returns the number of watched movies in the collection.
        """
        return sum(1 for movie in self.movies if movie.watched)

    def load_movies(self, file_path):
        """
        Loads movies from a JSON file into the movie list.
        
        :param file_path: str, path to the JSON file containing movie data
        """
        with open(file_path, 'r') as file:
            movies_json = json.load(file)
            for movie_data in movies_json:
                self.movies.append(Movie(movie_data['title'], movie_data['year']))

    def save_movies(self, file_path):
        """
        Saves the movie list into a JSON file.
        
        :param file_path: str, path to save the JSON file
        """
        with open(file_path, 'w') as file:
            json.dump([{'title': movie.title, 'year': movie.year} for movie in self.movies], file, indent=4)

    def sort(self, key):
        """
        Sorts the movies in the collection by the specified key, then by title.
        
        :param key: str, the key to sort the movies by (e.g., 'title' or 'year')
        """
        self.movies.sort(key=lambda movie: (getattr(movie, key), movie.title))