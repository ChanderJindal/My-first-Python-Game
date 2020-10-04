import os
#some basic declarations
IMAGE_SIZE = 128
SCREEN_SIZE = 512
num_titles_side = 4
num_titles_total = 16
margin = 8

asset_dir = 'assets'
asset_files = [x for x in os.listdir(asset_dir) if x[-3:].lower() == 'png'] # checking so that all are images png type
# loading in the images from 'assets'
assert len(asset_files) == 8
# reassuring that we have our 8 images