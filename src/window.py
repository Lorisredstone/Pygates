from typing import Tuple, List
import pygame

class Window:
    def __init__(self, size:Tuple[int, int]) -> None:
        self.size:Tuple[int, int] = size
        self.size_x:int = size[0]
        self.size_y:int = size[1]
        pygame.init()
        self.screen:pygame.surface.Surface = pygame.display.get_surface()
        pygame.display.set_mode(self.size)
        pygame.display.set_caption("LogicPy")
        # to move the map with keyboard
        self.key_state:List[bool] = [False, False, False, False]
        self.window_offset:List[int] = [0, 0]
    
    def mainloop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("Quitting logicPy...")
                    return