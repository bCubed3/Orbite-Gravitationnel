import pygame
import ctypes
import sys
import time
from vector import Vector

user32 = ctypes.windll.user32
pygame.init()
# size = width, height = round(user32.GetSystemMetrics(0) / 1.3), round(user32.GetSystemMetrics(1) / 1.3)
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)  # this is the surface



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

    pygame.display.flip()
    time.sleep(0.001)