import random
import pygame

def genGrid(row1,w,h,b,r): #row is list, w h and b are ints
    l = []
    l.append(row1)
    above = {}
    bStr = str(bin(r)[2:].zfill(8))
    above["111"] = int(bStr[0])
    above["110"] = int(bStr[1])
    above["101"] = int(bStr[2])
    above["100"] = int(bStr[3])
    above["011"] = int(bStr[4])
    above["010"] = int(bStr[5])
    above["001"] = int(bStr[6])
    above["000"] = int(bStr[7])
    for x in range(1,h):
        l.append([])
        for y in range(w):
            if y == 0:
                toMatch = str(l[x-1][w-1]) + str(l[x-1][0]) + str(l[x-1][1])
            elif y == w - 1:
                toMatch = str(l[x-1][w-2]) + str(l[x-1][w-1]) + str(l[x-1][0])
            else:
                toMatch = str(l[x-1][y-1]) + str(l[x-1][y]) + str(l[x-1][y+1])
            l[x].append(above[toMatch])

    return l

def genRow(s,w,f,c):
    l = []
    if f == "r": 
        random.seed(s)
        for x in range(w):
            l.append(round(random.random()))
    elif f == "f":
        for x in range(w):
            l.append(1)
    elif f == "e":
        for x in range(w):
            l.append(0)
    elif f == "o":
        for x in range(round((w-1)/2)):
            l.append(0)
        l.append(1)
        for x in range(round((w-1.5)/2)):
            l.append(0)
    elif f == "c":
        for x in range(len(c)):
            l.append(int(c[x]))
        l == c
        for x in range(w-len(c)):
            l.append(0)
            
    return l

def letter(input):
    l = ""
    if input == pygame.K_a:
        l = "a"
    elif input == pygame.K_b:
        l = "b"
    elif input == pygame.K_c:
        l = "c"
    elif input == pygame.K_d:
        l = "d"
    return l

def number(input):
    n = ""
    if input == pygame.K_0:
        n = 0
    elif input == pygame.K_1:
        n = 1
    elif input == pygame.K_2:
        n = 2
    elif input == pygame.K_3:
        n = 3
    elif input == pygame.K_4:
        n = 4
    elif input == pygame.K_5:
        n = 5
    elif input == pygame.K_6:
        n = 6
    elif input == pygame.K_7:
        n = 7
    elif input == pygame.K_8:
        n = 8
    elif input == pygame.K_9:
        n = 9
    return n
