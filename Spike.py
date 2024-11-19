from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Spike(Object): # 16 x 16

    def __init__(self,x,y,width=16,height=16):
        super().__init__(x, y, width, height, "spikes")
        self.Spikes = load_sprite_sheets("Traps","Spikes",width,height)
        self.image = self.Spikes["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)