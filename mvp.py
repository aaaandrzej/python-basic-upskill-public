import pathlib, json, csv
import random
from data import *


class Participant:
    def __init__(self, id, first_name, last_name, weight=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def open_file(filename, extension):
    if extension == "json":
        with open(filename) as json_opened:
            json_content = json.load(json_opened)
            participants_list_objects = []
            for e in json_content:
                participants_list_objects.append(Participant(**e))

        return participants_list_objects

    elif extension == "csv":
        with open(filename, newline="") as csv_opened:
            csv_content = csv.reader(csv_opened)
            participants_list_objects = []

            for row in csv_content:
                a = Participant(*row)
                participants_list_objects.append(a)
                # próbowałem to zrobić z ** ale wywalało błędy, więc obszedłem to tak o..

            return participants_list_objects[1:]  # pomijamy pierwszy wiersz


def check_file_extension(filename):
    index_dot = filename.rfind(".")
    extension = filename[index_dot+1:]
    return extension


def draw_participants(participants_list, how_many):
    winners_list = random.choices(participants_list, k=how_many)

    print(f"Zwycięska {how_many} to:")
    for winner in winners_list:
        print(winner)


if __name__ == "__main__":
    file_dir = pathlib.Path("data")
    file_temp = "participants2.json"
    file_input = f"{file_dir}/{file_temp}"

    how_many_winners = 4

    file_extension = check_file_extension(file_temp)
    file_content = open_file(file_input, file_extension)

    print(file_temp, "\n")
    draw_participants(file_content, how_many_winners)
