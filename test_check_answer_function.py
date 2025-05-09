import unittest
import main
from unittest.mock import patch
from io import StringIO
from main import user_guess

class CheckAnswerTest(unittest.TestCase):
    """ Class to test the check_answer function in main.py"""

    main.num_of_guesses_left = 3

    # This decorator replaces sys.stdout with a StringIO object, so that the print statements can be 
    # captured and examined in the tests
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_high(self, mock_stdout):
        result = main.check_answer(user_guess, 1)
        # This will check that result is 'None' since there's no return statement only print statements
        self.assertIsNone(result)

        # This will store the output, which should be "Your answer, {user_guess}, was too high, try again." 
        # And also, "You have {num_of_guesses_left} guesses left."
        output = mock_stdout.getvalue()
        
        self.assertEqual(f"Your answer, {user_guess}, was too high, try again.\nYou have {main.num_of_guesses_left} guesses left.\n", output)

        self.assertEqual(main.num_of_guesses_left, 2)

  
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_low(self, mock_stdout):
        result = main.check_answer(user_guess, 100)
        self.assertIsNone(result)
        output = mock_stdout.getvalue()
        self.assertEqual(f"Your answer, {user_guess}, was too low, try again.\nYou have {main.num_of_guesses_left} guesses left.\n", output)
        self.assertEqual(main.num_of_guesses_left, 2)
 
    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_guess(self, mock_stdout):
        result = main.check_answer(50, 50)
        output = mock_stdout.getvalue()
        self.assertIn("CORRECT!", output)
        self.assertTrue(result)
        self.assertEqual(main.num_of_guesses_left, 3)

if __name__ == '__main__':
    unittest.main()