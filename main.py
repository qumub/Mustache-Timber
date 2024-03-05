import pygame
from camera import Camera
from game import Game
from input_handler import InputHandler

pygame.init()

# создание объектов 
game = Game()
input_handler = InputHandler()
input_handler.start()
player = Player(camera) 
enemy = Enemy(camera)
platform = Platform()
camera = Camera(800, 600)
player.update(camera) 
enemy.update(camera)
player_group.add(player)
enemy_group.add(enemy) 
platform_group.add(platform)

screen = pygame.display.set_mode((800, 600))

running = True
while running:
  player.handle_input(input)  

  player.update()

  player.draw()

  # обработка ввода
  game.handle_input(input_handler.get_key_buffer())
  
  # обновление состояния игры
  game.update() 
  player_group.update()
  enemy_group.update()
  platform_group.update()
  
  # отрисовка (пока просто заливка экрана)
  screen.fill((0, 0, 0))
  player_group.draw(screen)
  enemy_group.draw(screen)
  platform_group.draw(screen)


  # обновление экрана 
  pygame.display.flip()

  # выход
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False 
