from mvp import *
import json
import click


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


def extract_lottery_scheme(filename):
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        for prize in lottery_scheme["prizes"]:
            for amount in range(prize["amount"]):
                lottery_prizes_list.append(Prize(**prize))
        return lottery_prizes_list


def draw_participants(participants_list, how_many, prizes, file_output):
    winners_list = random.sample(participants_list, k=how_many)
    winners_with_prizes = []
    winners_with_prizes_to_json = []

    for winner in winners_list:
        try:
            indexxx = winners_list.index(winner)
            prize = prizes[indexxx]
        except IndexError:
            prize = "Audience Prize" # todo ma być tyle zwycięzców co nagród i koniec, bez aidience prize
        winners_with_prizes.append(Winner(winner, prize))

    print(f"Zwycięska {how_many} to:")
    for winner_prize in winners_with_prizes:
        print(winner_prize)
        winners_with_prizes_to_json.append(winner_prize.to_dict())

    with open(file_output, 'w', encoding='utf-8') as file:
        file.write(json.dumps(str(winners_with_prizes_to_json)))


@click.command()
@click.option('--participants', default="data/participants1.json",
              help='Filename with participants, default is data/participants1.json')
@click.option('--scheme', default="data/lottery_templates/item_giveaway.json",
              help='Filename with lottery scheme, default is data/lottery_templates/item_giveaway.json')
@click.option('--output', default="data/result.json", help='Output json file, default is data/result.json')
def who_won_lottery(participants, scheme, output):
    click.echo("Witamy w loterii")

    how_many_winners = 11

    file_extension = check_file_extension(participants)
    file_content = open_file(participants, file_extension)

    prizes = extract_lottery_scheme(scheme)

    draw_participants(file_content, how_many_winners, prizes, output)

    result = f"(wylosowano z {participants} z użyciem {scheme} i zapisano do {output})"
    print(result)


if __name__ == "__main__":
    # file_dir = pathlib.Path("data")
    # file_temp = "participants2.json"
    # file_input = f"{file_dir}/{file_temp}"
    # file_output = f"{file_dir}/result.json"
    #
    # how_many_winners = 4
    #
    # lottery_scheme = "data/lottery_templates/separate_prizes.json"
    # lottery_scheme = "data/lottery_templates/item_giveaway.json"
    #
    # file_extension = check_file_extension(file_temp)
    # file_content = open_file(file_input, file_extension)
    #
    # print(file_temp, "\n")
    #
    # prizes = extract_lottery_scheme(lottery_scheme)
    #
    # draw_participants(file_content, how_many_winners, prizes, file_output)

    who_won_lottery()
