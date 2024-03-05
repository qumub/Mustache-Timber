# Импорты
import pygame
from sprite import Sprite 
from player import Player
from enemy import Enemy

# Инициализация 
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Создание объектов
player = Player()
enemy = Enemy() 

# Группы спрайтов
all_sprites = pygame.sprite.Group()
all_sprites.add(player) 
all_sprites.add(enemy)

# Цикл игры
running = True 
while running:

  # Обработка событий
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Обновление состояния    
  all_sprites.update()  
  
  # Отрисовка
  screen.fill((0,0,0))
  all_sprites.draw(screen)

  pygame.display.flip()
  
