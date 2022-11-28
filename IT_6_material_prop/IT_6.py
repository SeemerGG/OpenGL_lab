from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys


def resize(width,height):
   glViewport(0,0,width,height)
   glMatrixMode( GL_PROJECTION )
   glLoadIdentity()
   glOrtho(-5,5, -5,5, 2,12)
   gluLookAt( 0,0,5, 0,0,0, 0,1,0 )
   glMatrixMode( GL_MODELVIEW )
   



def display():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3d(1,1,1)
    glutSolidSphere(2, 50, 50)
    glutSwapBuffers()





def main():
    pos = [3,3,3,1]
    color = [1,1,1,1]
    sp1 = [1,1,1,1]
    sp2 = [0.1,0.1,0.1,1]
    sp3 = [0.5,0.5,0.5,0.5]
    mat_specular = [1,1,1,1]
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700)
    glutCreateWindow(b'rotate_light')
    glutDisplayFunc(display)
    glutReshapeFunc(resize)

  
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT3)
    glEnable(GL_LIGHT5)
    #glEnable(GL_LIGHT6)

    glLightfv(GL_LIGHT3, GL_SPECULAR, sp1)
    glLightfv(GL_LIGHT5, GL_SPECULAR, sp2)
    #glLightfv(GL_LIGHT6, GL_SPECULAR, sp3)


    color[1]=color[2]=0
    glLightfv(GL_LIGHT3, GL_DIFFUSE, color)

    color[0]=0
    color[1]=1
    glLightfv(GL_LIGHT5, GL_DIFFUSE, color)

    color[1]=0
    #color[2]=1
    #glLightfv(GL_LIGHT6, GL_DIFFUSE, color)

    glLightfv(GL_LIGHT3, GL_POSITION, pos)
    pos[0] = -3
    glLightfv(GL_LIGHT5, GL_POSITION, pos)
    #pos[0]=0;pos[1]=-3
    #glLightfv(GL_LIGHT6, GL_POSITION, pos)

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    glutMainLoop()

main()
