import pytest
from participant import Participant
from prize import Prize, extract_prizes_from_scheme
from winner import Winner, draw_winners


# class ParticipantTests:
def test_participant():
    p = Participant(1, "Jan", "Nowak", 2)
    assert p.id == 1
    assert p.first_name == "Jan"
    assert p.last_name == "Nowak"
    assert p.weight == 2


# class PrizeTests:
def test_prize():
    p = Prize(1, "Puchar")
    assert p.id == 1
    assert p.name == "Puchar"


def test_extract_prizes_from_scheme(filename="data/lottery_templates/item_giveaway.json"):
    expected_prizes = [Prize("1", "Annual Vim subscription") for _ in range(5)]
    prizes = extract_prizes_from_scheme(filename)

    assert len(prizes) == len(expected_prizes) == 5
    # assert prizes == expected_prizes


# class WinnerTests:
def test_winner():
    w = Winner("Jan Nowak", "Gold medal")
    assert w.name == "Jan Nowak"
    assert w.prize == "Gold medal"


def test_winner_to_dict():
    w = Winner("Jan Nowak", "Gold medal")
    assert w.to_dict() == {"name": "Jan Nowak", "prize": "Gold medal"}


def draw_winners_test_no_participant():
    file_content = [Participant(1, "Aaa", "Bbb") for _ in range(3)]
    prizes = [Prize("1", "Annual Vim subscription") for _ in range(2)]
    assert draw_winners(file_content, prizes) == ValueError  # yyy tak??


def draw_winners_test_no_prizes():
    file_content = [Participant(1, "Aaa", "Bbb") for _ in range(3)]
    prizes = []
    assert draw_winners(file_content, prizes) == ValueError  # yyy tak??


def draw_winners_test_less_prizes_then_participants():
    file_content = [Participant(1, "Aaa", "Bbb") for _ in range(3)]
    prizes = [Prize("1", "Annual Vim subscription") for _ in range(2)]
    p = len(draw_winners(file_content, prizes))
    assert p == 3  # yyy tak??


def draw_winners_test_more_prizes_then_participants():
    file_content = [Participant(1, "Aaa", "Bbb") for _ in range(3)]
    prizes = [Prize("1", "Annual Vim subscription") for _ in range(4)]
    assert draw_winners(file_content, prizes) == ValueError  # yyy tak??


if __name__ == "__main__":

    pytest.main()
