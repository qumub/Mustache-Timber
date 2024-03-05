import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        Sprite.__init__(self, image)
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = 5 
        self.health = 100
        
    def update(self):
        self.rect.x += self.speed
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

