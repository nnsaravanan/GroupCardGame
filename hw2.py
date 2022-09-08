# STOP! You should write tests in TestHw2.py before modifying this file.

import numbers
import random
from turtle import shapetransform


class Card:
    def __init__(self,number,color,shading,shape):
        # changes all the values to lower for ease of use
        self.number = number
        self.color = color.lower()
        self.shading = shading.lower()
        self.shape = shape.lower()
        
    def __str__(self):
        # returns a formatted string when the str function is called
        return "Card("+str(self.number)+", "+self.color+", "+self.shading+", "+self.shape+")"

    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        # returns if all the values are true
        return self.number==other.number and self.color==other.color and self.shading == other.shading and self.shape == other.shape


# Valid values for default game of GROUP! included here to avoid spelling
# issues. Feel free to copy/paste:
# [1, 2, 3]
# ['diamond', 'squiggle', 'oval']
# ['green', 'blue', 'purple']
# ['empty', 'striped', 'solid']
class Deck:
    def __init__(self,numbers=[1, 2, 3],shapes=['diamond', 'squiggle', 'oval'],colors=['green', 'blue', 'purple'],shadings=['empty', 'striped', 'solid']):
        # sets all given params to the proper attributes
        self.numbers = numbers
        self.shapes = shapes
        self.colors = colors
        self.shadings = shadings
        # list comprehension to create a list of all the cards with the card class
        self.cards = [Card(num,col,shade,shape) for num in numbers for shape in shapes for col in colors for shade in shadings]
    # should remove and return top card
    def draw_top(self):
        # checks whether the length of the list of cards are 0 and raises and error if list is empty
        if len(self.cards)==0:
            raise AttributeError
        else:
            return self.cards.pop()

    # should randomly shuffle cards. Does not need a return.
    def shuffle(self):
        # sets a seed so that the values can be tested 
        random.seed(652)
        random.shuffle(self.cards)

    # should return number of items in deck
    def __len__(self):
        # returns the length of the list of cards created in the initilization
        return len(self.cards)



# Once Card and Deck are both finished, write tests for this algorithm, then
# write the algorithm

# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(c1,c2,c3):
    return (((c1.number==c2.number==c3.number)or(c1.number!=c2.number!=c3.number))or((c1.color==c2.color==c3.color)or(c1.color!=c2.color!=c3.color))or((c1.shape==c2.shape==c3.shape)or(c1.shape!=c2.shape!=c3.shape))or((c1.shading==c2.shading==c3.shading)or(c1.shading!=c2.shading!=c3.shading)))

