import pygame
import os
from WalkWoman.woman import *

class Animation:

    background = ["assets", "img", "forest.jpg"]
    
    def __init__(self):
        pass
    def run(self):
        pygame.init()
        ancho_ventana = 640
        alto_ventana = 480
        background = pygame.image.load(os.path.join(*Animation.background))
        screen = pygame.display.set_mode([ancho_ventana, alto_ventana],0,32)
        pygame.display.set_caption("WalkWoman")
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()
        player = Woman((ancho_ventana/2, 307))
        game_over = False
        
        while game_over == False:
           for event in pygame.event.get():             
  
               if event.type == pygame.QUIT:
                   game_over = True
           player.handle_event(event)
           screen.fill(pygame.Color('blue'))
           screen.blit(background,(0,0))
           screen.blit(player.image, player.rect)
           pygame.display.flip()
           clock.tick(12)

        pygame.quit ()
