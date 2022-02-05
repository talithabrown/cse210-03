import random

class Drawer:
    """The person administrating the game. 
    
    The responsibility of Drawer is to select a random word and keep track of if the player is guessing correctly. 
    
    Attributes:
        _random_word (string): The random word the player is trying to guess.
        _words (List[string]): All possible random words.
    """

    def __init__(self):
        """Constructs a new Drawer.

        Args:
            self (Drawer): An instance of Drawer.
        """
        self._correct = False
        self._word_list = ["Bison", "Camel", "Horse", "Tiger", "Panda", "Puppy", "Rhino", "Sheep", "Skunk", "Sloth", "Snake", "Whale", "Zebra"]
        self._word = (random.choice(self._word_list))
        self._guessed_word = "_ " * len(self._word)

    def check_guess(self, guess):

        self.A = len(self._word)
        self.B = 0
        while self.A > 0:
            if guess == self._word[self.B]:
                self._guessed_word[self.B] = guess
                self._correct = True
            self.A = self.A-1
            self.B = self.B+1