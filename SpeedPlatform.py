#32x8
from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class SpeedPlatform(Object): # 28 x 28

    def __init__(self,x,y,width=28,height=28):
        super().__init__(x,y,width,height, "speedplatform")
        self.speedplatform = load_sprite_sheets("Traps","Speed Platforms",width,height)
        self.image = self.speedplatform["On"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "On"
        self.ANIMATION_DELAY = 2
        self.active = True


    def turn_on(self):
        self.animation_name = "On"
        self.animation_count = 0
        self.active = True

    def turn_off(self):
        self.animation_name = "Off"
        self.animation_count = 0
        self.active = False


    def loop(self):
        sprites = self.speedplatform[self.animation_name]
        sprite_index = (self.animation_count//self.ANIMATION_DELAY)%len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        
        if self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.animation_count = 0

        self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        
