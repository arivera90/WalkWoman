import pygame
import os
from WalkWoman.woman import Woman
from WalkWoman.config import Config
from WalkWoman.fps_stats import Fps_stats
from pygame.constants import ACTIVEEVENT, MOUSEMOTION, WINDOWENTER, WINDOWLEAVE

class Animation:

    background = ["WalkWoman","assets", "img", "forest.jpg"]
    
    def __init__(self):
        pass
    def run(self):
        pygame.init()
        background = pygame.image.load(os.path.join(*Animation.background))
        screen = pygame.display.set_mode(Config.get_instance().data["screen_size"])
        pygame.display.set_caption("WalkWoman")
        pygame.event.set_blocked([WINDOWENTER,WINDOWLEAVE,MOUSEMOTION,ACTIVEEVENT])
       
        clock = pygame.time.Clock()
        player = Woman(Config.get_instance().data["woman_position"])
        game_over = False
        
        while game_over == False:
           for event in pygame.event.get():             
               print(event)
               if event.type == pygame.QUIT:
                   game_over = True
           player.handle_event(event)
           screen.fill(pygame.Color('blue'))
           screen.blit(background,(0,0))
           screen.blit(player.image, player.rect)
           pygame.display.flip()
           clock.tick(12)

        pygame.quit ()
