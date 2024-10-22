from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Trampoline(Object): #28 x 28

    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height, "trampoline")
        self.trampoline = load_sprite_sheets("Traps","Trampoline",width,height)
        self.image = self.trampoline["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.ANIMATION_DELAY = 5

    def activated(self):
        self.animation_name = "Jump"
        self.animation_count = 0

    def deactivated(self):
        self.animation_name = "Idle"

    def loop(self):
        sprites = self.trampoline[self.animation_name]
        sprite_index = (self.animation_count//self.ANIMATION_DELAY)%len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        
        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0
            self.deactivated()

        self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        
