import pygame
import ctypes
import sys
import time
from vector import Vector
from body import Body

user32 = ctypes.windll.user32
pygame.init()
# size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)  # this is the surface


bodies = []
sun = Body(2000000, 30, (255, 0, 0), [400, 300], [0, 0])
bodies.append(sun)
earth = Body(6, 10, (0, 255, 0), [300, 300], [0, -0.7])
bodies.append(earth)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    for i in bodies:
        i.find_attractions(bodies)
        i.show(screen)
    print(sun.pos.vect)

    pygame.display.flip()
    time.sleep(0.0001)