from importlib import resources
from pygame.constants import ACTIVEEVENT, MOUSEMOTION, WINDOWENTER, WINDOWLEAVE
from WalkWoman.config import Config
from WalkWoman.controller import Controller
from WalkWoman.sound import Sound
from WalkWoman.woman import Woman
from WalkWoman.fps_stats import FPS
import pygame

class Animation:
   
    
    def __init__(self):
        pass
    def run(self):
        '''La función run ejecuta el bucle principal del programa'''
    
        pygame.init()
        self.__screen = pygame.display.set_mode(Config.get_instance().data["window"]["screen_size"])
        pygame.display.set_caption(Config.get_instance().data["window"]["animation_title"])
        with resources.path(Config.get_instance().data["window"]["background_pakage"],Config.get_instance().data["window"]["background_filename"]) as background_path:
            self.__background = pygame.image.load(background_path).convert_alpha()
        pygame.event.set_blocked([WINDOWENTER,WINDOWLEAVE,MOUSEMOTION,ACTIVEEVENT])
       
        self.__fps_clock = pygame.time.Clock()
        self.__animation = Woman(Config.get_instance().data["woman"]["woman_position"])
        self.__controller = Controller()
        self.__sound = Sound()
        self.__fps= FPS()
        self.__run = False
        
        while self.__run == False:
           for event in pygame.event.get():             
                if event.type == pygame.QUIT:
                   self.__run = True

           self.__animation.update( self.__controller.handle_event(event) ,Config.get_instance().data["woman"]["delta_time"])
           self.__animation.render(self.__screen,self.__background)
           self.__screen.blit(self.__fps.fps(self.__fps_clock),Config.get_instance().data["fps_counter"]["position"])
           pygame.display.flip()       
           self.__sound.update_stepsound(self.__animation.rect.x) 
           self.__fps_clock.tick(Config.get_instance().data["window"]["tick"])
        pygame.quit ()
