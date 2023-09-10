import pygame
import random
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
velocity_x=0
velocity_y=0
size_snake=10
score=0
food_x=random.randint(0,1200)
food_y=random.randint(0,500)
fps=30
pygame.draw.rect(game_window,black,[food_x,food_y,size_snake,size_snake])
while not exit_game :
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit_game=True
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        velocity_x=-10
        velocity_y=0
      if event.key==pygame.K_RIGHT:
        velocity_x=10
        velocity_y=0
      if event.key==pygame.K_UP:
        velocity_y=-10
        velocity_x=0
      if event.key==pygame.K_DOWN:
       velocity_y=10
       velocity_x=0

  snake_x=snake_x+ velocity_x
  snake_y=snake_y+ velocity_y
  game_window.fill(white)
  
  if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
    score +=1
    print("score: ",score)
    food_x=random.randint(0,1200)
    food_y=random.randint(0,500)
  pygame.draw.rect(game_window,red,[food_x,food_y,size_snake,size_snake])
  pygame.draw.rect(game_window,black,[snake_x,snake_y,size_snake,size_snake])
  pygame.display.update()
  clock.tick(fps)
  
  