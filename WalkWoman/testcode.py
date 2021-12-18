#Fichero para probar cosas fuera del programa.
def create_sprite(frames,init_point,size):
            init_point_x,init_point_y= init_point
            size_x,size_y= size
            sprite_dict= {}
            for frame in range(frames):
                sprite_dict[frame]=(init_point_x+frame*size_x,init_point_y,size_x,size_y)
            return sprite_dict


right_states = create_sprite(10,(0,0),(64,128))
print("hello")

print(right_states)