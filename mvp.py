import pathlib, json, csv
import random
from data import *


def open_file(filename, extension):
    if extension == "json":
        with open(filename) as json_opened:
            json_content = json.load(json_opened)
        return json_content
    elif extension == "csv":
        with open(filename) as csv_opened:
            csv_header = csv_opened.readlines(1)
            csv_body = csv_opened.readlines()
            csv_list = []
            for e in csv_body:
                line = str(str.split(e))
                # line = str(line)
                line_clean = line.replace("[","")
                line_clean = line_clean.replace("]","")
                line_clean = line_clean.replace("'","")
                # print(line_clean)
                # print(type(line))
                # tupplee = tuple(line_clean)
                # print(tupplee)
                csv_list.append(line_clean)
            return csv_list


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

    print(f"Zwycięska {how_many} to:")
    for g in json_content:
        if int(g["id"]) in winners_ids:
            winner_name = g["first_name"]
            winner_surname = g["last_name"]
            winner = f"{winner_name} {winner_surname}"
            print(winner)


def draw_participants_csv(csv_content, how_many):
    # poszukać czegoś specjalnie do csv bo na bank jest...
    participants_range = 0
    for e in csv_content:
        first_coma_index = e.find(",")
        participant_id = int(e[:first_coma_index])
        if participant_id > participants_range:
            participants_range = participant_id

    winners_ids = random.sample(range(1, participants_range), how_many)
    # print(winners_ids)

    print(f"Zwycięska {how_many} to:")
    for g in csv_content:
        first_coma_index = g.find(",")
        participant_id = int(g[:first_coma_index])
        if participant_id in winners_ids:
            winner = g[first_coma_index+1:]
            winner_no_coma = winner.replace(",", " ")
            print(winner_no_coma)


if __name__ == "__main__":
    file_dir = pathlib.Path("data")
    file_temp = "participants1.json"
    file_input = f"{file_dir}/{file_temp}"

    file_extension = check_file_extension(file_temp)
    file_content = open_file(file_input, file_extension)

    # print(file_content)
    # print(check_file_extension(file_input))

    if file_extension == "json":
        print(file_temp, "\n")
        draw_participants_json(file_content, 4)

    if file_extension == "csv":
        print(file_temp, "\n")
        draw_participants_csv(file_content, 4)
