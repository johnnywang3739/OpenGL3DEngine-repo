from glApp.PyOGApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO
from glApp.GraphicsData import *
vertex_shader = r'''
#version 330 core
in vec3 position;
void main()
{
   gl_Position = vec4(position.x, position.y, position.z, 1.0);
}
'''

fragment_shader = r'''
#version 330 core
out vec4 FragColor;
void main()
{
FragColor = vec4(0, 1, 1, 1.0f);
}
'''

class MyFirstShader(PyOGApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.vao_ref = None
        self.vertex_count = 0


    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glPointSize(10)
        position_data = [[0, -0.9, 0], [0.6, 0.8, 0], [0.9, -0.2, 0]]
        self.vertex_count = len(position_data)
        position_variable = GraphicsData("vec3", position_data)
        position_variable.create_variable(self.program_id, "position")

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_POINTS, 0, self.vertex_count)

MyFirstShader().mainloop()