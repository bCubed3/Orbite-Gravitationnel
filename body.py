from vector import Vector
import pygame

class Body:
    def __init__(self, mass, size, color, pos, velocity, sim_speed):
        self.mass = mass
        self.size = size
        self.color = color
        self.pos = Vector(pos) # this should be a vector
        self.velocity = Vector(velocity) * mass # this should be a vector
        self.G = 6.674 * 10**-30
        self.sim_speed = sim_speed

    def find_attractions(self, bodies):
        for body in bodies:
            if body == self:
                pass
            else:
                attraction = self.G * self.mass * body.mass * self.pos.dist(body.pos)**-2
                self.velocity = self.velocity + self.pos.vdist(body.pos).norm() * attraction
        #print(self.velocity.vect)

    def show(self, screen):
        self.pos = self.pos + self.velocity / self.mass
        pygame.draw.circle(screen, self.color, round(self.pos), self.size)

