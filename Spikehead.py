from Object import Object
import pygame
from sprite_functions import load_sprite_sheets

class Spikehead(Object):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spikehead")
        self.spikehead = load_sprite_sheets("Traps", "Spike Head", width, height)
        self.image = self.spikehead["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
        self.ANIMATION_DELAY = 3

        # Movement variables
        self.initial_y = y               # Starting y position (bottom position)
        self.target_y_up = y - 500        # Target y position for moving up (50 pixels up)
        self.movement_speed = 1          # Speed of upward movement
        self.fall_speed = 10              # Speed of falling down
        self.moving_up = True            # Start by moving up

        # Pause durations
        self.pause_duration_top = 500    # Pause 500 ms at the top
        self.pause_duration_bottom = 200 # Pause 500 ms at the bottom
        self.last_pause_time = 0         # Track last time we paused
        self.pausing = False             # Are we currently pausing?

        # Timer for blink control
        self.last_blink_time = pygame.time.get_ticks()  # Initial time in milliseconds
        self.blink_interval = 3000  # Blink every 3000 milliseconds (3 seconds)
        self.is_blinking = False

    def play_hit_animation(self):
        self.animation_name = "Hit"
        self.animation_count = 0

    def stop_hit_animation(self):
        self.animation_name = "Idle"
        self.animation_count = 0


    def blink(self):
        self.animation_name = "Blink"
        self.animation_count = 0
        self.is_blinking = True

    def loop(self):
        # Blink control
        current_time = pygame.time.get_ticks()
        if not self.is_blinking and current_time - self.last_blink_time >= self.blink_interval:
            self.blink()
            self.last_blink_time = current_time

        # Animation handling
        sprites = self.spikehead[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        if self.is_blinking and self.animation_count // self.ANIMATION_DELAY >= len(sprites):
            self.stop_hit_animation()
            self.is_blinking = False

        # Up and down movement with pauses
        if not self.pausing:  # Only move if not pausing
            if self.moving_up:
                if self.rect.y > self.target_y_up:
                    self.rect.y -= self.movement_speed
                else:
                    # Reached the top; pause
                    self.moving_up = False
                    self.pausing = True
                    self.last_pause_time = current_time
            else:
                if self.rect.y < self.initial_y:
                    self.rect.y += self.fall_speed
                else:
                    # Reached the bottom; pause
                    self.moving_up = True
                    self.pausing = True
                    self.last_pause_time = current_time

        # Check if pause duration has elapsed before resuming
        if self.pausing:
            if (self.moving_up and current_time - self.last_pause_time >= self.pause_duration_bottom) or \
               (not self.moving_up and current_time - self.last_pause_time >= self.pause_duration_top):
                self.pausing = False  # End the pause

        # Update mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)