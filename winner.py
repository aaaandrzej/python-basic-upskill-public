import random
import json
from prize import Prize
from participant import Participant


class Winner:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

    def __repr__(self):
        return f"{self.name} - {self.prize}"

    def to_dict(self):
        return {"name": self.name, "prize": self.prize}


def draw_winners(participants_list, prizes):  # TODO obtestować to, np kiedy nie ma uczestników albo nagród

    if len(participants_list) < len(prizes):
        raise ValueError("Za mało uczestników, za dużo nagród")

    if len(prizes) < 1:
        raise ValueError("Nie mam nagród :(")

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


if __name__ == "__main__":

    file_output = "result.json"

    file_content = [Participant(1, "Aaa", "Bbb") for _ in range(3)]

    prizes = [Prize("1", "Annual Vim subscription") for _ in range(2)]

    winners_with_prizes = draw_winners(file_content, prizes)

    write_winners_to_json(winners_with_prizes, file_output)
    print_winners(winners_with_prizes)

