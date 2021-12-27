from importlib import resources
from WalkWoman.config import Config
import pygame


class Woman(pygame.sprite.Sprite):
    ''' Clase que se encarga de gestionar la animación del personaje'''

    def __init__(self,position):
      
        with resources.path(Config.get_instance().data["woman"]["woman_sprite_pakage"],Config.get_instance().data["woman"]["woman_sprite_filename"]) as sprite_path:
            self.__sheet = pygame.image.load(sprite_path).convert_alpha()

        self.__sheet.set_clip(pygame.Rect(Config.get_instance().data["woman"]["frames_right_init"],Config.get_instance().data["woman"]["frames_right_size"]))
        self.__image = self.__sheet.subsurface(self.__sheet.get_clip())
        self.rect = self.__image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.__count = 0
      
        
        def __create_sprite(frames,init_point,size):
             init_point_x,init_point_y= init_point
             size_x,size_y= size
             sprite_dict= {}
             for frame in range(frames):
                sprite_dict[frame]=(init_point_x+frame*size_x,init_point_y,size_x,size_y)
             return sprite_dict

        self.__right_states = __create_sprite(Config.get_instance().data["woman"]["frames_right"],Config.get_instance().data["woman"]["frames_right_init"],Config.get_instance().data["woman"]["frames_right_size"])
        
        self.__left_states = __create_sprite(Config.get_instance().data["woman"]["frames_left"],Config.get_instance().data["woman"]["frames_left_init"],Config.get_instance().data["woman"]["frames_left_size"])
        

    def __get_frame(self, frame_set):
            self.frame += 1
            if self.frame > (len(frame_set) - 1):
                self.frame = 1
            return frame_set[self.frame]

    def __clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.__sheet.set_clip(pygame.Rect(self.__get_frame(clipped_rect)))
        else:
            self.__sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self,direction,delta_time):

        if self.__count == delta_time:
            if direction == 'left':
                if self.rect.x >= 0 :
                    self.__clip(self.__left_states)
                    self.rect.x -= Config.get_instance().data["woman"]["distance"]*delta_time
                else:
                 self.__clip(self.__left_states[0])    
                   
            if direction == 'right':
           
                if self.rect.x <= Config.get_instance().data["window"]["screen_size"][0] - Config.get_instance().data["woman"]["frames_right_size"][0]:
                    self.rect.x += Config.get_instance().data["woman"]["distance"]*delta_time              
                    self.__clip(self.__right_states)           
                else:
                    self.__clip(self.__right_states[0])       

            if direction == 'stand_left':
                self.__clip(self.__left_states[0])
            if direction == 'stand_right':
                self.__clip(self.__right_states[0])
        
            self.__image = self.__sheet.subsurface(self.__sheet.get_clip())
            self.__count = 0
        else:
            self.__count +=1    
               

    def render(self,dst_screen,background):
        dst_screen.fill(pygame.Color('blue'))
        dst_screen.blit(background,(0,0))
        dst_screen.blit(self.__image,self.rect)
        

    
               
               
   
