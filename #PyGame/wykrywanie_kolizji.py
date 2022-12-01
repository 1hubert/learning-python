# Kod powstał w ramach serii poradników dotyczących programowania w PyGame
# Materiały dodatkowe dostępne są pod adresem:
# https://www.moodle.3zy.pl/course/view.php?id=3

import pygame
import random
import math


def distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)


pygame.init()

s = pygame.display.set_mode((500, 500))
run = True
targets = []
while run:
    if random.randint(0, 5000) == 1:
        target = {"loc": [random.randint(0, 500), random.randint(0, 500)],
                  "direction": random.choice((True, False))}
        targets.append(target)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            i = 0
            for target in targets:
                if distance(target['loc'], mouse) < 30:
                    targets.pop(i)
                    break
                i += 1
    for target in targets:
        if target['loc'][0] < 0:
            target['direction'] = True
        elif target['loc'][0] > 500:
            target['direction'] = False
        if target['direction']:
            target['loc'][0] += 0.01
        else:
            target['loc'][0] -= 0.01
    s.fill((255, 255, 255))
    for target in targets:
        pygame.draw.circle(s, (255, 0, 0), target["loc"], 30)
    pygame.display.flip()
