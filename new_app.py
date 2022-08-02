import Micro_lib

MENU_IO = """
Please choose one of these option:
1)Add film
2)Get all notes
3)Delete note in film
4)Add note in film
5)Get films with the lowest rating
6)Get films with the highest rating
7)Get average rating among all films
8)Exit

Your selection:
"""


def menu():
    films = Micro_lib.UrkFilms()

    while (user_input :=input(MENU_IO))!='8':
        if user_input == "1":
            title = input("Enter title: ")
            rating = float(input("Enter rating (1-5): "))
            note = input("Enter note: ")
            films.add_film(film_title=title, rating=rating, note=note)

        elif user_input == "2":
            films.get_notes()

        elif user_input == "3":
            name = input("Enter name: ")
            films.delete_note(name)

        elif user_input == "4":
            name = input("Enter name: ")
            note = input("Enter note: ")
            films.add_note(name, note)
        elif user_input == "5":
            films.lowest_rating_films()
        elif user_input == "6":
            films.highest_rating_films()
        elif user_input == "7":
            films.avarage_rating()
        else:
            print("Invalid input, please try again!")

menu()
# user_data = [
#     ["Битва за Севастополь", "4.9", "военный, мелодрама, боевик"],
#     ["Вий 3D", "3.1", "приключения, триллер, фэнтези"],
#     ["Захар Беркут", "4.1", "Художественный"],
#     ["Донбасс", "1.6", "Украина"],
# ]