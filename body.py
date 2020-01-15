from vector import Vector
import pygame

class Body:
    def __init__(self, mass, size, color, pos, velocity, sim_speed):
        self.mass = mass
        self.size = size
        self.color = color
        self.pos = Vector(pos) # this should be a vector
        self.velocity = Vector(velocity) # this should be a vector
        self.G = 6.674 * 10**-11
        self.sim_speed = sim_speed
        self.accel = Vector((0, 0))

    def find_attractions(self, bodies):
        for body in bodies:
            if body == self:
                pass
            else:
                attraction = self.G * self.mass * body.mass * (self.pos.dist(body.pos) * 10**9)**-2
                #print("a :", attraction, "v :", self.velocity.vect)
                self.velocity = self.velocity + (self.pos.vdist(body.pos).norm() * (attraction / self.mass))

    def show(self, screen):
        self.pos = self.pos + self.velocity
        #print("c :", self.color, "v :", round(self.velocity).vect, "pos :", round(self.pos).vect)
        pygame.draw.circle(screen, self.color, round(self.pos), self.size)

