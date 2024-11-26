from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Pineapple(Object): # 16 x 16?
    ANIMATION_DELAY = 6
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height, "pineapple")
        self.pineappel =load_sprite_sheets("Fruits","Pineapple",width,height)
        self.image = self.pineappel["Pineapple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Pineapple"
    
    def loop(self):
        sprites = self.pineappel[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if  self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0