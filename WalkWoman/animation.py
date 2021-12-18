from importlib import resources
import pygame
from WalkWoman.woman import Woman
from WalkWoman.config import Config
from WalkWoman.controller import Controller
from WalkWoman.fps_stats import Fps_stats
from WalkWoman.sound import Sound
from pygame.constants import ACTIVEEVENT, MOUSEMOTION, WINDOWENTER, WINDOWLEAVE

class Animation:

    
    
    def __init__(self):
        pass
    def run(self):
        pygame.init()
        
        self.__screen = pygame.display.set_mode(Config.get_instance().data["window"]["screen_size"])
        pygame.display.set_caption(Config.get_instance().data["window"]["animation_title"])
        with resources.path(Config.get_instance().data["window"]["background_pakage"],Config.get_instance().data["window"]["background_filename"]) as background_path:
            background = pygame.image.load(background_path).convert_alpha()
        pygame.event.set_blocked([WINDOWENTER,WINDOWLEAVE,MOUSEMOTION,ACTIVEEVENT])
       
        self.__fps_clock = pygame.time.Clock()
        self.__animation = Woman(Config.get_instance().data["sprite"]["woman_position"])
        self.__sound = Sound()
        self.__controller = Controller()
        game_over = False
        
        while game_over == False:
           for event in pygame.event.get():             
               print(event)
               if event.type == pygame.QUIT:
                   game_over = True
          
           
           self.__animation.update( self.__controller.handle_event(event) , Config.get_instance().data["sprite"]["delta_time"])
           self.__screen.fill(pygame.Color('blue'))
           self.__screen.blit(background,(0,0))
           self.__screen.blit(self.__animation.image, self.__animation.rect)
           pygame.display.flip()
           self.__sound.update_stepsound(self.__animation.rect.x) 
           self.__fps_clock.tick(8)

        pygame.quit ()
