import json
import csv


class Participant:
    def __init__(self, id, first_name, last_name, weight=1):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def extract_participants_from_json(filename):
    with open(filename) as json_opened:
        json_content = json.load(json_opened)
        participants_list_objects = []
        for e in json_content:
            participants_list_objects.append(Participant(**e))

    return participants_list_objects


def extract_participants_from_csv(filename):
    with open(filename, newline="") as csv_opened:
        csv_content = csv.reader(csv_opened)
        participants_list_objects = []

        for row in csv_content:
            a = Participant(*row)
            participants_list_objects.append(a)

        return participants_list_objects[1:]
