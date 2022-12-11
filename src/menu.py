from typing import Tuple, List, Any

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
import src.Menu.BlankMenuElement
import src.Menu.CableElement
import src.Elements.BlankElement

class Menu:
    def __init__(self, menu_x_size:int, size:Tuple[int, int]) -> None:
        self.menu_x_size:int = menu_x_size
        self.size:Tuple[int, int] = size
        self.size_x:int = size[0]
        self.size_y:int = size[1]
        self.screen:pygame.surface.Surface = pygame.display.get_surface()
        self.possibilities:int = 4 #hardcoded
        self.currently_selected:int = -1
        
        self.menu_items:List[src.Menu.BlankMenuElement.Element] = [src.Menu.BlankMenuElement.Element(self.screen)] * self.possibilities
        self.menu_items[0] = src.Menu.CableElement.Element(self.screen)
        
        self.new_elements:List[src.Elements.BlankElement.Element] = []

    def render(self) -> List[src.Elements.BlankElement.Element]:
        pygame.draw.line(self.screen, (255, 255, 255), (self.size_x - self.menu_x_size, 0), (self.size_x - self.menu_x_size, self.size_y))
        # and we then draw the menu
        # we do the horizontal lines in the menu
        for i in range(self.possibilities):
            pygame.draw.line(self.screen, (255, 255, 255), (self.size_x - self.menu_x_size, self.size_y / self.possibilities * i), (self.size_x, self.size_y / self.possibilities * i))
        # we render the menu item
        for i in range(self.possibilities):
            # we have to translate the position by 1
            self.menu_items[i].render(self.screen, (self.size_x - self.menu_x_size + 1, int(self.size_y / self.possibilities * i)), (self.menu_x_size, int(self.size_y / self.possibilities)))
        # we then render the selected item
        if self.currently_selected != -1:
            self.menu_items[self.currently_selected].show_selected(self.screen, (self.size_x - self.menu_x_size + 1, int(self.size_y / self.possibilities * self.currently_selected)), (self.menu_x_size, int(self.size_y / self.possibilities)))
        new_elements:List[src.Elements.BlankElement.Element] = self.new_elements.copy()
        self.new_elements = []
        return new_elements
        
    def click(self, pos:Tuple[int, int]) -> None:
        # if the click isnt in the menu, we run the click on the selected item
        if not (pos[0] > self.size_x - self.menu_x_size):
            new_element:src.Elements.BlankElement.Element | None = self.menu_items[self.currently_selected].windowClick(pos)
            if new_element is not None:
                self.new_elements.append(new_element)
            return
        # if we are here, we are in the menu
        # we get the menu item
        menu_item:int = int(pos[1] // (self.size_y / self.possibilities))
        if self.currently_selected == menu_item:
            self.currently_selected = -1
        else:
            self.menu_items[self.currently_selected].click()
            self.currently_selected = menu_item
        # we then get the menu item
        self.menu_items[menu_item].click()
        # and we set the last selected item to not_selected