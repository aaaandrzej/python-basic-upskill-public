import unittest
from lottery import Participant, Prize, Winner


class TestClasses(unittest.TestCase): # todo zmienić na pytest
    def test_participant(self):
        p = Participant(1, "Jan", "Nowak", 2)
        self.assertEqual(p.id, 1)
        self.assertEqual(p.first_name, "Jan")
        self.assertEqual(p.last_name, "Nowak")
        self.assertEqual(p.weight, 2)

    def test_prize(self):
        p = Prize(1, "Jan Nowak", 2)
        self.assertEqual(p.id, 1)
        self.assertEqual(p.name, "Jan Nowak")
        self.assertEqual(p.amount, 2)


    def test_winner(self):
        w = Winner("Jan Nowak", "Gold medal")
        self.assertEqual(w.name, "Jan Nowak")
        self.assertEqual(w.prize, "Gold medal")

    def test_winner_to_dict(self):
        w = Winner("Jan Nowak", "Gold medal")
        self.assertEqual(w.to_dict(), {"name": "Jan Nowak", "prize": "Gold medal"})


if __name__ == '__main__':
    unittest.main()
