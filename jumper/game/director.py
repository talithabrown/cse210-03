from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.drawer import Drawer


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's player.
        is_playing (boolean): Whether or not to keep playing.
        drawer (Drawer): Draws the stick man and parachute.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._drawer = Drawer()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets and stores inout from the player.

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_updates(self):
        """Updates if the player loses a life or if the player guesses a letter correctly.

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_outputs(self):
        """Shows the player and word so far and the updated picture.

        Args:
            self (Director): An instance of Director.
        """
        
        # if self._hider.is_found():
        #     self._is_playing = False