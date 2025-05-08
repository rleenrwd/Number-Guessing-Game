import unittest
from main import choose_difficulty

class DifficultyTestCase(unittest.TestCase):

    """Class to test the choose_difficulty function in main.py"""
    def test_quitting_game(self):
        """Does pressing 'q' quit the game"""
        choice = choose_difficulty("q")
        self.assertEqual(choice, "quit")

    def test_empty_string_selection(self):
        """Does entering an empty string return a message?"""
        choice = choose_difficulty("")
        self.assertEqual(choice, "That isn't a valid choice. Enter either 'easy' or 'hard' to continue.")

    def test_easy_mode_selection(self):
        """Does entering 'easy' select easy mode and give the user 10 attempts"""
        choice = choose_difficulty("easy")
        self.assertEqual(choice, 10)

    def test_hard_mode_selection(self):
        """Does entering 'hard' select hard mode and give the user 5 attempts"""
        choice = choose_difficulty("hard")
        self.assertEqual(choice, 5)


if __name__ == '__main__':
    unittest.main()