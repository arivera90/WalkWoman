from importlib import resources
from WalkWoman.config import Config
import pygame


class Sound():
    '''Clase que se encarga de gestionar todo el sonido de la aplicación'''

    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        with resources.path(Config.get_instance().data["sound"]["walk_sound_pakage"],Config.get_instance().data["sound"]["walk_sound_filename"]) as effect1_path:
            self.__effect1 = pygame.mixer.Sound(effect1_path)
        with resources.path(Config.get_instance().data["sound"]["background_music_pakage"],Config.get_instance().data["sound"]["background_music_filename"]) as background_music_path:
            pygame.mixer.music.load(background_music_path)
            self.__previous_position_x = Config.get_instance().data["woman"]["woman_position"][0]
            self.__step_cadency = Config.get_instance().data["sound"]["walk_sound_cadency"] * Config.get_instance().data["woman"]["delta_time"]
              
        
        pygame.mixer.music.set_volume(Config.get_instance().data["sound"]["background_music_volume"])  
        pygame.mixer.music.play(-1)

    def update_stepsound(self,position):

        pygame.mixer.Channel(0).set_volume( abs(-Config.get_instance().data["window"]["screen_size"][0] + position)/1000 , abs(position)/1000)

        if position <= (self.__previous_position_x - self.__step_cadency) or position >= (self.__previous_position_x + self.__step_cadency):
       
           pygame.mixer.Channel(0).play(self.__effect1)
           self.__previous_position_x = position
        
              