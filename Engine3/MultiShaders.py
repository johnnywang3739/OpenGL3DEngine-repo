from glapp.PyOGLApp import *
from glapp.LoadMesh import *
from glapp.Light import *
from glapp.Material import *
from glapp.Axes import *




class MultiShaders(PyOGLApp):

    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.plane = None
        self.floor = None
        self.tabletop = None
        self.lights = []
        self.teapot = None
        self.axes = None
        glEnable(GL_CULL_FACE)

    def initialise(self):
        mat = Material("shaders/texturedvert.vs", "shaders/texturedfrag.vs")
        axesmat = Material("shaders/vertexcolvert.vs", "shaders/vertexcolfrag.vs")

        self.axes = Axes(pygame.Vector3(0, 0, 0), axesmat)
        self.floor = LoadMesh("models/plane.obj", "images/tiles.png",
                              location=pygame.Vector3(0, -1.5, 0),
                              scale= pygame.Vector3(5,1,5),
                              material=mat)
        # self.plane = LoadMesh("models/plane.obj", "images/window.png",
        #                       location=pygame.Vector3(0, 0, 0),
        #                       material=mat)
        self.tabletop = LoadMesh("models/tabletop.obj", "images/timber.png",
                              location=pygame.Vector3(0, -0.5, 0),
                              scale = pygame.Vector3(1.2, 0.8, 1.2),
                              material=mat)
        self.leg1 = LoadMesh("models/tableleg.obj", "images/timber.png",
                        location=pygame.Vector3(-0.5, -1, 0.5),
                        material=mat)
        self.leg2 = LoadMesh("models/tableleg.obj", "images/timber.png",
                        location=pygame.Vector3(-0.5, -1, -0.5),
                        material=mat)
        self.leg3 = LoadMesh("models/tableleg.obj", "images/timber.png",
                location=pygame.Vector3(0.5, -1, -0.5),
                material=mat)
        self.leg4 = LoadMesh("models/tableleg.obj", "images/timber.png",
                location=pygame.Vector3(0.5, -1, 0.5),
                material=mat)
        
        self.teapot = LoadMesh("models/teapot.obj", "images/gold.png",
                              location=pygame.Vector3(0.5, -0.5, 0),
                              scale = pygame.Vector3(0.2, 0.2, 0.2),
                              material=mat)
        
        self.lights.append(Light(pygame.Vector3(-2, 2, 0), pygame.Vector3(1, 1, 1), 0))  
        # self.lights.append(Light(pygame.Vector3(1, 1, 0), pygame.Vector3(1, 0, 1), 0))  
        self.camera = Camera(self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.axes.draw(self.camera, None)
        self.tabletop.draw(self.camera, self.lights)
        self.leg1.draw(self.camera, self.lights)
        self.leg2.draw(self.camera, self.lights)
        self.leg3.draw(self.camera, self.lights)
        self.leg4.draw(self.camera, self.lights)
        self.floor.draw(self.camera, self.lights)
        self.teapot.draw(self.camera, self.lights)




# import pygame
# from pygame.locals import DOUBLEBUF, OPENGL
# from OpenGL.GL import *
# from OpenGL.GL.shaders import *

# pygame.init()
# screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)

# if not glCreateShader:
#     print("glCreateShader is not loaded")
# else:
#     shader = glCreateShader(GL_VERTEX_SHADER)
#     print("Shader ID:", shader)

# pygame.quit()


MultiShaders().mainloop()
