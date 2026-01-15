# FIRST PYGAME LAB/SQUARE CHASING GAME
__AUTHOR__ = "JACKSON_DEL_GAIZO"
__VERSION__ = "1-15-2026"



import random


import pygame

def main():
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    # Before the loop: create speed variables
    speed_x = random.randint(-2, 2)
    if speed_x == 0:
        speed_x = 1
    speed_y = random.randint(-2, 2)
    if speed_y == 0:
        speed_y = 1
    size = (1000, 800)

    # intialize the Pygame engine
    pygame.init()
    clock = pygame.time.Clock()

    # setup the screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("my first game")
    # keep the animation loop going
    running = True
    # this is a Rect object in Pygame -- draw to the screen
    rect = pygame.Rect(random.randint(0, size[0] - 100), random.randint(0, size[1] - 100), 100, 100)
    playerRect = pygame.Rect((size[0] - 10) / 2, (size[1] - 10) / 2, 20, 20)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # this code processes key movement with the small rect object
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            playerRect.move_ip(0, -1)
        if keys[pygame.K_s]:
            playerRect.move_ip(0, 1)
        if keys[pygame.K_a]:
            playerRect.move_ip(-1, 0)
        if keys[pygame.K_d]:
            playerRect.move_ip(1, 0)
        playerRect.clamp_ip(screen.get_rect())
        # 0-255 2^8 = RGB 0000 0000 1111 1111
        # if
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, GREEN, playerRect)
        pygame.display.flip()
        # Update position (move the rect)
        rect.x += speed_x
        rect.y += speed_y

        if rect.x > size[0] - 100 or rect.x < 0:
            speed_x *= -1
        if rect.y > size[1] - 100 or rect.y < 0:
            speed_y *= -1
        clock.tick(180)
        if playerRect.colliderect(rect):
            running = False
    running = True
    font = pygame.font.SysFont("Bold", 20)  # 20=size
    text_surface = font.render("Gameover, click to quit", True, RED)
    text_rect = text_surface.get_rect(centerx=size[0] / 2, centery=size[1] / 2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.fill(BLACK)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # symbolic constants




