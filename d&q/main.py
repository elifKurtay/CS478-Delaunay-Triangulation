"""

Delaunay Triangulation. 

Given a set of points on a plane, compute DT using divide-and-conquer
alogorithm.

"""

import pygame
from pygame.locals import *
from config import *
import config as G
import time
import numpy as np
from mesh import Mesh
from mesh import gen_random
from mesh import gen_grid
from mesh import gen_circle
from mesh import gen_circle_i
from delaunay import delaunay


def main():
    pygame.init()
    pygame.display.set_caption('Delaunay')
    G.screen_w = SCREEN_W
    G.screen_h = SCREEN_H
    G.screen_mode = SCREEN_MODE
    G.screen = pygame.display.set_mode([G.screen_w, G.screen_h], G.screen_mode)
    G.screen.fill(BG_COLOR)
    G.background = G.screen.copy()
    point_n = 20_000

    G.mesh = Mesh()
    print("Generating Delaunay Mesh...")
    start = time.time()
    G.mesh.generate(point_n)
    end = time.time()
    print("Elapsed time: " + str(end - start))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.__dict__['key'] == 32:  # space
                    G.mesh.generate()
        time.sleep(0.1)


def main_no_visual():
    points = gen_random(100_000_000, 100_000_000, 1000)
    edges = delaunay(points)
    print("Number of edges (random): " + str(len(edges)))


if __name__ == '__main__':
    main()
    #main_no_visual()
