import pygame
from Object import Object
from sprite_functions import load_sprite_sheets


class Goal(Object): #64x64
    def __init__(self, x, y, width = 64, height = 64):
        super().__init__(x,y, width, height, name="goal")
        self.goal = load_sprite_sheets("Checkpoints", "End", width, height)
        self.image = self.goal["End"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.activated = False
        self.animation_name = "End"
        self.ANIMATION_DELAY = 8

    def activate(self):
        if not self.activated:
            self.activated = True
            self.animation_name ="EndPressed"
            self.animation_count = 0

    def makeIdle(self):
        self.ANIMATION_DELAY = 3
        self.animation_name = "End"
        self.animation_count = 0
    


    def loop(self):
        sprites = self.goal[self.animation_name]
        sprite_index = (self.animation_count//self.ANIMATION_DELAY)%len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1


        if self.animation_count // self.ANIMATION_DELAY >= 2*len(sprites):
            self.animation_count = 0
            self.makeIdle()


                  


        self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
