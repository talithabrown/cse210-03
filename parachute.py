x = input("Press enter")

class Parachute:

    def __init__(self):
        self.life = 4

    def jump(self):

        if self.life == 4:
            print("  _____")
            print(" /_____\\")
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
            print("\n^^^^^^^^^")
        if self.life == 3:
            print(" /_____\\")
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
        if self.life == 2:
            print(" \     /")
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
        if self.life == 1:
            print("  \   /")
            print("    0")
            print("   /|\\")
            print("   / \\")
        if self.life == 0:
            print("    X")
            print("   /|\\")
            print("   / \\")
            #the game ends
