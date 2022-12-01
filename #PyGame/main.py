import math
import random
import time
import sys

import pygame


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


pygame.init()
OKNO_X = 900
OKNO_Y = 800
s = pygame.display.set_mode((OKNO_X, OKNO_Y))

run = True

PROMIEN = 30
postac = [100, 100]
POSTAC_HP = 100
predkosc = [0, 0]
PREDKOSC_ZOMBIE = 0.4
pociski = []
zombies = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_w:
                predkosc[1] = -0.1
            elif event.key == pygame.K_a:
                predkosc[0] = -0.1
            elif event.key == pygame.K_s:
                predkosc[1] = 0.1
            elif event.key == pygame.K_d:
                predkosc[0] = 0.1

        if event.type == pygame.KEYUP:
            keys = pygame.key.get_pressed()
            if event.key == pygame.K_w:
                predkosc[1] = 0
            elif event.key == pygame.K_a:
                predkosc[0] = 0
            elif event.key == pygame.K_s:
                predkosc[1] = 0
            elif event.key == pygame.K_d:
                predkosc[0] = 0
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            n = pygame.mouse.get_pos()
            pociski.append({'start': postac.copy(), 'pos': postac.copy(), 'l': postac[0] - n[0], 'h': postac[1] - n[1], 'dis': distance(postac, (n[0], n[1])), 'prog': 0})

    # Sekcja przetwarzania
    i = 0
    for pocisk in pociski:
        pocisk['prog'] += 0.5
        pocisk['pos'][0] = pocisk['start'][0] - pocisk['l'] * pocisk['prog'] / pocisk['dis']
        pocisk['pos'][1] = pocisk['start'][1] - pocisk['h'] * pocisk['prog'] / pocisk['dis']
        if pocisk['pos'][0] > OKNO_X or pocisk['pos'][0] < 0:
            pociski.pop(i)
        elif pocisk['pos'][1] > OKNO_Y or pocisk['pos'][1] < 0:
            pociski.pop(i)
        for zombie in zombies:
            if distance(zombie['pos'], pocisk['pos']) < 30:
                pociski.pop(i)
                zombie['hp'] -= 1
        i += 1
    if not (postac[0] + predkosc[0] + PROMIEN >= OKNO_X or postac[0] + predkosc[0] <= 0 + PROMIEN):
        postac[0] += predkosc[0]
    if not (postac[1] + predkosc[1] + PROMIEN >= OKNO_Y or postac[1] + predkosc[1] <= 0 + PROMIEN):
        postac[1] += predkosc[1]
    if not (POSTAC_HP >= 100):
        POSTAC_HP += 0.1
    if POSTAC_HP == 0:
        time.sleep(1)
        sys.exit()

    if random.randint(0, 2000) == 1:
        if random.randint(0, 1):
            x = -random.randint(50, 100)
        else:
            x = -random.randint(OKNO_X, OKNO_X+100)
        if random.randint(0, 1):
            y = -random.randint(50, 100)
        else:
            y = -random.randint(OKNO_Y, OKNO_Y+100)
        
        zombies.append({'pos': [x, y], 'hp': 3})
    
    i = 0
    for zombie in zombies:
        if zombie['pos'][0] > postac[0]:
            zombie['pos'][0] -= PREDKOSC_ZOMBIE
        else:
            zombie['pos'][0] += PREDKOSC_ZOMBIE
        if zombie['pos'][1] > postac[1]:
            zombie['pos'][1] -= PREDKOSC_ZOMBIE
        else:
            zombie['pos'][1] += PREDKOSC_ZOMBIE
        if zombie['hp'] <= 0:
            zombies.pop(i)
        if distance(zombie['pos'], postac) < 55:
            POSTAC_HP -= 1
    i += 1

    # Sekcja renderowania
    s.fill((255, 255, 255))
    for pocisk in pociski:
        pygame.draw.circle(s, pygame.Color('black'), pocisk['pos'], 4)
    for zombie in zombies:
        pygame.draw.circle(s, (0, 255, 0), zombie['pos'], 30)
    pygame.draw.circle(s, (255, 0, 0), postac, PROMIEN)
    pygame.draw.line(s, (255, 0, 0), [20, 20], [POSTAC_HP, 20], 10)
    pygame.display.flip()
