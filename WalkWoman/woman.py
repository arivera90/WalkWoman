import os
import pygame

class Woman(pygame.sprite.Sprite):
    woman_sprite_filename = ["assets", "sprites", "walking_animation.png"]
    step_sound_filename = ["assets", "sound", "walking_grass.wav"]

    def __init__(self, position):
        pygame.mixer.set_num_channels(1)  
        self.step_sound = pygame.mixer.Sound(os.path.join(*Woman.step_sound_filename))
        self.sheet = pygame.image.load(os.path.join(*Woman.woman_sprite_filename))
        self.sheet.set_clip(pygame.Rect(64, 0, 64, 128))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.right_states = { 0: (0, 0, 64, 128), 1: (64, 0, 64, 128), 2: (128, 0, 64, 128), 3: (192, 0, 64, 128),4:(256,0,64,128),5:(320,0,64,128),
                             6: (384, 0, 64, 128),7:(448,0,64,128) ,8:(512,0,64,128),9:(576,0,64,128)}
        self.left_states = { 0: (0, 128, 64, 128),1: (64, 128, 64, 128),2: (128, 128, 64, 128), 3: (192, 128, 64, 128),4:(256,128,64,128),5:(320,128,64,128),
                             6: (384, 128, 64, 128),7:(448,128,64,128) ,8:(512,128,64,128),9:(576,128,64,128)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 1
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
             if self.rect.x != 0 :
                self.clip(self.left_states)
                self.rect.x -= 8 
             else:
                 self.clip(self.left_states[0])
                 self.step_sound.stop()

        if direction == 'right':
            if self.rect.x != 576:
                self.clip(self.right_states)
                self.rect.x += 8
                
            else:
                self.clip(self.right_states[0])
                self.step_sound.stop()
        
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
       
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
     
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:          

            if event.key == pygame.K_LEFT:
                self.step_sound.play()
                self.update('left')
                
            if event.key == pygame.K_RIGHT:
                self.step_sound.play()
                self.update('right')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.step_sound.fadeout(180)
                self.update('stand_left')
                
            if event.key == pygame.K_RIGHT:
                self.step_sound.fadeout(180)
                self.update('stand_right')
               