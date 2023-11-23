from PIL import Image
import numpy as np
from collections import deque

X_SIZE, Y_SIZE = 1024, 1024  # Set field dimension

field = np.ones((X_SIZE, Y_SIZE), np.byte)  # Create white field


class Ant:
    """Create Ant who will walk"""
    def __init__(self, field, pos):
        self.field = field
        self.x, self.y = pos
        self.increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])  # Create possible move directions

    def run(self):
        value = self.field[self.x, self.y]  # Get color of position
        self.field[self.x, self.y] = not value  # Invert position
        self.increments.rotate(1) if value else self.increments.rotate(-1)  # Change direction of the ant
        dx, dy = self.increments[0]  # Select increment for move
        self.x += dx  # Add increment for x
        self.y += dy  # Add increment for y

    def get_field(self) -> np.ndarray:
        return self.field


ant = Ant(field, pos=[field.shape[0] // 2, field.shape[1] // 2])  # place the ant to field center

while True:
    ant.run()
    if ant.x == X_SIZE or ant.y == Y_SIZE: break  # Checking the ant for reaching the border
    if ant.x == 0 or ant.y == 0: break  # Checking the ant for reaching the border

newfield = ant.get_field()  # Getting a field modified by movement of ant
newfield[newfield == 1] = -1  # Preparing field values to create contrasting Image

Image.fromarray(newfield, mode='L').show()  # Create & Show Image
