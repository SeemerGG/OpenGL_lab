from cmath import cos, sin
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
verticies = (
    (-3, 2, 0),
    (-1, 2, 0),
    (1, 2, 0),
    (3, 2, 0),
    (-3, -2, 0),
    (-1, -2, 0),
    (1, -2, 0),
    (3, -2, 0)
    )

edges = (
    (0, 3),
    (0, 4),
    (4, 7),
    (7, 3),
    (1, 5),
    (2, 6)
    )

def Star(radius, y_center, x_center):
    step = math.pi * 4.0 / 5.0
    glColor3f(1,1,1)
    glBegin(GL_LINE_LOOP) 
    angel = - math.pi / 2 
    i = 0
    while i < 5:
        x = x_center + radius * math.cos(angel)
        y = y_center + radius * math.sin(angel)
        glVertex2f(x, y)
        i += 1
        angel += step
    
    glEnd()


def Flag():
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-3, 6)
    glVertex2f(5, 6)
    glVertex2f(5, -6)
    glEnd()

    count = 0
    x = -4
    y = 5.5

    while count < 9:
        Star(0.5, y, x)
        count += 1
        x += 0.9
        y = x * -1.5
    
    #ффлаг франции
    #glColor3f(0.0,0.0, 1)
    
    #glBegin(GL_QUADS)
    
    #glVertex2f(-3.0, -2.0)
    #glVertex2f(-3, 2)
    #glVertex2f(-1, 2)
    #glVertex2f(-1, -2)
    
    #glColor(1, 1, 1)
    #glVertex2f(-1.0, 2.0)
    #glVertex2f(-1, -2)
    #glVertex2f(1, -2)
    #glVertex2f(1, 2)
    
    #glColor(1, 0, 0)
    #glVertex2f(3, 2)
    #glVertex2f(3, -2)
    #glVertex2f(1, -2)
    #glVertex2f(1, 2)

    #glEnd()

    #glBegin(GL_LINES)
    #glColor3d(0.0, 0.0, 0.0)
    #for edge in edges:
    #    for vertex in edge:
    #        glVertex3fv(verticies[vertex])

    #glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClearColor(0, 0, 139/255, 0)
    glTranslatef(0.0, 0.0, -14.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Flag()
        pygame.display.flip()
        pygame.time.wait(10)

main() 