from typing import Tuple, List, Any
import math

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
import src.Menu.BlankMenuElement
import src.Elements.CableElement
import src.Elements.BlankElement
    
class Element(src.Menu.BlankMenuElement.Element):
    def __init__(self, screen:pygame.surface.Surface, currently_selected:bool = False) -> None:
        self.image:pygame.surface.Surface = pygame.image.load("Assets/CableElement.jpg")
        self.screen:pygame.surface.Surface = screen
        self.currently_selected:bool = currently_selected
        self.placements:List[Tuple[int, int]] = [(0, 0), (0, 0)]
        self.nb_of_placed_points:int = 0
    
    def reset(self) -> None:
        self.currently_selected = False
        self.placements = [(0, 0), (0, 0)]
        self.nb_of_placed_points = 0
    
    def click(self) -> None:
        self.currently_selected = not self.currently_selected
        self.reset()
        
    def draw_to_screen(self) -> src.Elements.CableElement.Element:
        return src.Elements.CableElement.Element(self.placements, self.screen)
            
    def windowClick(self, pos:Tuple[int, int]) -> src.Elements.BlankElement.Element | None:
        to_return:src.Elements.BlankElement.Element | None = None
        if self.nb_of_placed_points == 0:
            self.placements[0] = pos
            self.nb_of_placed_points += 1
        elif self.nb_of_placed_points == 1:
            self.placements[1] = pos
            self.nb_of_placed_points += 1
            to_return = self.draw_to_screen()
            # we have to draw a line between the two points
            self.reset()
        return to_return
        
    def render(self, screen:pygame.surface.Surface, pos:Tuple[int, int], size:Tuple[int, int]) -> None:
        # before we render the image, we have to add black at the top and bottom
        # we do this by creating a new surface
        new_image:pygame.surface.Surface = pygame.Surface((size[0], size[1]))
        # we then fill it with black
        new_image.fill((0, 0, 0))
        # we then blit the image onto the new image
        new_image.blit(self.image, (0, int((size[1] - self.image.get_height()) / 2)))
        # we then blit the new image onto the screen
        screen.blit(new_image, (pos[0], pos[1]))