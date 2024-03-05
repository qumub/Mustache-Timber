import pygame
from constants import Constants

class Player(pygame.sprite.Sprite):
    
    def __init__(self, camera):
        self.camera = camera
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()  
        self.rect.center = (400, 300)
        self.speed = 5


    def update(self):
        self.camera.update(self)
        GRAVITY = Constants.GRAVITY
        TERMINAL_VELOCITY = Constants.TERMINAL_VELOCITY
        self.rect.x += 1
        self.velocity += self.acceleration
        self.velocity.y += GRAVITY
        if self.velocity.y > TERMINAL_VELOCITY:
            self.velocity.y = TERMINAL_VELOCITY

    
    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed 
        
    def jump(self):
        pass # будет добавлено позже
       
            
    def take_damage(self):
        self.lives -= 1
        if self.lives == 0:
            self.die()
            
    def die(self):
        # логика смерти игрока
        pass
        