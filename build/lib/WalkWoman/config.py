from importlib import resources
import json
import os


class Config():
    __config_json_path, __config_json_filename= "WalkWoman.assets.config", "config.json"
    __instance = None

    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config()
        
        return Config.__instance
    

    def __init__(self):
        if Config.__instance is None:
            Config.__instance= self

            with resources.path(Config.__config_json_path,Config.__config_json_filename) as config_path:
                with open(config_path) as f:
                    self.data = json.load(f)
        
        else:
            raise Exception("Config cannot have multiple instances")