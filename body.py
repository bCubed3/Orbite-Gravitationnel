from vector import Vector

class Body:
    def __init__(self, mass, size, color, pos, velocity):
        self.mass = mass
        self.size = size
        self.color = color
        self.pos = pos
        self.velocity = velocity

    def find_attractions(self, bodies):
        attractions = []
        for body in bodies:
            if body == self:
                pass

