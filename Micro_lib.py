import csv
from pathlib import Path
import os


class UrkFilms():
    average = 0
    name_file = ''
    def __init__(self, name_file='data.csv'):
        self.name_file = name_file
        path = Path(self.name_file)
        if not path.is_file():
            with open(self.name_file, "w+", encoding="cp1251", newline="") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(("film_title", "rating", "note"))

    def add_film(self, film_title=None, rating=None, note=None):
        with open(self.name_file, "a", encoding="cp1251", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(
                (film_title, rating, note)
            )

    def get_notes(self):
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            for film in films:
                print(film[2])

    def delete_note(self, name):
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            with open('data2.csv', "w", encoding="cp1251", newline="") as new_file:
                writer = csv.writer(new_file, delimiter=';')
                for film in films:
                    if name == film[0]:
                        writer.writerow(
                            (film[0], film[1], '')
                        )
                    else:
                        writer.writerow(
                            (film)
                        )
        os.remove(self.name_file)
        os.rename('data2.csv', self.name_file)

    def add_note(self, name, note):
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            with open('data2.csv', "w", encoding="cp1251", newline="") as new_file:
                writer = csv.writer(new_file, delimiter=';')
                for film in films:
                    if name == film[0]:
                        writer.writerow(
                            (film[0], film[1], note)
                        )
                    else:
                        writer.writerow(
                            (film)
                        )
        os.remove(self.name_file)
        os.rename('data2.csv', self.name_file)

    def highest_rating_films(self):
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            for film in films:
                if film[1] != "rating" and float(film[1]) >= 4:
                    print("Film with the highest rating: ", film)


    def lowest_rating_films(self):
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            for film in films:
                if film[1] != "rating" and float(film[1]) <= 2:
                    print("Film with the lowest rating: ", film)


    def avarage_rating(self):
        value = []
        with open(self.name_file, "r", encoding="cp1251") as file:
            films = csv.reader(file, delimiter=';')
            for film in films:
                if film[1] != "rating":
                    value.append(float(film[1]))
                    self.average = sum(value) / len(value)
        print("Average rating among all films: ", self.average)




# user_data = [
#     ["Битва за Севастополь", "7.4", "военный, мелодрама, боевик"],
#     ["Вий 3D", "5.8", "приключения, триллер, фэнтези"],
#     ["Захар Беркут", "5.9", "Художественный"],
#     ["Донбасс", "6.6", "Украина"],
# ]
# films = UrkFilms()
# films.add_film(film_title="Битва за Севастополь", rating=4.1, note="военный, мелодрама, боевик")
# films.add_film(film_title="Вий 3D", rating=3.9, note="приключения, триллер, фэнтези")
# films.add_film(film_title="Захар Беркут", rating=4.9, note="Художественный")
# films.add_film(film_title="Донбасс", rating=1.1, note="Украина")
# films.get_notes()
# films.delete_note('Битва за Севастополь')
# films.add_note('Захар Беркут', 'УкраинаУкраинаУкраина')
# films.lowest_rating_films()
# films.highest_rating_films()
# films.avarage_rating()
