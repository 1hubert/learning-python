import pygame

#pygame.init()

# setting up resolution (in a tuple)
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

# speed in x and y axis
x = 50
y = 50

# width an heigth of MC
width = 40
height = 60
vel = 5

# main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width))
    pygame.display.update()


pygame.quit()
