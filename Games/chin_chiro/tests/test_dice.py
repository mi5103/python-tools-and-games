import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    def test_roll_dice(self):
        """Test that the roll_dice function generates three dice rolls, each between 1 and 6"""
        dice = Dice()
        roll = dice.roll_dice()
        for x in roll:
            self.assertGreaterEqual(x, 1)
            self.assertLessEqual(x, 6)
        self.assertEqual(len(roll), 3)
        self.assertTrue(roll[0] <= roll[1] <= roll[2])


if __name__ == "__main__":
    unittest.main()
