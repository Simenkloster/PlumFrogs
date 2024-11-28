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
window = pygame.display.set_mode((WIDTH, HEIGHT))




def main(window):
    clock = pygame.time.Clock()
    block_size = 96

    # background collor
    background, bg_image = get_background("Yellow.png", WIDTH, HEIGHT)
    
    
    
    
    #Making player
    Player1 = Player(100, 100, 50, 50)


    #Importing level
    from sindre_sitt_nivå import objects, loopable


    offset_x = 0
    scroll_area_width = 300



    #Game-loop
    run = True
    while run:
        clock.tick(FPS)
        Player1.loop(FPS)

        
        for obj in loopable:
            obj.loop()
        
        
        #Håndterer bevegelse og kollisjon
        handle_move(Player1, objects) 
        
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
