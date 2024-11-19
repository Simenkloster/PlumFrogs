import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from Falling_platform import Falling_platform
from Spikehead import Spikehead
from Trampoline import Trampoline
from sprite_functions import *
from movement_functions import *
pygame.init()

heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart,(40,40))
pygame.display.set_caption("Platformer")


WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 6
window = pygame.display.set_mode((WIDTH, HEIGHT))




def main(window):
    clock = pygame.time.Clock()
    block_size = 96

    # background collor
    background, bg_image = get_background("Yellow.png", WIDTH, HEIGHT)
    
    
    
    
    #Making stuff that goes into the game
    Player1 = Player(100, 100, 50, 50)
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    spike = Spike(600, HEIGHT-block_size-32, 16, 16)
    fan = Fan(200, HEIGHT - block_size - 16, 24, 8)
    fan.on()
    falling_platforms = [Falling_platform(80*i, 350, 32, 10) for i in range(8, 20)]
    trampoline = Trampoline(300, HEIGHT - block_size - 56, 28, 28)
    #Liste med blocks som danner gulvet
    floor = [Block(i * block_size, HEIGHT - block_size, block_size) for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)]
    #Liste med alle tingene som inngår i spillet

    #Spikehead
    spikehead = Spikehead(-100, 600, 54,  52)

    objects = [*floor, fire, *falling_platforms, spike, fan, trampoline, spikehead]
   
   
   


    offset_x = 0
    scroll_area_width = 300



    #Game-loop
    run = True
    while run:
        clock.tick(FPS)
        Player1.loop(FPS)
        fire.loop()
        fan.loop()
        spikehead.loop()
        
        for platform in falling_platforms:
            platform.loop()
        
        
        trampoline.loop()
        #Håndterer bevegelse og kollisjon
        handle_move(Player1, objects, PLAYER_VEL) 
        
        #Tegner opp alt
        draw(window, background, bg_image, Player1, objects, offset_x)
        
        dynamic_x = 0
        for i in range(Player1.lives):
            dynamic_x+=45
            window.blit(heart,(dynamic_x,30))
        if Player1.lives == 0:
            offset_x = 0
        
        pygame.display.update()

        #Sjekker hvor spilleren er på skjermen og flytter kameraet
        if ((Player1.rect.right - offset_x >= WIDTH - scroll_area_width and Player1.x_vel > 0) or 
            (Player1.rect.left - offset_x <= scroll_area_width and Player1.x_vel < 0)):
            offset_x += Player1.x_vel


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Player1.jump_count < 2:
                    Player1.jump()

    
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
