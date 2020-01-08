from mvp import *


class Prize:
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name}"


class Winner(Participant):
    def __init__(self, id, first_name, last_name, prize):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.prize = prize

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def extract_lottery_scheme(filename):
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        for prize in lottery_scheme["prizes"]:
            for amount in range(prize["amount"]):
                lottery_prizes_list.append(Prize(**prize))
        return lottery_prizes_list


def draw_participants(participants_list, how_many, prizes):
    winners_list = random.sample(participants_list, k=how_many)

    print(f"Zwycięska {how_many} to:")
    for winner in winners_list:
        try:
            indexxx = winners_list.index(winner)
            prize = prizes[indexxx]
        except IndexError:
            prize = "Audience Prize"
        winner_ = f"{winner} - {prize}"
        print(winner_)


if __name__ == "__main__":
    file_dir = pathlib.Path("data")
    file_temp = "participants2.json"
    file_input = f"{file_dir}/{file_temp}"

    how_many_winners = 4

    # lottery_scheme = "data/lottery_templates/separate_prizes.json"
    lottery_scheme = "data/lottery_templates/item_giveaway.json"


    file_extension = check_file_extension(file_temp)
    file_content = open_file(file_input, file_extension)

    print(file_temp, "\n")

    prizes = extract_lottery_scheme(lottery_scheme)

    draw_participants(file_content, how_many_winners, prizes)
