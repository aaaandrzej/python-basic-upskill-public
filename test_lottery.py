import pytest
from lottery import Participant, Prize, Winner


def test_participant():
    p = Participant(1, "Jan", "Nowak", 2)
    assert p.id == 1
    assert p.first_name == "Jan"
    assert p.last_name == "Nowak"
    assert p.weight == 2


def test_prize():
    p = Prize(1, "Jan Nowak", 2)
    assert p.id == 1
    assert p.name == "Jan Nowak"
    assert p.amount == 2


def test_winner():
    w = Winner("Jan Nowak", "Gold medal")
    assert w.name == "Jan Nowak"
    assert w.prize == "Gold medal"


def test_winner_to_dict():
    w = Winner("Jan Nowak", "Gold medal")
    assert w.to_dict() == {"name": "Jan Nowak", "prize": "Gold medal"}

