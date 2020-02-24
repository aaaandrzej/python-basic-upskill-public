import json


class Prize:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.name}"


def extract_prizes_from_scheme(filename):  # TODO obtestować to
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        for prize in lottery_scheme["prizes"]:
            for amount in range(prize["amount"]):
                lottery_prizes_list.append(Prize(prize["id"], prize["name"]))
        return lottery_prizes_list
