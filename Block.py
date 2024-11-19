import pygame
from Object import Object
from sprite_functions import get_block

class Block(Object):
    def __init__(self, x, y, size=96):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

