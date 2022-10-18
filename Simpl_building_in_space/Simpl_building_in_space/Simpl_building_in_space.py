from cmath import cos, sin
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def floor():
    glColor3f(222/255, 184/255, 135/255)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0.5, 0)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(-0.5, -0.5, 0)
    glEnd()

def walls():
    glColor3f(165/255, 42/255, 42/255)
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(-0.5, 0.5, 0)

    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0)
    glVertex3f(-0.5, 0.5, 0)

    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0)
    glVertex3f(-0.5, -0.5, 0)

    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0)
    glVertex3f(0.5, -0.5, 0)
    glEnd()

def roof():
    glColor3f(95/255, 158/255, 160/255)
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 0, 0.75)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    glVertex3f(0, 0, 0.75)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    
    glVertex3f(0, 0, 0.75)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    glVertex3f(0, 0, 0.75)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glEnd()

def house():
    walls()
    roof()
    floor()
    




def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glClearColor(0, 1, 1, 1)
    glTranslatef(0,0,-5)
    flags = [False, False, False, False]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glRotatef(5, 0.1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(-5, 0.1, 0, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(5, 0, 0, 0.1)
                elif event.key == pygame.K_LEFT:
                    glRotatef(-5, 0, 0, 0.1)
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        house()

        pygame.display.flip()
        pygame.time.wait(10)

main() 
