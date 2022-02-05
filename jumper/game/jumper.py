

class Jumper:
    """The person playing the game (guessing). 
    
    The responsibility of Jumper is to keep track of the players guess. 
    
    Attributes:
        _player_guess (string): The letter the player guesses.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._life = 4

    def jump(self):

        if self._life == 4:
            print("  _____")
            print(" /_____\\")
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")
        if self._life == 3:
            print(" /_____\\")
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")
        if self._life == 2:
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")
        if self._life == 1:
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")
        if self._life == 0:
            print("    X")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")