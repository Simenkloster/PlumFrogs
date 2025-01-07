from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Fan(Object): # 24 x 8
    ANIMATION_DELAY = 4
    def __init__(self,x,y,width=24,height=8):
        super().__init__(x,y,width,height, "fan")
        self.fan = load_sprite_sheets("Traps","Fan",width,height)
        self.image = self.fan["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Off"
    
    def on(self):
        self.animation_name = "On"
    
    def off(self):
        self.animation_name = "Off"
    
    def loop(self):
        sprites = self.fan[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
