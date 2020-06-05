from vector import Vector
import pygame


class Body:
    def __init__(self, mass, size, color, pos, velocity, sim_speed):
        self.mass = mass
        self.size = size
        self.color = color
        self.pos = Vector(pos)  # this should be a vector
        self.velocity = Vector(velocity)  # this should be a vector
        self.G = 6.674 * 10**-11
        self.sim_speed = sim_speed

    def find_attractions(self, bodies):
        for body in bodies:
            if body == self:
                pass
            else:
                d = self.pos.dist(body.pos)
                attraction = self.G * self.mass * body.mass * (d * 10**10)**-2
                if d < self.size + body.size:
                    self.mass = self.mass + body.mass
                    self.size = round(self.size + body.size / 3)
                    self.velocity = self.velocity + body.velocity / body.mass
                    body.remove(bodies)
                #print("a :", attraction, "v :", self.velocity.vect)
                self.velocity = self.velocity + (self.pos.vdist(body.pos).norm() * (attraction / self.mass))

    def show(self, screen, zoom, center):
        self.pos = self.pos + self.velocity
        #print("c :", self.color, "v :", round(self.velocity).vect, "pos :", round(self.pos).vect)
        pygame.draw.circle(screen, self.color, round((self.pos * zoom - center * (zoom - 1))), self.size)

    def remove(self, l):
        l.remove(self)
