import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
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

def Flag():

    glColor3f(0.0,0.0, 1)
    
    glBegin(GL_QUADS)
    
    glVertex2f(-3.0, -2.0)
    glVertex2f(-3, 2)
    glVertex2f(-1, 2)
    glVertex2f(-1, -2)
    
    glColor(1, 1, 1)
    glVertex2f(-1.0, 2.0)
    glVertex2f(-1, -2)
    glVertex2f(1, -2)
    glVertex2f(1, 2)
    
    glColor(1, 0, 0)
    glVertex2f(3, 2)
    glVertex2f(3, -2)
    glVertex2f(1, -2)
    glVertex2f(1, 2)

    glEnd()

    glBegin(GL_LINES)
    glColor3d(0.0, 0.0, 0.0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClearColor(119/255,221/255,231/255, 0.5)
    glTranslatef(0.0, 0.0, -10)
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