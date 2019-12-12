from mvp import *


class Prize:
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name}, {self.amount}"


class Winner(Participant):
    pass


def extract_lottery_scheme(filename):
    with open(filename) as lottery_scheme_file:
        lottery_scheme = json.load(lottery_scheme_file)
        lottery_prizes_list = []
        lottery_prizes = lottery_scheme["prizes"]
        for prize in lottery_prizes:
            return Prize(**prize)


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

    lottery_scheme = "data/lottery_templates/item_giveaway.json"

    file_extension = check_file_extension(file_temp)
    file_content = open_file(file_input, file_extension)

    print(file_temp, "\n")
    draw_participants(file_content, how_many_winners)
    print()
    prizes = extract_lottery_scheme(lottery_scheme)
    print(prizes)
