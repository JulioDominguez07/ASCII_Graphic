# ASCIIgraphic.py
#
# Written by:
# Julio Gouveia
import os

class ASCIIgraphic:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
    def point(self, x, y, char='*'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[x][y] = char
    def display(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for row in self.canvas:
            print(''.join(row))
