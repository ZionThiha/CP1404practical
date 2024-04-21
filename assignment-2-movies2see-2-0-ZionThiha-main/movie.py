class Movie:
    """
    A class representing a movie with a title, release year, and watch status.
    """
    def __init__(self, title, year):
        """
        Initializes a new Movie instance.

        :param title: str, the title of the movie
        :param year: int, the release year of the movie
        """
        self.title = title
        self.year = year
        self.watched = False

    def __str__(self):
        """
        Returns a string representation of the Movie instance.
        """
        return f"{self.title} ({self.year}) - {'Watched' if self.watched else 'Not Watched'}"

    def mark_as_watched(self):

        self.watched = True

    def mark_as_unwatched(self):

        self.watched = False
