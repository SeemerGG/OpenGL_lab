from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys


xrot = 0

def fun_rotate_light():
    global xrot
    if xrot:
        return -pow(xrot,2) + 1
    else:
        return 0

def display():
    global xrot
    light_position = [0.,0.,0.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glutSolidSphere(0.5, 40, 20)
    glTranslatef(0+xrot, 0, fun_rotate_light())
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glPopMatrix()
    glutSwapBuffers()

def specialkeys(key, x, y):
    global xrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        xrot -= 0.1             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        xrot += 0.1             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700)
    glutCreateWindow(b'rotate_light')
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glutDisplayFunc(display)
    glutSpecialFunc(specialkeys)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,5,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return

main()