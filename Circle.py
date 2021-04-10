import pygame
import numpy as np
from random import randint
from itertools import combinations



class Circle():
    FIELD_WIDTH = 600
    FIELD_HEIGHT = 600
    VELOCITY_MAX = 0
    id_list = []
    def __init__(self):
        self.id = len(self.id_list) + 1
        self.id_list.append(self.id)
        self.mass = randint(10, 100)
        self.radius = randint(10, 40)
        self.r = np.array((randint(0 + self.radius, self.FIELD_WIDTH - self.radius),
                                               randint(0 + self.radius, self.FIELD_HEIGHT - self.radius)))
        self.v = np.array((randint(-self.VELOCITY_MAX, self.VELOCITY_MAX), randint(-self.VELOCITY_MAX, self.VELOCITY_MAX)))
        if self.v[0] == 0 or self.v[1] == 0:
            self.v = pygame.math.Vector2(randint(-self.VELOCITY_MAX, self.VELOCITY_MAX), randint(-self.VELOCITY_MAX, self.VELOCITY_MAX))
        self.a = np.array((1,1))
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))


    def draw(self, screen):
        self.screen = screen
        return pygame.draw.circle(self.screen, self.color, (self.r[0], self.r[1]), self.radius)

    def advance(self, dt):
        self.r += self.v * dt



class Simulation():
    def wall_collision(self, particle):
        if particle.r[0] - particle.radius < 0:
            particle.r[0] = particle.radius
            particle.v[0] = -particle.v[0]
        if particle.r[0] + particle.radius > 1:
            particle.r[0] = 1 - particle.radius
            particle.v[0] = -particle.v[0]
        if particle.r[1] - particle.radius < 0:
            particle.r[1] = particle.radius
            particle.v[1] = -particle.v[1]
        if particle.r[1] + particle.radius > 1:
            particle.r[1] = 1 - particle.radius
            particle.v[1] = -particle.v[1]


    def change_velocity(self, p1, p2):
        r1 = p1.r
        r2 = p2.r
        v1 = p1.v
        v2 = p2.v
        m1 = p1.mass
        m2 = p2.mass
        M = m1 + m2
        d = np.linalg.norm(r1 - r2) ** 2
        u1 = v1 - 2 * m2 / M * np.dot(v1 - v2, r1 - r2) / d * (r1 - r2)
        u2 = v2 - 2 * m1 / M * np.dot(v2 - v1, r2 - r1) / d * (r2 - r1)
        p1.v = u1
        p2.v = u2
        return p1.v, p2.v


    def particle_collision(self, p1, p2, dt):
        pairs = combinations(range(len(self.id_list)), 2)
        for i, j in pairs:
            if self.id_list[i].overlaps(self.id_list[j]):
                self.change_velocity(self.id_list[i], self.id_list[j])

    def overlap(self, other):
        return np.hypot(*(self.p - other.r)) < self.radius + other.radius

    def is_clicked(self):
        pass