import unittest
from main import choose_difficulty

class DifficultyTestCase(unittest.TestCase):
    """Class to test the choose_difficulty function in main.py"""
    def test_quitting_game(self):
        """Does pressing 'q' quit the game"""
        choice = choose_difficulty("q")
        self.assertEqual(choice, "quit")

if __name__ == '__main__':
    unittest.main()