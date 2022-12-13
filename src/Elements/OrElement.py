from typing import Tuple, List, Any
from typing_extensions import Self

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
import src.Elements.BlankElement
    
class Element(src.Elements.BlankElement.Element):
    def __init__(self, pos:List[Tuple[int, int]], screen:pygame.surface.Surface) -> None:
        self.pos:List[Tuple[int, int]] = pos
        self.orPos:Tuple[int, int] = pos[0]
        self.screen = screen
        
    def render(self, to_render:List[Self]) -> None:
        # we show assets/OrElement.jpg
        image:pygame.surface.Surface = pygame.image.load("Assets/OrElement.jpg")
        new_pos:Tuple[int, int] = (self.orPos[0] - int(image.get_width() / 2), self.orPos[1] - int(image.get_height() / 2))
        self.screen.blit(image, (new_pos[0], new_pos[1]))