from contextlib import nullcontext
from WalkWoman.config import Config
import pygame



class FPS():
    '''Clase para monitorizar los FPS a los que se esta ejecutando la aplicación'''
    
    def __init__(self) :
        self.__font = pygame.font.SysFont("Arial", 50)
        self.__none = self.__font.render ("",1, pygame.Color("Blue"))

    def fps(self,clock):
        if Config.get_instance().data["fps_counter"]["enable"] == True :
            fr =  "Fps: " + str(int(clock.get_fps()))
            frt = self.__font.render(fr, 1, pygame.Color(Config.get_instance().data["fps_counter"]["color"]))
            return frt
        else:
            return self.__none