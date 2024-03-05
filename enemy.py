import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.speed = 2
        self.damage = 1
        
        # тип врага (наземный, летающий и т.д.)
        self.type = type
        
        # анимации 
        self.animations = {}
        
        # текущая анимация
        self.animation = None 
        
    def move(self):
        if self.type == "ground":
            pass# логика движения по земле
        
        if self.type == "flying":
            pass# логика полета
            
        self.x += self.speed
        self.animate()
            
    def animate(self):
       pass# смена кадров текущей анимации
        
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()
            
    def die(self):
        # взрыв, анимация смерти
        pass
