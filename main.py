
# Lage background
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    
    for i in range(WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            pos = [i * width, j * height]
            tiles.append(pos)
    
    return tiles, image

#Tegne background
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tuple(tile))

    pygame.display.update()


# Dette skal inn i "def main()"

background, bg_image = get_background("Blue.png")

# Inn i "while" loopen
draw(window, background, bg_image)

#Trenger ikke "BG_COLOR"
