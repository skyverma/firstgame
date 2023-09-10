import pygame
x=pygame.init()
#Creating window
game_window=pygame.display.set_mode((1200,500))
pygame.display.set_caption('MY first game')
pygame.display.update()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
clock=pygame.time.Clock()
#creating variables
exit_game=False
game_over= False
snake_x=45
snake_y=55
size_snake=10
fps=30
while not exit_game :
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit_game=True
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_RIGHT:
        nake_x=snake_x+10
      if event.key==pygame.K_LEFT:
        snake_x=snake_x-10
      if event.key==pygame.K_DOWN:
        size_snake=snake_y+10
      if event.key==pygame.K_LEFT:
       snake_y=snake_y-10


  game_window.fill(white)
  pygame.draw.rect(game_window,black,[snake_x,snake_y,size_snake,size_snake])
  pygame.display.update()
  clock.tick(fps)
  
  