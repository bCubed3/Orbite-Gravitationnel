import pygame
import ctypes
import sys
import time
from vector import Vector
from body import Body
import random
import math

user32 = ctypes.windll.user32
pygame.init()
# size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)  # this is the surface

sim_speed = 1
size = 0
c = (0, 0, 0)
sx = 0
sy = 0

bodies = []
sun = Body(2 * 10**30, 30, (255, 0, 0), [400, 400], [0, 0], sim_speed)
bodies.append(sun)
earth = Body(6 * 10**24, 5, (0, 255, 0), [150, 400], [0, 0.7], sim_speed)
bodies.append(earth)
super_earth = Body(6*10**26, 10, (0, 0, 255), [120, 300], [0.2, 0.5], sim_speed)
bodies.append(super_earth)
for i in range(0):
    size_t = random.randint(1, 28)
    bodies.append(Body(10**size_t, size_t,
                       (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                       [random.randint(0, width), random.randint(0, height)], [random.random(), random.random()], sim_speed))
#asteroid = Body(0.07, 3, (127, 127, 127), [149.972, 400], [0, 0], sim_speed)
#bodies.append(asteroid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sx, sy = Vector(pygame.mouse.get_pos())
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            if size > 30:
                size = 30
            size = 10**size
            if sx - x == 0 and sy - y == 0:
                bodies.append(Body(size, round(math.log(math.ceil(size), 10)) + 1, c, [sx, sy],
                                   Vector([0, 0]).vect, sim_speed))
            else :
                bodies.append(Body(size, round(math.log(math.ceil(size), 10)) + 1, c, [sx, sy],
                                   Vector([sx - x, sy - y]).norm().vect, sim_speed))
            size = 0
    screen.fill((0, 0, 0))
    if pygame.mouse.get_pressed()[0] == 1:
        size += 0.05
        pygame.draw.circle(screen, c, [sx, sy], round(math.log(math.ceil(10**size), 10)) + 1)
    for i in bodies:
        i.find_attractions(bodies)
        i.show(screen)
    #print(sun.pos.vect)

    pygame.display.flip()
    time.sleep(0.01)