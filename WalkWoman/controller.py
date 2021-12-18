import pygame



class Controller():

    def __init__(self):
        pass    

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