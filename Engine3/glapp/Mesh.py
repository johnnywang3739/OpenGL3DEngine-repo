import pygame
from .GraphicsData import *
from .Uniform import *
from .Transformations import *
from .Texture import *


class Mesh:
    def __init__(self, vertices,
                 imagefile=None,
                 vertex_normals=None,
                 vertex_uvs=None,
                 vertex_colors=None,
                 draw_type=GL_TRIANGLES,
                 translation=pygame.Vector3(0, 0, 0),
                 rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 scale=pygame.Vector3(1, 1, 1),
                 move_rotation=Rotation(0, pygame.Vector3(0, 1, 0)),
                 move_translate=pygame.Vector3(0, 0, 0),
                 move_scale=pygame.Vector3(1, 1, 1),
                 material=None
                 ):
        self.material=material
        self.vertices = vertices
        self.vertex_normals = vertex_normals
        self.vertex_uvs = vertex_uvs
        self.draw_type = draw_type
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        if vertices is not None:
            position = GraphicsData("vec3", self.vertices)
            position.create_variable(self.material.program_id, "position")
        if vertex_colors is not None:
            colors = GraphicsData("vec3", vertex_colors)
            colors.create_variable(self.material.program_id, "vertex_color")
        if vertex_normals is not None:
            v_normals = GraphicsData("vec3", vertex_normals)
            v_normals.create_variable(self.material.program_id, "vertex_normal")
        if vertex_uvs is not None:
            v_uvs = GraphicsData("vec2", vertex_uvs)
            v_uvs.create_variable(self.material.program_id, "vertex_uv")
        self.transformation_mat = identity_mat()
        self.transformation_mat = rotateA(self.transformation_mat, rotation.angle, rotation.axis)
        self.transformation_mat = translate(self.transformation_mat, translation.x, translation.y, translation.z)
        self.transformation_mat = scale3(self.transformation_mat, scale.x, scale.y, scale.z)
        self.transformation = Uniform("mat4", self.transformation_mat)
        self.transformation.find_variable(self.material.program_id, "model_mat")
        self.move_rotation = move_rotation
        self.move_translate = move_translate
        self.move_scale = move_scale
        self.texture = None
        if imagefile is not None:
            self.image = Texture(imagefile)
            self.texture = Uniform("sampler2D", [self.image.texture_id, 1])


    def draw(self, camera, lights):
        self.material.use()
        camera.update(self.material.program_id)
        if lights is not None:
            for light in lights:
                light.update(self.material.program_id)  
        if self.texture is not None:
            self.texture.find_variable(self.material.program_id, "tex")
            self.texture.load()
        self.transformation_mat = rotateA(self.transformation_mat, self.move_rotation.angle, self.move_rotation.axis)
        self.transformation_mat = translate(self.transformation_mat,
                                            self.move_translate.x, self.move_translate.y, self.move_translate.z)
        self.transformation_mat = scale3(self.transformation_mat,
                                         self.move_scale.x, self.move_scale.y, self.move_scale.z)
        self.transformation = Uniform("mat4", self.transformation_mat)
        self.transformation.find_variable(self.material.program_id, "model_mat")
        self.transformation.load()
        glBindVertexArray(self.vao_ref)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
