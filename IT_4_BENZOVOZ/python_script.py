from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

global xrot 
global yrot 

def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:      # Клавиша вверх
        xrot -= 2.0             # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:    # Клавиша вниз
        xrot += 2.0             # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:    # Клавиша влево
        yrot -= 2.0             # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:   # Клавиша вправо
        yrot += 2.0             # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()         # Вызываем процедуру перерисовки
    
def display():
    global xrot
    global yrot
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)                              # Вращаем по оси X на величину xrot
    glRotatef(yrot, 0.0, 1.0, 0.0) 
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[168/255,101/255,64/255,1.])
    glTranslatef(0.0, 0.0, -0.25)
    glutSolidCube(0.25)
    glTranslatef(0.0, 0.0, 0.25)
    glutSolidCube(0.25)
    glTranslatef(0.0, 0.0, 0.25)
    glutSolidCube(0.25)
    glTranslatef(-0.25, 0.0, 0.0)
    glutSolidCube(0.25)
    glTranslatef(0.0, 0.0, -0.6)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[1.0,0.,0.,1.])
    glutSolidCylinder(0.125, 0.4, 20,20)
    glTranslatef(0.3, 0.125, 0.125)
    glRotatef(90, 1.0, 0.0, 0.0)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[144/255,144/255,144/255,1.])
    glutSolidTorus(0.0625, 0.1,20,20)
    glTranslatef(0, 0, 0.25)
    glutSolidTorus(0.0625, 0.1,20,20)   
    glTranslatef(0, 0.475, 0)
    glutSolidTorus(0.0625, 0.1,20,20)
    glTranslatef(0, 0, -0.25)
    glutSolidTorus(0.0625, 0.1,20,20)
    glPopMatrix()
    glutSwapBuffers()
    
    
def main():
    global xrot
    global yrot
    xrot = 0.0
    yrot = 0.0
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700,700)
    glutCreateWindow(b'benzovoz')
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
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


#property_mat = [(0.0215, 0.1745, 0.0215), (0.7568, 0.61424, 0.07568), (0.633, 0.727811, 0.633), 0.6]
#property_mat = [(0, 0, 0), (0.5, 0, 0), (0.7, 0.6, 0.6), 0.25]
#glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, property_mat[0]) #рассеяный цвет
#glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, property_mat[2]) # зеркальный цвет
#glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, property_mat[1]) # диффузный цвет 
#glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, property_mat[3]) # мощность бликов