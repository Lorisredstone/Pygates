from typing import Tuple, List, Any

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
class Element:
    def __init__(self, pos:List[Tuple[int, int]], screen:pygame.surface.Surface) -> None:
        self.pos:List[Tuple[int, int]] = pos
        self.screen = screen
    
    def render(self) -> None:
        ...