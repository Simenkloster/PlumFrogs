from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Pineapple(Object): # 16 x 16?
    ANIMATION_DELAY = 3
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height, "pineapple")
        self.pineapple =load_sprite_sheets("Fruits","Pineapple",width,height)
        self.image = self.pineapple["Pineapple"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Pineapple"
        self.active = True
        self.isCollected = False
        self.dummymask = pygame.mask.Mask((1,1))
    
    def loop(self):
        if not self.active:
            return
        sprites = self.pineapple[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect =self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_name == "Collected" and self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.active = False
            self.image = pygame.Surface((1,1))
            self.rect = self.image.get_rect(topleft=(-100,-100))
            self.mask = self.dummymask

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

    def collected(self):
        if not self.isCollected:
            self.animation_name = "Collected"
            self.animation_count = 0
            self.isCollected = True