# https://www.moodle.3zy.pl/course/view.php?id=3
import pygame as p

p.init()

s = p.display.set_mode((500, 500))

run = True

while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        if event.type == p.MOUSEBUTTONDOWN:
            print(p.mouse.get_pos())
    s.fill((22, 155, 155))
    p.draw.rect(s, (0, 255, 0), (200, 200, 100, 100))
    p.draw.circle(s, (255, 0, 0), (250, 250), 50)
    p.draw.line(s, (0, 0, 255), (200, 200), (300, 300), 5)
    p.display.flip()
