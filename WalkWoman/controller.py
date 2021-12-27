import pygame

class Controller():
    ''' Clase que analiza las teclas que se pulsan y devuelve hacia donde debe moverse el personaje'''

    def __init__(self):
        self.__value=0
        self.__previus_position = "stand_right"
        
     
    def handle_event(self, event):     
        
        if event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_LEFT:
               return 'left'   
            if event.key == pygame.K_RIGHT:
               return 'right'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:           
                return 'stand_left'  
            if event.key == pygame.K_RIGHT:
                return 'stand_right'
