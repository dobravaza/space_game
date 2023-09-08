import pygame
from pygame.locals import *
from PlayerShip import PlayerShip
# Inicjalizacja pygame
pygame.init()

# Ustawienia ekranu
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kosmiczna Obrona")
###############################################






#SHIP
SHIP_X = 400
SHIP_Y = 200
#images
player_ship_images = {
    "full_health": "assets/ships/full_health.png",
    "slight_damage": "assets/ships/slight_demage.png",
    "very_damage": "assets/ships/very_damage.png",
    "damaged": "assets/ships/damaged.png"
}
player_ship = PlayerShip(SHIP_X, SHIP_Y, player_ship_images)
############################################################3
# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_ship.move_left()

    if keys[K_RIGHT]:
        player_ship.move_right()

    screen.fill((0, 0, 0))  # Wypełnienie ekranu kolorem czarnym
    # warship
    # rysowanie
    player_ship.draw(screen)



    pygame.display.flip()

pygame.quit()
