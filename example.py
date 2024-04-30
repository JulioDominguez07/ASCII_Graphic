from ASCIIgraphic import *
import os

width = 20
height = 10

art = ASCIIgraphic(width, height)
for i in range(10):
    art.point(i, 0)
    art.display()