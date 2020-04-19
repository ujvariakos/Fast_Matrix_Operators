import ctypes
import math
from typing import List
from dll_importer import dll_handler
from .Vector import Vector


class Matrix:

    def __init__(self, vectors:List[Vector]):
        self.vectors = vectors
        self.vector_len = len(vectors[0].points)
        # check lens
        for v in vectors:
            if len(v.points) != self.vector_len:
                raise ValueError('Vectors lens must be same')
        # self.fast_matrix_operators_dll = None
        self.fast_matrix_operators_dll = dll_handler.get_dll()

    def __str__(self):
        ret = str()
        for v in self.vectors:
            ret += str(v)
        return ret

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Others type must be Vector')
        if self.vector_len != other.vector_len:
            raise ValueError('Vectors must be the same size')
        # result = Matrix(list())
        # for i in range(len(self.points)):
        #     result.points.append(self.points[i] + v.points[i])
        func = self.fast_matrix_operators_dll.matrix_add
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                         ctypes.c_int32, ctypes.POINTER(ctypes.c_float), ctypes.c_int32, ctypes.c_int32]
        func.restype = ctypes.POINTER(ctypes.c_float)
        points_arg0 = list()
        for v in self.vectors:
            points_arg0.extend(v.points)
        arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
        points_arg1 = list()
        for v in other.vectors:
            points_arg1.extend(v.points)
        arg1 = (ctypes.c_float * len(points_arg1))(*(points_arg1))
        ret = func(arg0, len(self.vectors),len(self.vectors[0].points),
                   arg1, len(other.vectors),len(other.vectors[0].points))
        ret_v = list()
        for i in range(len(self.vectors)):
            ret_points = list()
            for k in range(len(self.vectors[0].points)):
                ret_points.append(ret[i*len(self.vectors[0].points) + k])
            ret_vector = Vector(ret_points)
            ret_v.append(ret_vector)
        return Matrix(ret_v)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('Others type must be Vector')
        if self.vector_len != other.vector_len:
            raise ValueError('Vectors must be the same size')
        # result = Matrix(list())
        # for i in range(len(self.points)):
        #     result.points.append(self.points[i] + v.points[i])
        func = self.fast_matrix_operators_dll.matrix_sub
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                         ctypes.c_int32, ctypes.POINTER(ctypes.c_float), ctypes.c_int32, ctypes.c_int32]
        func.restype = ctypes.POINTER(ctypes.c_float)
        points_arg0 = list()
        for v in self.vectors:
            points_arg0.extend(v.points)
        arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
        points_arg1 = list()
        for v in other.vectors:
            points_arg1.extend(v.points)
        arg1 = (ctypes.c_float * len(points_arg1))(*(points_arg1))
        ret = func(arg0, len(self.vectors),len(self.vectors[0].points),
                   arg1, len(other.vectors),len(other.vectors[0].points))
        ret_v = list()
        for i in range(len(self.vectors)):
            ret_points = list()
            for k in range(len(self.vectors[0].points)):
                ret_points.append(ret[i*len(self.vectors[0].points) + k])
            ret_vector = Vector(ret_points)
            ret_v.append(ret_vector)
        return Matrix(ret_v)

    def test(self):
        result = Vector(list())
        # for i in range(len(self.points)):
        #     result.points.append(self.points[i] + v.points[i])
        func = self.fast_matrix_operators_dll.create_matrix
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32, ctypes.c_int32]
        func.restype = ctypes.POINTER(ctypes.c_float)
        points = list()
        for v in self.vectors:
            points.extend(v.points)
        arg0 = (ctypes.c_float * len(points))(*(points))
        ret = func(arg0, len(points), self.vector_len)
        for i in range(self.vector_len):
            result.points.append(ret[i])
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        print('result', result)
        return result