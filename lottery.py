import pathlib, json, csv
import random
import click

from data import *


class Participant:
    def __init__(self, id, first_name, last_name, weight=1):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Prize:
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name}"


class Winner:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def __repr__(self):
        return f"{self.name} - {self.prize}"

    def to_dict(self):
        return {"name": self.name, "prize": self.prize}


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


def extract_file_extension(filename):
    index_dot = filename.rfind(".")
    extension = filename[index_dot+1:]
    return extension


def extract_lottery_scheme(filename):  # TODO obtestować to
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        for prize in lottery_scheme["prizes"]:
            for amount in range(prize["amount"]):
                lottery_prizes_list.append(Prize(**prize))
        return lottery_prizes_list


def draw_winners(participants_list, how_many, prizes, file_output):  # todo weight ogarnąć z choices i while
    if how_many > len(prizes):  # TODO wywalić how many i ustalić na len prizes
        raise ValueError(f"Nie może być więcej zwycięzców ({how_many}) niż mamy nagród ({len(prizes)}), soraski")

    winners_list = random.sample(participants_list, k=how_many)
    winners_with_prizes = []
    winners_with_prizes_to_json = []

    for winner in winners_list:
        index = winners_list.index(winner)
        prize = prizes[index]
        winners_with_prizes.append(Winner(winner, prize))

    print(f"Zwycięska {how_many} to:")
    for winner_prize in winners_with_prizes:
        print(winner_prize)
        winners_with_prizes_to_json.append(winner_prize.to_dict())

    with open(file_output, 'w', encoding='utf-8') as file:  # todo rozbić na 3 funkcje, draw, print, files
        file.write(json.dumps(str(winners_with_prizes_to_json)))


@click.command()
@click.option('--participants', default="data/participants1.json",
              help='Filename with participants, default is data/participants1.json')  # TODO argument pozycyjny
@click.option('--file_extension', default="json",
              help='Extension of the filename with participants, default is json')
@click.option('--scheme', default="data/lottery_templates/item_giveaway.json",
              help='Filename with lottery scheme, default is data/lottery_templates/item_giveaway.json')
@click.option('--how_many_winners', default=3,
              help='Number of expected winners of the lottery')
@click.option('--output', default="data/result.json", help='Output json file, default is data/result.json')
def who_won_lottery(participants, file_extension, scheme, how_many_winners, output):
    click.echo("Witamy w loterii")

    file_content = extract_participants_from_json(participants)

    prizes = extract_lottery_scheme(scheme)

    draw_winners(file_content, how_many_winners, prizes, output)

    result = f"(wylosowano z {participants} z użyciem {scheme} i zapisano do {output})"
    print(result)


if __name__ == "__main__":
    # '''
    file_dir = pathlib.Path("data")
    file_temp = "participants2.csv"
    file_input = f"{file_dir}/{file_temp}"
    file_output = f"{file_dir}/result.json"

    how_many_winners = 3

    # lottery_scheme = "data/lottery_templates/separate_prizes.json"
    lottery_scheme = "data/lottery_templates/item_giveaway.json"

    file_extension = extract_file_extension(file_temp)

    if file_extension == "json":
        file_content = extract_participants_from_json(file_input)
    elif file_extension == "csv":
        file_content = extract_participants_from_csv(file_input)

    print(file_temp, "\n")

    prizes = extract_lottery_scheme(lottery_scheme)

    draw_winners(file_content, how_many_winners, prizes, file_output)
# '''
# start script
#     who_won_lottery()
