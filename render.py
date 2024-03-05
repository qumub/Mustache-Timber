class Renderer:

  def draw_sprites(self, sprite_group):
    sprite_group.draw(screen)
    
  def draw_background(self):  
    screen.fill((0,0,0))
