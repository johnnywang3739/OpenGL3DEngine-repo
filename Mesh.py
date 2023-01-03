from OpenGL.GL import *
import pygame


class Rotation:
    def __init__(self, angle, axis):
        self.angle = angle
        self.axis = axis


class Mesh:

    def __init__(self, vertices, triangles, draw_type, translation, rotation, scale):

        self.vertices = vertices
        self.triangles = triangles
        self.draw_type = draw_type
        self.translation = translation
        self. rotation = rotation
        self.scale =scale
    def draw(self, move=pygame.Vector3(0,0,0)):
        glPushMatrix()

        glTranslated(move.x, move.y, move.z)
        glTranslatef(self.translation.x, self.translation.y, self.translation.z)
        glRotate(self.rotation.angle, self.rotation.axis.x, self.rotation.axis.y, self.rotation.axis.z)
        glScalef(self.scale.x,self.scale.y, self.scale.z)
        for t in range(0, len(self.triangles) , 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()

        glPopMatrix()