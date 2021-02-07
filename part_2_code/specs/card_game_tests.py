import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 4)
        self.card2 = Card("Clubs", 8)
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))

        
