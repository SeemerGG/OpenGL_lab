from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

glutImiDisplayMode(GLUT_DOUBLE | GLUT_RGB) #инициализируем режим отображения с двойной буферизацией и отображением цветов в формате rgb

glutIniWindowSize(512, 512) #задаем начальный размер окна 

glutIniWindowPosition(1920, 1080) #позиция окна относительно левого верхнего угла 

glutInit(sys.argv) #инициализируем OpenGL 

glutCreateWindow(b"Flag") #создаем окно 

glutMainLoop() # запуск основного цикла программы 



