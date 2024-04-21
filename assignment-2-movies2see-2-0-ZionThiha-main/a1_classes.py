import csv

MOVIES_FILE = "movies.csv"
WATCHED = "w"
UNWATCHED = "u"

print("Movies2See 1.0 - by Aung Thiha")


def load_movies():
    movies = []
    with open(MOVIES_FILE, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies


def save_movies(movies):
    with open(MOVIES_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)


def movie_sort_key(movie):
    return movie[2], movie[0]


def display_movies(movies):
    print("Movies:")
    sorted_movies = sorted(movies, key=movie_sort_key)
    for index, movie in enumerate(sorted_movies):
        status = "*" if movie[3] == UNWATCHED else ""
        print(f"{index + 1}. {movie[0]}, {movie[2]}, {movie[1]} {status}")
    unwatched_count = sum(1 for movie in movies if movie[3] == UNWATCHED)
    print(f"\n{unwatched_count} movies to watch.")


def add_movie(movies):
    title = input("Enter movie title: ")
    year = input("Enter movie year: ")
    category = input("Enter movie category: ")
    movies.append([title, category, year, UNWATCHED])
    print("Movie added successfully.")


def watch_movie(movies):
    unwatched_movies = [index + 1 for index, movie in enumerate(movies) if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    print("Choose a movie to mark as watched:")
    for index in unwatched_movies:
        print(f"{index}. {movies[index - 1][0]}")
    choice = int(input("Enter your choice: "))
    if choice in unwatched_movies:
        movies[choice - 1][3] = WATCHED
        print(f"{movies[choice - 1][0]} marked as watched.")
    else:
        print("Invalid choice.")


def main():
    print("Welcome to Movie List Program by [Your Name]!")
    movies = load_movies()

    while True:
        print("\nMenu:")
        print("1. List movies")
        print("2. Add movie")
        print("3. Mark movie as watched")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            watch_movie(movies)
        elif choice == "4":
            save_movies(movies)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


main()
