import ctypes
# import math
import numpy
from typing import List
from dll_importer import dll_handler
from .Vector import Vector



class Matrix:

    def __init__(self, vectors):
        if isinstance(vectors, List):
            self.vectors = vectors
        else:
            self.vectors = list()
            for v in vectors:
                vector = Vector(v)
                print(vector)
                self.vectors.append(vector)
        self.vector_len = len(self.vectors[0].points)
        for v in self.vectors:
            if len(v.points) != self.vector_len:
                raise ValueError('Vectors lens must be same')
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

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            func = self.fast_matrix_operators_dll.matrix_mul_scalar
            func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                             ctypes.c_int32, ctypes.c_float]
            func.restype = ctypes.POINTER(ctypes.c_float)
            points_arg0 = list()
            for v in self.vectors:
                points_arg0.extend(v.points)
            arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
            ret = func(arg0, len(self.vectors),len(self.vectors[0].points), other)
            ret_v = list()
            for i in range(len(self.vectors)):
                ret_points = list()
                for k in range(len(self.vectors[0].points)):
                    ret_points.append(ret[i * len(self.vectors[0].points) + k])
                ret_vector = Vector(ret_points)
                ret_v.append(ret_vector)
        elif isinstance(other, Matrix):
            func = self.fast_matrix_operators_dll.matrix_mul_m
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
            ret = func(arg0, len(self.vectors), len(self.vectors[0].points),
                       arg1, len(other.vectors), len(other.vectors[0].points))
            ret_v = list()
            for i in range(len(self.vectors)):
                ret_points = list()
                for k in range(len(other.vectors[0].points)):
                    ret_points.append(ret[i*len(other.vectors[0].points) + k])
                ret_vector = Vector(ret_points)
                ret_v.append(ret_vector)
        elif isinstance(other, Vector):
            _vectors = list()
            for p in other.points:
                _vectors.append(Vector([p]))
            _m = Matrix(_vectors)
            func = self.fast_matrix_operators_dll.matrix_mul_m
            func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                             ctypes.c_int32, ctypes.POINTER(ctypes.c_float), ctypes.c_int32, ctypes.c_int32]
            func.restype = ctypes.POINTER(ctypes.c_float)
            points_arg0 = list()
            for v in self.vectors:
                points_arg0.extend(v.points)
            arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
            points_arg1 = list()
            for v in _m.vectors:
                points_arg1.extend(v.points)
            arg1 = (ctypes.c_float * len(points_arg1))(*(points_arg1))
            ret = func(arg0, len(self.vectors), len(self.vectors[0].points),
                       arg1, len(_m.vectors), len(_m.vectors[0].points))
            ret_v = list()
            for i in range(len(self.vectors)):
                ret_points = list()
                for k in range(len(_m.vectors[0].points)):
                    ret_points.append(ret[i*len(_m.vectors[0].points) + k])
                ret_vector = Vector(ret_points)
                ret_v.append(ret_vector)
        else:
            raise ValueError('Wrong other type it should be int or float or Matrix or Vector')
        return Matrix(ret_v)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            func = self.fast_matrix_operators_dll.matrix_div_scalar
            func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                             ctypes.c_int32, ctypes.c_float]
            func.restype = ctypes.POINTER(ctypes.c_float)
            points_arg0 = list()
            for v in self.vectors:
                points_arg0.extend(v.points)
            arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
            ret = func(arg0, len(self.vectors),len(self.vectors[0].points), other)
            ret_v = list()
            for i in range(len(self.vectors)):
                ret_points = list()
                for k in range(len(self.vectors[0].points)):
                    ret_points.append(ret[i * len(self.vectors[0].points) + k])
                ret_vector = Vector(ret_points)
                ret_v.append(ret_vector)
        else:
            raise ValueError('Wrong other type it should be int or float or int')
        return Matrix(ret_v)

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            func = self.fast_matrix_operators_dll.matrix_div_scalar
            func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                             ctypes.c_int32, ctypes.c_float]
            func.restype = ctypes.POINTER(ctypes.c_float)
            points_arg0 = list()
            for v in self.vectors:
                points_arg0.extend(v.points)
            arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
            ret = func(arg0, len(self.vectors),len(self.vectors[0].points), other)
            ret_v = list()
            for i in range(len(self.vectors)):
                ret_points = list()
                for k in range(len(self.vectors[0].points)):
                    ret_points.append(ret[i * len(self.vectors[0].points) + k])
                ret_vector = Vector(ret_points)
                ret_v.append(ret_vector)
        else:
            raise ValueError('Wrong other type it should be int or float or int')
        return Matrix(ret_v)

    def inv(self):
        if self.vector_len != len(self.vectors):
            raise ValueError('Not square matrix')
        func = self.fast_matrix_operators_dll.matrix_invert
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                         ctypes.c_int32]
        func.restype = ctypes.POINTER(ctypes.c_float)
        points_arg0 = list()
        for v in self.vectors:
            points_arg0.extend(v.points)
        arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
        ret = func(arg0, len(self.vectors),len(self.vectors[0].points))
        ret_v = list()
        for i in range(len(self.vectors)):
            ret_points = list()
            for k in range(len(self.vectors[0].points)):
                ret_points.append(ret[i * len(self.vectors[0].points) + k])
            ret_vector = Vector(ret_points)
            ret_v.append(ret_vector)
        return Matrix(ret_v)

    def det(self):
        func = self.fast_matrix_operators_dll.matrix_determinant
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int32,
                         ctypes.c_int32]
        func.restype = ctypes.c_float
        points_arg0 = list()
        for v in self.vectors:
            points_arg0.extend(v.points)
        arg0 = (ctypes.c_float * len(points_arg0))(*(points_arg0))
        ret = func(arg0, len(self.vectors),len(self.vectors[0].points))
        return ret

    def toNumpy(self):
        l = list()
        for v in self.vectors:
            l.append(v.toNumpy())
        return numpy.array(l, dtype=float)