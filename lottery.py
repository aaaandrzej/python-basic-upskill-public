import json, csv
import random
import click


class Participant:  #  TODO wydzielić na 3 pliki po klasach + funkcjach ich dotyczących
    def __init__(self, id, first_name, last_name, weight=1):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Prize:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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


def extract_prizes_from_scheme(filename):  # TODO obtestować to
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        for prize in lottery_scheme["prizes"]:
            for amount in range(prize["amount"]):
                lottery_prizes_list.append(Prize(prize["id"], prize["name"]))
        return lottery_prizes_list


def draw_winners(participants_list, prizes):  # TODO obtestować to, np kiedy nie ma uczestników albo nagród

    participants_list_weights = []

    for winner in participants_list:
        participants_list_weights.append(int(winner.weight))

    winners_list = []

    #  TODO obsłużyć edge case kiedy jest 1 uczestnik a 3 nagrody, lub któregoś 0

    while len(winners_list) < len(prizes):
        winner = random.choices(participants_list, weights=participants_list_weights, k=1)
        if winner[0] not in winners_list:
            winners_list.append(winner[0])

    winners_with_prizes = []

    for prize in prizes:
        index = prizes.index(prize)
        winner = winners_list[index]
        winners_with_prizes.append(Winner(winner, prize))

    return winners_with_prizes


def write_winners_to_json(winners_with_prizes, file_output):
    winners_with_prizes_to_json = []

    for winner_prize in winners_with_prizes:
        winners_with_prizes_to_json.append(winner_prize.to_dict())

    with open(file_output, 'w', encoding='utf-8') as file:
        file.write(json.dumps(str(winners_with_prizes_to_json)))


def print_winners(winners_with_prizes):
    print(f"Zwycięska {len(winners_with_prizes)} to:")
    for winner_prize in winners_with_prizes:
        print(winner_prize)


@click.command()
@click.argument("file_input")
@click.option('--file_extension', default="json",
              help='Extension of the filename with participants, default is json')
@click.option('--scheme', default="data/lottery_templates/item_giveaway.json",
              help='Filename with lottery scheme, default is data/lottery_templates/item_giveaway.json')
@click.option('--file_output', default="data/result.json", help='Output json file, default is data/result.json')
def main(file_input, file_extension, scheme, file_output):
    click.echo("Witamy w loterii")

    if file_extension == "json":
        file_content = extract_participants_from_json(file_input)
    elif file_extension == "csv":
        file_content = extract_participants_from_csv(file_input)

    prizes = extract_prizes_from_scheme(scheme)

    winners_with_prizes = draw_winners(file_content, prizes)

    write_winners_to_json(winners_with_prizes, file_output)

    print_winners(winners_with_prizes)

    summary = f"(wylosowano z {file_input} z użyciem {scheme} i zapisano do {file_output})"

    print(summary)


if __name__ == "__main__":

    main()  # file_input argument required, e.g.: "python lottery.py participants1.json"

'''
# scripts for testing only - commented by default
    file_input="data/participants2.json"
    file_extension="json"
    scheme="data/lottery_templates/item_giveaway.json"
    file_output="data/result.json"

    if file_extension == "json":
        file_content = extract_participants_from_json(file_input)
    elif file_extension == "csv":
        file_content = extract_participants_from_csv(file_input)

    prizes = extract_prizes_from_scheme(scheme)

    winners_with_prizes = draw_winners(file_content, prizes)

    # write_winners_to_json(winners_with_prizes, file_output)
    #
    # print_winners(winners_with_prizes)
    #
    # summary = f"(wylosowano z {file_input} z użyciem {scheme} i zapisano do {file_output})"
    #
    # print(summary)

    print(winners_with_prizes)
'''
