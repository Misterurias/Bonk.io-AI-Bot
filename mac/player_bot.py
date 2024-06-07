import random
import time

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= 1
        print(f"Moved UP to ({self.x}, {self.y})")

    def move_down(self):
        self.y += 1
        print(f"Moved DOWN to ({self.x}, {self.y})")

    def move_left(self):
        self.x -= 1
        print(f"Moved LEFT to ({self.x}, {self.y})")

    def move_right(self):
        self.x += 1
        print(f"Moved RIGHT to ({self.x}, {self.y})")

    def move_up_right(self):
        self.x += 1
        self.y -= 1
        print(f"Moved UP-RIGHT to ({self.x}, {self.y})")

    def move_up_left(self):
        self.x -= 1
        self.y -= 1
        print(f"Moved UP-LEFT to ({self.x}, {self.y})")

    def move_down_right(self):
        self.x += 1
        self.y += 1
        print(f"Moved DOWN-RIGHT to ({self.x}, {self.y})")

    def move_down_left(self):
        self.x -= 1
        self.y += 1
        print(f"Moved DOWN-LEFT to ({self.x}, {self.y})")

    def get_position(self):
        return self.x, self.y

def main():
    # Initialize the player at the starting position (0, 0)
    player = Player(0, 0)

    # Define possible movements
    movements = [
        player.move_up,
        player.move_down,
        player.move_left,
        player.move_right,
        player.move_up_right,
        player.move_up_left,
        player.move_down_right,
        player.move_down_left
    ]

if __name__ == "__main__":
    main()
