import pytest
from participant import Participant
from prize import Prize, extract_prizes_from_scheme
from winner import Winner, draw_winners


class TestParticipant:
    def test_participant(self):
        p = Participant(1, "Jan", "Nowak", 2)
        assert p.id == 1
        assert p.first_name == "Jan"
        assert p.last_name == "Nowak"
        assert p.weight == 2

    def test_participant_no_weight(self):
        p = Participant(1, "Jan", "Nowak")
        assert p.id == 1
        assert p.first_name == "Jan"
        assert p.last_name == "Nowak"
        assert p.weight == 1


class TestPrizeTests:
    def test_prize(self):
        p = Prize(1, "Puchar")
        assert p.id == 1
        assert p.name == "Puchar"

    def test_extract_prizes_from_scheme(self, filename="tests/test_scheme.json"):
        prizes = extract_prizes_from_scheme(filename)
        assert len(prizes) == 2
        assert prizes[0].name == "Prize"
        assert prizes[0].id == 1
        assert prizes[1].name == "Prize"
        assert prizes[1].id == 1


class TestWinnerTests:
    def test_winner(self):
        w = Winner("Jan Nowak", "Gold medal")
        assert w.name == "Jan Nowak"
        assert w.prize == "Gold medal"

    def test_winner_to_dict(self):
        w = Winner("Jan Nowak", "Gold medal")
        assert w.to_dict() == {"name": "Jan Nowak", "prize": "Gold medal"}

    def test_draw_winners_test_no_participant(self):
        file_content = []
        prizes = [Prize("1", "Annual Vim subscription")]
        with pytest.raises(ValueError) as ex:
            draw_winners(file_content, prizes)
        assert ex.value.args[0] == "Nie mam uczestników :("

    def test_draw_winners_test_no_prizes(self):
        file_content = [Participant(1, "Aaa", "Bbb")]
        prizes = []
        with pytest.raises(ValueError) as ex:
            draw_winners(file_content, prizes)
        assert ex.value.args[0] == "Nie mam nagród :("

    def test_draw_winners_test_less_prizes_then_participants(self):
        file_content = [Participant(1, "Aaa", "Bbb"), Participant(1, "Aaa", "Bbb")]
        prizes = [Prize("1", "Annual Vim subscription")]
        assert len(draw_winners(file_content, prizes)) == 1

    def test_draw_winners_test_more_prizes_then_participants(self):
        file_content = [Participant(1, "Aaa", "Bbb")]
        prizes = [Prize("1", "Prize"), Prize("1", "Prize")]
        assert len(draw_winners(file_content, prizes)) == 1


if __name__ == "__main__":

    pytest.main()  # testy powinny być uruchamiane z root'a - czyli katalog powyżej (pytest lub python -m pytest)
