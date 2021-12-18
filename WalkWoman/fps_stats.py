class Fps_stats:

    __max_update_time = 1000


    def __init__(self, font) -> None:
        self.__font = font
        self.__update_time = 0 
        self.__frames = 0
        pass

    def update(self, delta_time):
        self.__update_time += delta_time
        self.__frames += 1
        pass

    def render(self,surface_dst):
        pass
    def __set_fps_surface(self):
        pass