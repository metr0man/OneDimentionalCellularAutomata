import random
import pygame
import sys

#import functions
from functions import letter
from functions import number
from functions import genGrid
from functions import genRow

#paramaters
blockSize = 10
width = 192 #number of blocks across of the window
height = 108 #includes first random row
topSize = 30 #height of top box in pixels; default is 30
firstRow = "o" #r is random, f is full, e is empty, o is one block, c is custom
customRow = "00101010101" #enter 0's and 1's; the program will append 0s

pygame.init()
screen = pygame.display.set_mode([width*blockSize,topSize+height*blockSize])
font = pygame.font.SysFont("consolas", 20)

borders = 2 #2 is looping; CHANGING DOES NOTHING
seed = ""
rule = 0
slide = 0

grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)

running = True

mode = "n" #n is normal

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if mode == "n":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                mode = "s" #setting seed
        if mode == "n":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                mode = "r" #setting rule

        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            rect = pygame.Rect(0,topSize,width*blockSize,height*blockSize)
            sub = screen.subsurface(rect)
            pygame.image.save(sub,'screenshot'+str(rule)+'.png')

        #arrows
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if slide > 0:
                slide -= 1
                grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            slide += 1
            grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if rule > 0:
                rule -= 1
                grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if rule < 255:
                rule += 1
                grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
                
        elif mode == "s": #seed
            if event.type == pygame.KEYDOWN and letter(event.key) != "" and len(seed) < 8:
                seed += letter(event.key)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                mode = "n"
                grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                seed = seed[:-1]
        elif mode == 'r': #rule
            if event.type == pygame.KEYDOWN and number(event.key) != "" and len(str(rule)) < 3:
                rule = int(str(rule) + str(number(event.key)))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if rule > 255:
                    rule = 255
                mode = "n"
                slide = 0
                grid = genGrid(genRow(seed+str(slide),width,firstRow,customRow),width,height,borders,rule)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                if len(str(rule)) > 1:
                    rule = int(str(rule)[:-1])
                else:
                    rule = 0

    screen.fill((255,255,255))

    toptext = 'seed "' + seed + '" | rule ' + str(int(rule)) + ' | slide ' + str(int(slide))
    text = font.render(toptext, True, (0, 0, 0))
    screen.blit(text,(5, 5))

    #draw
    for x in range(height):
        for y in range(width):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (0,0,0), (y*blockSize, topSize+x*blockSize, blockSize, blockSize))

    pygame.display.update()

pygame.quit()
sys.exit()
