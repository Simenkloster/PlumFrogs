import pygame
from Player import Player
from sprite_functions import *
from movement_functions import *
pygame.init()

menuBackground = pygame.image.load('./assets/Background/MenuBackground.jpg')
menuBackground = pygame.transform.scale(menuBackground, (1200, 800))

playButtonImage = pygame.image.load("./assets/Menu/Buttons/PlayButton.png")
playButtonImage = pygame.transform.scale(playButtonImage, (95, 95))

restartButtonImage = pygame.image.load("./assets/Menu/Buttons/Restart.png")
restartButtonImage = pygame.transform.scale(restartButtonImage, (50, 50))
restartButtonImageRect = restartButtonImage.get_rect()
restartButtonImageRect.topright =(1180, 20)


playButtonRect_simen = playButtonImage.get_rect()
playButtonRect_simen.topleft = (300, 150+25)

playButtonRect_mikkel = playButtonImage.get_rect()
playButtonRect_mikkel.topleft = (300, 275+25)


playButtonRect_kjølv = playButtonImage.get_rect()
playButtonRect_kjølv.topleft = (300, 400+25)


playButtonRect_kristoffer = playButtonImage.get_rect()
playButtonRect_kristoffer.topleft = (300, 525+25)


playButtonRect_sindre = playButtonImage.get_rect()
playButtonRect_sindre.topleft = (300, 650+25)




heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart,(40,40))
pygame.display.set_caption("Platformer")




WIDTH, HEIGHT = 1200, 800
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
background, bg_image = get_background("Yellow.png", WIDTH, HEIGHT)

objects = []
loopable = []

menuActive = True
gameActive = False

def show_start_menu():

    global objects, loopable, gameActive, menuActive

    start_meny_font = pygame.font.Font('./Fonts/DigitalArcade.ttf', 120)
    levelbutton_font = pygame.font.Font('./Fonts/ARCADECLASSIC.TTF', 60)
    start_meny_text = start_meny_font.render('PlumFrogs Platformer', True, (0,0,0))

    simen_text = levelbutton_font.render('Simens     level', True, (0,0,0))
    mikkel_text = levelbutton_font.render('Mikkels      level', True, (0,0,0))
    kjølv_text = levelbutton_font.render('Kjølvs       level', True, (0,0,0))
    kristoffer_text = levelbutton_font.render('Kristoffers      level', True, (0,0,0))
    sindre_text = levelbutton_font.render('Sindres      level', True, (0,0,0))




    if menuActive:
        window.blit(menuBackground, (0,0))
        window.blit(start_meny_text, (20, 50))

        window.blit(simen_text, (440, 195))
        window.blit(mikkel_text, (440, 320))
        window.blit(kjølv_text, (440, 445))
        window.blit(kristoffer_text, (440, 570))
        window.blit(sindre_text, (440, 695))

 

        window.blit(playButtonImage, playButtonRect_simen)
        window.blit(playButtonImage, playButtonRect_mikkel)
        window.blit(playButtonImage, playButtonRect_kjølv)
        window.blit(playButtonImage, playButtonRect_kristoffer)
        window.blit(playButtonImage, playButtonRect_sindre)


        pygame.display.flip()
        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if playButtonRect_simen.collidepoint(mouse_pos):
                        waiting = False
                        from Simen_testnivå import objects, loopable
                        gameActive = True
                        menuActive = False
                    
                    if playButtonRect_mikkel.collidepoint(mouse_pos):
                        waiting = False
                        from mi_level import objects, loopable
                        gameActive = True
                        menuActive = False
                    
                    if playButtonRect_kjølv.collidepoint(mouse_pos):
                        waiting = False
                        from kj_level import objects, loopable
                        gameActive = True
                        menuActive = False

                    if playButtonRect_kristoffer.collidepoint(mouse_pos):
                        waiting = False
                        from kristoffersittlevel import objects, loopable
                        gameActive = True
                        menuActive = False
                    if playButtonRect_sindre.collidepoint(mouse_pos):
                        waiting = False
                        from sindre_sitt_nivå import objects, loopable
                        gameActive = True
                        menuActive = False



def main(window):

    global objects, loopable, gameActive, menuActive

    clock = pygame.time.Clock()
    block_size = 96
    
    
    
    #Making player
    Player1 = Player(100, 100, 50, 50)




    offset_x = 0
    offset_y = 0
    scroll_area_width = 400
    scroll_area_height = 200

    show_start_menu()

    #Game-loop
    while gameActive:
        clock.tick(FPS)
        Player1.loop(FPS)

        print(Player1.finishedLevelStatus)

        if Player1.finishedLevelStatus == True:
            gameActive = False
            menuActive = True
            Player1.finishedLevelStatus = False
            show_start_menu()
            Player1.respawn()
            offset_x = Player1.spawn_x - (WIDTH/2)
            if Player1.spawn_y <= 0:
                offset_y = Player1.spawn_y


        if Player1.rect.centery >= (HEIGHT + 200) or Player1.lives <= 0:
            offset_x = Player1.spawn_x - (WIDTH/2)
            if Player1.spawn_y <= 0:
                offset_y = Player1.spawn_y
            Player1.respawn()
        
        for obj in loopable:
            obj.loop()
        
        #print(Player1.x_vel)
        #Håndterer bevegelse og kollisjon
        handle_move(Player1, objects) 
        
        #Tegner opp alt
        draw(window, background, bg_image, Player1, objects, offset_x,offset_y)
        window.blit(restartButtonImage, restartButtonImageRect)

        
        dynamic_x = 0
        for i in range(Player1.lives):
            dynamic_x+=45
            window.blit(heart,(dynamic_x,30))
        if Player1.lives == 0:
            offset_x = 0
            offset_y = 0


        
        pygame.display.update()


        #Sjekker hvor spilleren er på skjermen og flytter kameraet
        if ((Player1.rect.right - offset_x >= WIDTH - scroll_area_width and (Player1.x_vel + Player1.conveyor_speed) > 0) or (Player1.rect.left - offset_x <= scroll_area_width and (Player1.x_vel + Player1.conveyor_speed) < 0)):
            offset_x += Player1.x_vel + Player1.conveyor_speed

        if ((Player1.rect.top - offset_y >= HEIGHT - scroll_area_height) and Player1.y_vel > 0 ) or ((Player1.rect.bottom - offset_y <= scroll_area_height) and Player1.y_vel < 0):
            offset_y += Player1.y_vel
            if offset_y > 0:
                offset_y = 0





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
                menuActive = True
                Player1.finishLevel()
                
                show_start_menu()
                offset_x = Player1.spawn_x - (WIDTH/2)
                if Player1.spawn_y <= 0:
                    offset_y = Player1.spawn_y
                Player1.respawn()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and Player1.jump_count < 2:
                    Player1.jump()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restartButtonImageRect.collidepoint(mouse_pos):
                    Player1.respawn()
                    offset_x = Player1.spawn_x - (WIDTH/2)
                    if Player1.spawn_y <= 0:
                        offset_y = Player1.spawn_y

                    

    
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
