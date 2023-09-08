import pygame
class PlayerShip:
    def __init__(self, x, y, images):
        self.images = {
            "full_health": pygame.image.load(images["full_health"]),
            "slight_damage": pygame.image.load(images["slight_damage"]),
            "very_damage": pygame.image.load(images["very_damage"]),
            "damaged": pygame.image.load(images["damaged"])
        }
        self.current_image = self.images["full_health"]
        self.rect = self.current_image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1
        self.health = 100




    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < 1280:
            self.rect.move_ip(self.speed, 0)
            print(self.rect.y)

    def update_image(self):
        if self.health > 75:
            self.current_image = self.images["full_health"]
        elif 50 < self.health <= 75:
            self.current_image = self.images["slight_damage"]
        elif 25 < self.health <= 50:
            self.current_image = self.images["very_damage"]
        else:
            self.current_image = self.images["damaged"]


    def draw(self, screen):
        screen.blit(self.current_image, self.rect.topleft)