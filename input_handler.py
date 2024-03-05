import threading

class InputHandler(threading.Thread):

  def __init__(self):
    self.key_buffer = {} # буфер нажатых клавиш

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          key = event.key
          self.key_buffer[key] = True

        if event.type == KEYUP:
          key = event.key
          self.key_buffer[key] = False
  def get_key_buffer(self):
    return self.key_buffer

  def handle_input(self):
    pass
