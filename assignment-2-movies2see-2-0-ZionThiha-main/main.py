"""
Name: Aung Thiha
Date: 21/4/2024
Brief Project Description: Assignment 2
GitHub URL: https://github.com/ZionThiha/CP1404practical
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from movie import Movie
from moviecollection import MovieCollection

class Movies2SeeApp(App):
    def build(self):
        self.title = 'Movies 2 See'
        self.movie_collection = MovieCollection()
        self.load_movies()

        # Root layout
        root = BoxLayout(orientation='horizontal')

        # Left side layout
        left_panel = BoxLayout(orientation='vertical', size_hint_x=0.4)

        # Spinner for sorting movies
        self.spinner = Spinner(
            text='Sort by...',
            values=('Title', 'Year'),
            size_hint_y=None,
            height=50
        )
        self.spinner.bind(text=self.on_spinner_select)

        # Text inputs for new movie
        self.title_input = TextInput(hint_text='Title', size_hint_y=None, height=50)
        self.year_input = TextInput(hint_text='Year', size_hint_y=None, height=50)
        add_button = Button(text='Add Movie', size_hint_y=None, height=50)
        add_button.bind(on_press=self.add_new_movie)

        # Adding widgets to left panel
        left_panel.add_widget(self.spinner)
        left_panel.add_widget(self.title_input)
        left_panel.add_widget(self.year_input)
        left_panel.add_widget(add_button)

        # Right side layout
        right_panel = BoxLayout(orientation='vertical', size_hint_x=0.6)

        # Status label at the top
        self.status_label_top = Label(size_hint_y=None, height=50)

        # Movie list display using ScrollView and GridLayout
        self.movie_grid = GridLayout(cols=1, size_hint_y=None)
        self.movie_grid.bind(minimum_height=self.movie_grid.setter('height'))
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 500))
        scroll_view.add_widget(self.movie_grid)

        # Status label at the bottom
        self.status_label_bottom = Label(size_hint_y=None, height=50, text='Ready')

        # Adding widgets to right panel
        right_panel.add_widget(self.status_label_top)
        right_panel.add_widget(scroll_view)
        right_panel.add_widget(self.status_label_bottom)

        # Adding left and right panels to the root layout
        root.add_widget(left_panel)
        root.add_widget(right_panel)

        self.update_movie_list()
        self.update_status_label_top()

        return root

    def update_movie_list(self):
        self.movie_grid.clear_widgets()
        for movie in self.movie_collection.movies:
            btn = Button(
                text=f"{movie.title} ({movie.year})",
                background_color=('green' if movie.watched else 'red'),
                size_hint_y=None,
                height=40
            )
            btn.bind(on_press=lambda btn, m=movie: self.toggle_movie_watched(m))
            self.movie_grid.add_widget(btn)

    def toggle_movie_watched(self, movie):
        movie.watched = not movie.watched
        self.update_movie_list()
        self.update_status_label_top()

    def on_spinner_select(self, spinner, text):
        self.movie_collection.sort(key=text.lower())
        self.update_movie_list()

    def add_new_movie(self, instance):
        title = self.title_input.text
        year = self.year_input.text
        if title and year.isdigit():
            new_movie = Movie(title, int(year))
            self.movie_collection.add_movie(new_movie)
            self.update_movie_list()
            self.update_status_label_top()
            self.status_label_bottom.text = f"Added movie: {title}"

    def update_status_label_top(self):
        watched = self.movie_collection.get_number_of_watched_movies()
        unwatched = self.movie_collection.get_number_of_unwatched_movies()
        self.status_label_top.text = f"Watched: {watched} | Unwatched: {unwatched}"

    def load_movies(self):
        self.movie_collection.load_movies('movies.json')

    def save_movies(self):
        self.movie_collection.save_movies('movies.json')

    def on_stop(self):
        self.save_movies()

if __name__ == '__main__':
    Movies2SeeApp().run()