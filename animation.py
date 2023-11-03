import os
from pygame import image, transform, SRCALPHA

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

        self.factor = len(self.alive_images) / len(self.dead_images) * 5
        
    
    @classmethod
    def get_all_birds(self):

        birds = []
        types = []
        for file_name in os.listdir("birds"):
            images = os.listdir("birds" + os.sep + file_name +"/flying")
            img = image.load("birds" + os.sep + file_name +"/flying/" + images[0]).convert_alpha()
            # img = img.set_aa(pygame.SRCALPHA)
            # img = image.load(path + "/flying" + os.sep + file_name).convert_alpha()
            birds.append(transform.scale(img, (128, 100)))
            types.append(file_name)
        return birds, types
    


    

class Sprite_Animation:

    def load_images():
        red = [[],
               []]
        chicken = [['frame-1.png'],
                   []]

    def update(self):
        pass