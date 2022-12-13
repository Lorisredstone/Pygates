from typing import Tuple, List, Any

import contextlib

with contextlib.redirect_stdout(None):
    import pygame
    
import src.menu as menu
import src.Elements.BlankElement as BlankElement

class Window:
    def __init__(self, size:Tuple[int, int]) -> None:
        self.size:Tuple[int, int] = size
        self.size_x:int = size[0]
        self.size_y:int = size[1]
        pygame.init()
        self.screen:pygame.surface.Surface = pygame.display.set_mode(size)
        pygame.display.set_caption("LogicPy")
        # to move the map with keyboard
        self.key_state:List[bool] = [False, False, False, False]
        self.window_offset:List[int] = [0, 0]
        
        # now we get every element
        self.menu:menu.Menu = menu.Menu(50, size)
        
        # the list of things to the screen
        self.to_screen:List[BlankElement.Element] = []
        
    def draw(self) -> None:
        new_elements:List[BlankElement.Element] = self.menu.render()
        for element in new_elements:
            self.to_screen.append(element)
    
    def mainloop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.click(event.pos)
                if event.type == pygame.KEYUP and event.key == pygame.K_c:
                    self.to_screen = []
            # we create the new frame with a flip
            self.screen.fill((0, 0, 0))
            self.draw()
            for element in self.to_screen:
                element.render(self.to_screen)
            pygame.display.flip()