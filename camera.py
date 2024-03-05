import pygame
class Camera:

    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.x = 0
        self.y = 0
        
    def update(self, target):
        self.x = -target.rect.x + SCREEN_WIDTH / 2
        self.y = -target.rect.y + SCREEN_HEIGHT / 2 
        
    def apply(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y