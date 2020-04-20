import ctypes
import math
from typing import List
from dll_importer import dll_handler
import numpy
# numpy.



class Vector:

    def __init__(self, points):
        self.points = list()
        for p in points:
            # if not isinstance(p, float):
            #     raise TypeError('Possible type is float')
            self.points.append(float(p))
        # self.fast_matrix_operators_dll = None
        self.fast_matrix_operators_dll = dll_handler.get_dll()

    def __str__(self):
        return str(self.points)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Others type must be Vector')
        if len(self.points) != len(other.points):
            raise ValueError('Vectors must be the same size')
        result = Vector(list())
        # for i in range(len(self.points)):
        #     result.points.append(self.points[i] + v.points[i])
        func = self.fast_matrix_operators_dll.vector_add
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64]
        func.restype = ctypes.POINTER(ctypes.c_float)
        arg0 = (ctypes.c_float * len(self.points))(*(self.points))
        arg1 = (ctypes.c_float * len(other.points))(*(other.points))
        ret = func(arg0, len(self.points), arg1, len(other.points))
        for i in range(len(self.points)):
            result.points.append(ret[i])
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        return result

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Others type must be Vector')
        if len(self.points) != len(other.points):
            raise ValueError('Vectors must be the same size')
        result = Vector(list())
        func = self.fast_matrix_operators_dll.vector_sub
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64]
        func.restype = ctypes.POINTER(ctypes.c_float)
        arg0 = (ctypes.c_float * len(self.points))(*(self.points))
        arg1 = (ctypes.c_float * len(other.points))(*(other.points))
        ret = func(arg0, len(self.points), arg1, len(other.points))
        for i in range(len(self.points)):
            result.points.append(ret[i])
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        return result

    def __mul__(self, other):
        if not isinstance(other, (int,float)):
            raise TypeError('Others type must be int or float')
        s = other
        if isinstance(other, int):
            s = float(other)
        result = Vector(list())
        func = self.fast_matrix_operators_dll.vector_mult
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64, ctypes.c_float]
        func.restype = ctypes.POINTER(ctypes.c_float)
        arg0 = (ctypes.c_float * len(self.points))(*(self.points))
        ret = func(arg0, len(self.points), s)
        for i in range(len(self.points)):
            result.points.append(ret[i])
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        return result

    def __truediv__(self, other):
        if not isinstance(other, (int,float)):
            raise TypeError('Others type must be int or float')
        # if other == 0:
        #     raise ValueError("Other can not be 0")
        s = other
        if isinstance(other, int):
            s = float(other)
        result = Vector(list())
        func = self.fast_matrix_operators_dll.vector_div
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64, ctypes.c_float]
        func.restype = ctypes.POINTER(ctypes.c_float)
        arg0 = (ctypes.c_float * len(self.points))(*(self.points))
        ret = func(arg0, len(self.points), s)
        for i in range(len(self.points)):
            result.points.append(ret[i])
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        return result

    def __floordiv__(self, other):
        if not isinstance(other, (int,float)):
            raise TypeError('Others type must be int or float')
        # if other == 0:
        #     raise ValueError("Other can not be 0")
        # s = other
        # if isinstance(other, int):
        #     s = float(other)
        result = Vector(list())
        func = self.fast_matrix_operators_dll.vector_div
        func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64, ctypes.c_float]
        func.restype = ctypes.POINTER(ctypes.c_float)
        arg0 = (ctypes.c_float * len(self.points))(*(self.points))
        ret = func(arg0, len(self.points), other)
        for i in range(len(self.points)):
            result.points.append(math.floor(ret[i]))
        # ret = self.fast_matrix_operators_dll.vector_free(ret)
        return result

    def toNumpy(self):
        # array = numpy.arange(len(self.points), dtype=float)
        # print('array', array)
        # for i in range(len(self.points)):
        #     array[i] = self.points[i]
        # for p in
        return numpy.array(self.points, dtype=float)
        # print('array', array)
        # return array
