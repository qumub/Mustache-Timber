import pygame
from constants import Constants

class Player(pygame.sprite.Sprite):
    
    speed = 5 
    direction = 0 # 0 - стоит, 1 - вправо, -1 - влево
    
    def __init__(self, camera):
        self.camera = camera
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()  
        self.rect.center = (400, 300)
        self.speed = 5

    def handle_input(input):
        if input.right:
            direction = 1  
        if input.left:
            direction = -1
        if input.up:
            self.dy = -JUMP_POWER 
            self.y += self.dy
            self.dy += GRAVITY 
        if input.no_key_pressed:
            direction = 0

    def update(self):
        self.camera.update(self)
        self.y += self.dy
        GRAVITY = Constants.GRAVITY
        TERMINAL_VELOCITY = Constants.TERMINAL_VELOCITY
        if direction == 1:
            self.x += speed
        if direction == -1: 
            self.x -= speed
        if self.on_ground() and self.dy > 0:
            # Воспроизвести анимацию приземления
            self.play_landing_animation()
            self.dy = 0
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
       
    def on_ground(self):
        pass
    
    def play_landing_animation(self):
        # Проиграть анимацию приземления
        pass

    def take_damage(self):
        self.lives -= 1
        if self.lives == 0:
            self.die()
            
    def die(self):
        # логика смерти игрока
        pass

    def draw(self, screen):
        pass

        