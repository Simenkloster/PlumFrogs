import pygame
from sprite_functions import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    PLAYER_VEL = 5
    COLOR = (0,200,255)
    GRAVITY = 1
    ANIMATION_DELAY = 3
    HOVER_DURATION = 1
    INVINCIBLE_DURATION = 120
    SUPERSPEED_DURATION = 180
    FINISHLEVEL_DURATION = 180
    
    def __init__(self,x,y,width,height):
        super().__init__()
        self.initialX = x
        self.initialY = y
        self.spawn_x = self.initialX
        self.spawn_y = self.initialY
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.appearing = True
        self.SPRITES = load_sprite_sheets("MainCharacters","NinjaFrog",32,32,True)
        self.hit = False
        self.hit_count = 0
        sprites = self.SPRITES['idle_left']  
        self.sprite = sprites[0]  
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.hovering = False
        self.HOVER_FORCE = -2
        self.hover_timer = 0
        self.lives = 3
        self.invincible = False
        self.invincible_timer = 0
        self.superspeed_active = False
        self.superspeed_timer = 0
        self.finishLevel_timer = 0
        self.finishlevelTimer_active = False
        self.conveyor_active = False  # Whether the conveyor effect is active
        self.conveyor_speed = 0
        self.finishedLevelStatus = False

    

    def activate_superspeed(self):
        if not self.superspeed_active:
            self.superspeed_active = True
            self.superspeed_timer = self.SUPERSPEED_DURATION
            self.PLAYER_VEL = 10
    
    def activateFinishlevelTimer(self):
        if not self.finishlevelTimer_active:
            self.finishlevelTimer_active = True
            self.finishLevel_timer = self.FINISHLEVEL_DURATION


    def jump(self):
        self.deactivate_conveyor()
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def activate_conveyor(self):
        self.conveyor_active = True
        self.conveyor_speed = 4

    def deactivate_conveyor(self):
        self.conveyor_active = False
        self.conveyor_speed = 0

    def highjump(self):
        self.y_vel = -self.GRAVITY * 16
        self.animation_count = 0
        self.jump_count = 1
        self.fall_count = 0

    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

    def make_hit(self):
        self.hit = True
        self.hit_count = 0
        self.take_damage()

    def take_damage(self):
        if not self.invincible:
            self.lives -= 1
            self.invincible = True
            self.invincible_timer = self.INVINCIBLE_DURATION
    
    def respawn(self):
        self.finishedLevelStatus = False
        self.rect = pygame.Rect(self.spawn_x,self.spawn_y,self.width,self.height)
        self.lives = 3
        self.animation_count = 0
        self.appearing = True
        self.y_vel, self.x_vel = 0, 0
        self.fall_count = 0
        self.invincible_timer = 0
        self.hit = False
        self.hit_count = 0

        return [self.spawn_x, self.spawn_y]

    def move_left(self,vel):
        if not self.appearing:
            self.x_vel= -vel
            if self.direction != 'left':
                self.direction = 'left'
                self.animation_count = 0

    def move_right(self,vel):
        if not self.appearing:
            self.x_vel = vel
            if self.direction != 'right':
                self.direction = 'right'
                self.animation_count = 0

    def finishLevel(self):
        print("KJØRER FINISH LEVEL")
        self.rect.x = 100
        self.rect.y = 100
        self.spawn_x = 100
        self.spawn_y = 100
        self.finishedLevelStatus = True
        

    def update_respawn_position(self, x, y):
        self.spawn_x = x
        self.spawn_y = y

        return [x, y] #Prøver å returnere siste spawn-setting slik at en kan sette riktig offset i main når man trykker respawn knappen? Funker nå i hvert fall
    

    def loop(self,fps):

        if self.finishlevelTimer_active:
            self.finishLevel_timer -= 1
            if self.finishLevel_timer <= 0:
                self.finishLevel()
                self.finishlevelTimer_active = False
                self.finishLevel_timer = self.FINISHLEVEL_DURATION

        if self.superspeed_active:
            self.superspeed_timer -=1
            if self.superspeed_timer <= 0:
                self.superspeed_active = False
                self.PLAYER_VEL = 6

        if self.conveyor_active:
            self.rect.x += self.conveyor_speed

        if self.hovering:
            self.jump_count = 1
            if self.hover_timer > 0:
                self.y_vel = self.HOVER_FORCE
                self.hover_timer -= 1
            else:
                self.stop_hover()
        else:
            self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)



        
        self.move(self.x_vel,self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False

        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def bump_left(self):
        pass
        #Skal lage denne senere kanskje hvis jeg gidder

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1
    
    def hover(self):
        if not self.hovering:
            self.hovering = True
            self.hover_timer = self.HOVER_DURATION * 60
        self.fall_count = 0


            
    
    def stop_hover(self):
        self.hovering = False
        self.hover_timer = 0

    def update_sprite(self):
        if self.appearing:  
            sprite_sheet = load_sprite_sheets("MainCharacters", "AppDisapp", 96, 96, False)
            sprites = sprite_sheet["appearing"]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            self.update()
            
            if sprite_index >= len(sprites)-1: 
                self.appearing = False  
                self.animation_count = 0  
                sprite_sheet = "idle"  
            self.sprite = sprites[sprite_index % len(sprites)]  
            self.update()
        
        else:
            sprite_sheet = "idle"
            if self.hit:
                sprite_sheet = "hit"
            elif self.y_vel < 0:
                if self.jump_count == 1 or self.hovering:
                    sprite_sheet = "jump"
                elif self.jump_count == 2:
                    sprite_sheet = "double_jump"
            elif self.y_vel > self.GRAVITY * 2:
                sprite_sheet = "fall"
            elif self.x_vel != 0:
                sprite_sheet = "run"

            sprite_sheet_name = sprite_sheet + "_" + self.direction
            sprites = self.SPRITES[sprite_sheet_name]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            self.update()
        

    def update(self):
        self.rect = self.sprite.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self,win, offset_x,offset_y):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y - offset_y))