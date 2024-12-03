import pygame
from Player import Player
from Block import Block
from Fire import Fire
from Spike import Spike
from Fan import Fan
from FallingPlatform import Falling_platform
from Spikehead import Spikehead
from Trampoline import Trampoline
from sprite_functions import *
from movement_functions import *
from Button import Button
pygame.init()

heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart,(40,40))
pygame.display.set_caption("Platformer")


WIDTH, HEIGHT = 1200, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
background, bg_image = get_background("Yellow.png", WIDTH, HEIGHT)

objects = []
loopable = []

def show_start_menu():

    global objects, loopable

    button = Button("Play", 100, 100)
    
    #Knapp for å begynne spillet
    start_knapp_font = pygame.font.SysFont("times new roman", 50)
    start_knapp_tekst = start_knapp_font.render("START SPILLET", True, (0, 0, 255))
    start_knapp = start_knapp_tekst.get_rect(center=(390, 340))

    window.blit(start_knapp_tekst, start_knapp)
    pygame.display.flip()


    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_knapp.collidepoint(mouse_pos):
                    waiting = False
                    from sindre_sitt_nivå import objects, loopable



def main(window):


    clock = pygame.time.Clock()
    block_size = 96
    
    
    
    #Making player
    Player1 = Player(100, 100, 50, 50)


    #Importing level
    


    offset_x = 0
    scroll_area_width = 400

    show_start_menu()

    #Game-loop
    run = True
    while run:
        clock.tick(FPS)
        Player1.loop(FPS)


        if Player1.rect.centery >= (HEIGHT + 200) or Player1.lives <= 0:
            offset_x = Player1.spawn_x - (WIDTH/2)
            Player1.respawn()
        
        for obj in loopable:
            obj.loop()
        
        #print(Player1.x_vel)
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
        if ((Player1.rect.right - offset_x >= WIDTH - scroll_area_width and (Player1.x_vel + Player1.conveyor_speed) > 0) or (Player1.rect.left - offset_x <= scroll_area_width and (Player1.x_vel + Player1.conveyor_speed) < 0)):
            offset_x += Player1.x_vel + Player1.conveyor_speed


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
