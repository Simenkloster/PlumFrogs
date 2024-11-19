import pygame
from sprite_functions import load_sprite_sheets

class Player(pygame.sprite.Sprite):
    COLOR = (0,200,255)
    GRAVITY = 1
    ANIMATION_DELAY = 3
    HOVER_GRAVITY = 0.2
    HOVER_DURATION = 1
    INVINCIBLE_DURATION = 120
    SUPERSPEED_TIMER = 300

    def __init__(self,x,y,width,height):
        super().__init__()
        self.spawn_x = x
        self.spawn_y = y
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
        sprites = self.SPRITES['idle_left']  # Assuming 'idle_left' is the default state
        self.sprite = sprites[0]  # Default to the first frame of the idle animation
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.hovering = False
        self.HOVER_FORCE = -4
        self.hover_timer = 0
        self.lives = 3
        self.invincible = False
        self.invincible_timer = 0
        self.super_speed_active = False
        self.speed_timer = 0
        self.vel = 5


    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

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
        self.rect = pygame.Rect(self.spawn_x,self.spawn_y,self.width,self.height)
        self.lives = 3
        self.animation_count = 0
        self.appearing = True

    def move_left(self,vel):
        self.x_vel= -vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self,vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0
    
    def activate_speed(self):
        self.super_speed_active = True
        self.speed_timer = self.SUPERSPEED_TIMER

    def loop(self,fps):
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

        if self.lives <= 0:
            self.respawn()
        self.update_sprite()

        if self.super_speed_active:
            self.vel = 8
            self.speed_timer -= 1
            if self.speed_timer <= 0:
                self.super_speed_active = False
                self.vel = 5

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

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
        if self.appearing:  # Handle the appearing animation
            sprite_sheet = load_sprite_sheets("MainCharacters", "AppDisapp", 96, 96, False)
            sprites = sprite_sheet["appearing"]
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
            self.update()
            
            if sprite_index >= len(sprites)-1:  # End of appearing animation
                self.appearing = False  # Exit appearing state
                self.animation_count = 0  # Reset the animation count for normal animations
                sprite_sheet = "idle"  # Transition to idle state after appearing
                sprites = self.SPRITES[sprite_sheet + "_" + self.direction]
            self.sprite = sprites[sprite_index % len(sprites)]  # Loop if necessary
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

    def draw(self,win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))