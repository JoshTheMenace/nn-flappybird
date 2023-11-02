import os
from pygame import image, transform

class Sprite_Collection:

    def __init__(self, folder_name) -> None:
        self.alive_images = []
        self.dead_images = []
        path = "birds/" + folder_name

        for file_name in os.listdir(path + "/flying"):
            img = image.load(path + "/flying" + os.sep + file_name).convert_alpha()
            img = transform.scale(img, (64, 50))
            self.alive_images.append(img)
        for file_name in os.listdir(path + "/hit"):
            img = image.load(path + "/hit" + os.sep + file_name).convert_alpha()
            img = transform.scale(img, (64, 50))
            self.dead_images.append(img)

        self.factor = len(self.alive_images) / len(self.dead_images)
        
    

    

class Sprite_Animation:

    def load_images():
        red = [[],
               []]
        chicken = [['frame-1.png'],
                   []]

    def update(self):
        pass