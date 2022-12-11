from typing import Tuple, List, Any

import contextlib

with contextlib.redirect_stdout(None):
    import pygame

import src.Elements.BlankElement
    
class Element:
    def __init__(self, screen:pygame.surface.Surface, currently_selected:bool = False) -> None:
        self.currently_selected:bool = currently_selected
        self.screen:pygame.surface.Surface = screen
    
    def reset(self) -> None:
        self.currently_selected = False
        ...
    
    def click(self) -> None:
        ...
    
    def render(self, screen:pygame.surface.Surface, pos:Tuple[int, int], size:Tuple[int, int]) -> None:
        ...
        
    def windowClick(self, pos:Tuple[int, int]) -> src.Elements.BlankElement.Element | None:
        ...
        
    # common methods with the same code for every object in the menu
    def show_selected(self, screen:pygame.surface.Surface, pos:Tuple[int, int], size:Tuple[int, int]) -> None:
        color:Tuple[int, int, int] = (255, 0, 0)
        # we draw a blue line on the left side of the element
        pygame.draw.rect(screen, color, (pos[0]-2, pos[1], 2, size[1]))
        # we draw a blue line on the bottom side of the element
        pygame.draw.rect(screen, color, (pos[0], pos[1]+size[1]-2, size[0], 2))
        # we draw a blue line on the top side of the element
        pygame.draw.rect(screen, color, (pos[0], pos[1], size[0], 2))