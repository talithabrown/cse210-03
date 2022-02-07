from mimetypes import guess_all_extensions
from game.terminal_service import TerminalService
from game.drawer import Drawer
from game.jumper import Jumper


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
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
            
    def _do_outputs(self):
        """Shows the player and word so far and the updated picture.

        Args:
            self (Director): An instance of Director.
        """
        self._drawer._get_hidden_word()
        self._jumper.jump(self._drawer._get_lives())


    def _get_inputs(self):
        """Gets and stores input from the player.

        Args:
            self (Director): An instance of Director.
        """

        self.letter_guessed = self._terminal_service.read_text("Guess a letter [a-z]: ")
        
        
    def _do_updates(self):
        """Updates if the player loses a life or if the player guesses a letter correctly.

        Args:
            self (Director): An instance of Director.
        """
        self._drawer._replace_blank_with_letter(self.letter_guessed)
        self._drawer._update_lives()
        lives = self._drawer._get_lives()
        if lives == 0:
            self._jumper.jump(lives)
            self._terminal_service.write_text("You lose :(")
            self._is_playing = False
        elif "_" not in self._drawer._hidden_word:
            self._terminal_service.write_text("You won!")
            self._is_playing = False