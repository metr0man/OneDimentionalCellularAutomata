import pygame
import sys
import random

# import functions
from functions2 import genGrid

# paramaters
blockSize = 10  # size of the blocks in pixels
width = 192  # number of blocks across of the window
height = 108  # includes first random row
firstRow = "one"  # random or one

# new params
colors = 3  # num colors, colors are from palette
above = 3  # number of cells above to consider
assert above % 2 == 1  # make sure odd
palette = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# setup pygame
pygame.init()
screen = pygame.display.set_mode([width * blockSize, height * blockSize])
font = pygame.font.SysFont("consolas", 20)

seed = ""
rule = 0
slide = 0

ruleBound = colors ** (colors ** above)
print(f"number of possible rules: { ruleBound }")

running = True
while running:
    for event in pygame.event.get():  # get keys
        # quit if escape of x out
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # check for input keys
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:  # screenshot on k
            rect = pygame.Rect(0, 0, width * blockSize, height * blockSize)
            sub = screen.subsurface(rect)
            pygame.image.save(sub, f"screenshots/a{ above }c{ colors }r{ rule }.png")  # todo this str
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            rule = random.randrange(ruleBound)
        # arrow keys
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if slide > 0:
                slide -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            slide += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if rule > 0:
                rule -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if rule + 1 < ruleBound:
                rule += 1

    # update grid
    grid = genGrid(rule, seed, slide, colors, above, width, height, firstRow)

    # top bar info
    toptext = 'seed "' + seed + '" | rule ' + str(int(rule)) + ' | slide ' + str(int(slide))
    pygame.display.set_caption(toptext)

    # draw
    for x in range(height):
        for y in range(width):
            pygame.draw.rect(screen, palette[grid[x][y]], (y * blockSize, x * blockSize, blockSize, blockSize))
    pygame.display.update()

pygame.quit()
sys.exit()
