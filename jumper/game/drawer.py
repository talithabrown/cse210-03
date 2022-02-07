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
        self._word_list = ["monkey", "lion", "horse", "tiger", "panda", "puppy", "cat", "sheep", "skunk", "sloth", "elephant", "whale", "zebra", "bear", "koala", "lizard", "dog", "fish", "wolf"]
        self._word = list((random.choice(self._word_list)))
        self._hidden_word = list("_" * len(self._word))
        self._lives = 4

    def _get_hidden_word(self):
        for letter in self._hidden_word:
            print(letter, end=" ")
        print()

    def _get_lives(self):
        return self._lives

    def _replace_blank_with_letter(self, guess):
        hidden_word_idex = 0
        self._correct = False
        for letter in self._word:
            if guess.lower() == letter:
                self._hidden_word[hidden_word_idex] = guess
                self._correct = True
            hidden_word_idex += 1
    

    def _update_lives(self):
        if not self._correct:
            self._lives = self._lives - 1

    def _check_for_win(self):
        if "_" not in self._hidden_word:
            return 
        
