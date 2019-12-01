import pathlib, json, csv
import random
from data import *

file_dir = pathlib.Path("data")
file_temp = "participants1.json"
file_input = f"{file_dir}/{file_temp}"


def open_file(filename, extension="json"):
    if extension == "json":
        with open(filename) as file_opened:
            file_content = json.load(file_opened)
        return file_content


def check_file_extension(filename):
    index_dot = filename.rfind(".")
    extension = filename[index_dot+1:]
    return extension


def draw_participants_json(json_content, how_many):
    participants_range = 0
    for e in json_content:
        if int(e["id"]) > participants_range:
            participants_range = int(e["id"])
    winners_ids = random.sample(range(1, participants_range), how_many)

    print(f"Zwycięzka {how_many} to:")
    for g in json_content:
        if int(g["id"]) in winners_ids:
            winner_name = g["first_name"]
            winner_surname = g["last_name"]
            winner = f"{winner_name} {winner_surname}"
            print(winner)


def draw_participants_csv(csv_content, how_many):
    pass



if __name__ == "__main__":
    file_content = open_file(file_input)
    # print(file_content)
    # print(check_file_extension(file_input))
    draw_participants_json(file_content, 3)