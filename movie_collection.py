import os


def clear_terminal_screen():
    return os.system("clear || cls")


MENU_PROMPT = "\nEnter 'add' to add a movie,\n'list' to show movie list,\n'find' to find a movie by title,\n'clear' to clear the terminal screen,\nor 'quit' to exit the program: "

movies = []

def add_movie():
    clear_terminal_screen()
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter the movie's release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    clear_terminal_screen()
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    clear_terminal_screen()
    print(
        f"Title: {movie['title']}"
        f"\nDirector: {movie['director']}"
        f"\nRelease year: {movie['year']}"
    )


def find_movie():
    clear_terminal_screen()
    search_title = input("Enter movie title that you're looking for: ")

    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)


user_options = {
    'add': add_movie,
    'list': show_movies,
    'find': find_movie,
    'clear': clear_terminal_screen()
}

def menu():
    clear_terminal_screen()
    selection = input(MENU_PROMPT)
    while selection != "quit":
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            clear_terminal_screen()
            print("Unknown command. Try again.")
        
        selection = input(MENU_PROMPT)


menu()