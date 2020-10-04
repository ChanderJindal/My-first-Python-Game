import os
import random
import game_config as gc 
from pygame import image , transform

animals_count = dict((a,0) for a in gc.asset_files)
# in a dictionary placing the animals or chara. with initial value of 0

def available_animals():
    return [a for a,c in animals_count.items() if c < 2]

class animals:
    def __init__(self,index):
        self.index = index
        self.row = index // gc.num_titles_side
        # // is same as / (division) but returns the answer/value as that of int, even if both are of float
        self.col = index % gc.num_titles_side
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1
        self.image_path = os.path.join(gc.asset_dir,self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image,(gc.IMAGE_SIZE- 2*gc.margin,gc.IMAGE_SIZE- 2*gc.margin))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip = False