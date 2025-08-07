from screen import Screen
import pygame
DEFAULT_BG_COLOUR = (255,255,255)

"""
CONTAINS THE TREE BUILDING, AND PREORDER, INORDER AND POSTORDER TRAVERSAL 
VISUALISING
"""

class TreeVisualiser(Screen):
    def __init__(self):
        super().__init__()

    def draw(self):
        self.display.fill(DEFAULT_BG_COLOUR)
        ...
        super().draw()

    def eventHandler(self):
        ...
        super().eventHandler()

    def update(self):
        ...
        super().update()
