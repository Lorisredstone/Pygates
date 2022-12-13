from typing import Tuple, List, Any
from typing_extensions import Self

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
class Element:
    def __init__(self, pos:List[Tuple[int, int]], screen:pygame.surface.Surface) -> None:
        self.pos:List[Tuple[int, int]] = pos
        self.screen = screen
    
    def render(self, to_render:List[Self]) -> None:
        ...