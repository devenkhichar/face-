import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))


mouth=pygame.Rect(100,200,200,200)

eye1=pygame.Rect(110,220,20,20)

eye2=pygame.Rect(110,260,20,20)

mouth=pygame.Rect(200,230,10,140)

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.typepygame.QUIT:
            pygame.quit()
            sys.exit()
         
    pygame.draw.rect(screen,(120,120,120),face)  
    pygame.draw.rect(screen,(255,0,0),eye1)
    pygame.draw.rect(screen,(255,0,0),eye2)
    pygame.draw.rect(screen,(200,200,200),mouth)
    
pygame.display.update()
clock.tick(30)



