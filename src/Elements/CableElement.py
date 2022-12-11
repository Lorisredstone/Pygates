from typing import Tuple, List, Any
import math

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
import src.Elements.BlankElement
    
class Element(src.Elements.BlankElement.Element):
    def __init__(self, pos:List[Tuple[int, int]], screen:pygame.surface.Surface) -> None:
        self.pos:List[Tuple[int, int]] = pos
        self.screen = screen
        
    def render(self) -> None:
        # first we do the horizontal line
        pygame.draw.line(self.screen, (255, 255, 255), self.pos[0], (self.pos[1][0], self.pos[0][1]))
        # then we do the vertical line
        pygame.draw.line(self.screen, (255, 255, 255), (self.pos[1][0], self.pos[0][1]), self.pos[1])