# Start here. Once you have good test, move on to hw2.py

import unittest
from hw2 import Card, Deck, is_group

class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        """Test that we can get a good string representation of GroupCard instances"""
        c1 = Card(2, "green", "striped", "diamond")
        self.assertEqual(str(c1),'Card(2, green, striped, diamond)')

    def test_eq(self):
        """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
        c1 = Card(1,'green','empty','diamond')
        c2 = Card(1,'green','empty','diamond')
        self.assertTrue(c1==c2)

# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize decks with given list: numbers/shapes/colors/shadings"""
        d1 = Deck()
        self.assertTrue(d1.numbers==[1,2,3])
        self.assertTrue(d1.shapes==['diamond', 'squiggle', 'oval'])
        self.assertTrue(d1.colors==['green', 'blue', 'purple'])
        self.assertTrue(d1.shadings==['empty', 'striped', 'solid'])

    def test_draw_top(self):
        """Test that we can use to check if the draw_top function returns the expected output"""
        d1 = Deck()
        self.assertEqual(d1.draw_top(),Card(3, 'purple', 'solid', 'oval'))

    def test_shuffle(self):
        """Test that we can use to check if the shuffle function returns the expected output"""
        test_deck = Deck([1],['oval'],['red','green'],['empty','solid'])
        test_deck.shuffle()
        self.assertEqual(test_deck.cards, [Card(1, 'red', 'empty', 'oval'), Card(1, 'green', 'solid', 'oval'), Card(1, 'green', 'empty', 'oval'), Card(1, 'red', 'solid', 'oval')])

# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    '''creates 6 cards and checked whether grouping 3 together will form a group or not'''
    def test_is_group(self):
        """Test to see if the is_group function returns the expected output of True or False according to the grouping of the cards"""
        c1 = Card(1,'green','striped','diamond')
        c2 = Card(1,'red','striped','diamond')
        c3 = Card(1,'green','solid','oval')
        c4 = Card(3,'green','striped','diamond')
        c5 = Card(4,'green','striped','diamond')
        c6 = Card(4,'blue','empty','squiggle')
        self.assertTrue(is_group(c1,c2,c3))
        self.assertFalse(is_group(c4,c5,c6))
        self.assertTrue(is_group(c3,c5,c6))

unittest.main() # runs all unittests above