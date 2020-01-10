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

sim_speed = 10

bodies = []
sun = Body(2 * 10**30, 30, (255, 0, 0), [400, 300], [0, 0], sim_speed)
bodies.append(sun)
earth = Body(6 * 10**24, 3, (0, 255, 0), [300, 300], [0, -0.3], sim_speed)
bodies.append(earth)
asteroid = Body(0.07, 3, (127, 127, 127), [290, 300], [0, 0], sim_speed)
#bodies.append(asteroid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #screen.fill((0, 0, 0))
    for i in bodies:
        i.find_attractions(bodies)
        i.show(screen)
    print(sun.pos.vect)

    pygame.display.flip()
    time.sleep(0.0001)