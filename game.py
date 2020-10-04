import pygame
import game_config as gc
#mport chara
from pygame import display , event , image
from chara import animals
from time import sleep
#import time
def find_index(x,y):
    row = y//gc.IMAGE_SIZE
    col =  x//gc.IMAGE_SIZE
    index = gc.num_titles_side*row + col
    return index

pygame.init()

display.set_caption('Our DCMK Game') #stuff to put in title of game window

screen = display.set_mode((gc.SCREEN_SIZE,gc.SCREEN_SIZE)) # enter value in tuplets

matched = image.load('other_assets/matched.png')
"""
screen.blit(matched,(0,0)) #blit method displays image over other image/screen
display.flip() #it shows the updated image from above
"""

running = True
tiles = [animals(i) for i in range(0,gc.num_titles_total)]

current_images = []

while running:
    current_events = event.get() # to get the previous command/itteration
 
    for current in current_events:
        if current.type == pygame.QUIT:
            running = False # to end the game

        if current.type == pygame.KEYDOWN: # this way can use keyboard to interact with game
            if current.key == pygame.K_ESCAPE: 
                running = False

        if current.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(mouse_x,mouse_y)
            index = find_index(mouse_x,mouse_y)
            #print(index)
            if index in current_images:
                current_images.remove(index)
            else :
                if len(current_images) > 1:
                    current_images = current_images[1:]
                current_images.append(index)


    screen.fill((255,255,255)) # 255 is rgb 255 white color
    total_found = 0 
    for i,tile in enumerate(tiles):
        
        image_i = tile.image if i in current_images else tile.box
        # i can be replaced by tile.index but enumerate returns tuplets
        # ps try it with range
        if tile.skip  : total_found += 1
        else :
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.margin,gc.margin + tile.row * gc.IMAGE_SIZE))
            # change image_i to tile.image to see all the images face up
            # if matched then skip it algo.c
    display.flip()
    if len(current_images) == 2:
        index_1,index_2 = current_images
        if tiles[index_1].name == tiles[index_2].name:
            tiles[index_2].skip = True
            tiles[index_1].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images = []
    

    if total_found == len(tiles):
        running = False


print("That's all folks!") # message after the game has ended which comes in cmd prompt