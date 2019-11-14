import pathlib, json, csv
from data import *

file_dir = pathlib.Path("data")
file_temp = "participants1.csv"
file_input = f"{file_dir}/{file_temp}"


def open_file(filename):
    with open(file_input) as file_opened:
        file_content = file_opened.read()
    return file_content


def check_file_extension(filename):
    pass


def draw_participants(filename, how_many):
    pass


def enumerate_participants(file_content):
    # participant = "1, Dffg, Fsde"
    # print(file_content)
    for number, first_name, last_name in file_content:
        print(first_name, first_name, "dfgf", last_name)


if __name__ == "__main__":
    file_content = open_file(file_input)
    # print(open_file(1))
    enumerate_participants(file_content)