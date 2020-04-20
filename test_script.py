from dll_importer import *
from matrix_and_vector.Vector import Vector
from matrix_and_vector.Matrix import Matrix
import numpy

# import numpy

import ctypes

# fast_matrix_operators_dll = dll_handler.get_dll()
#
#
# # print(fast_matrix_operators_dll.sum(1,3))
#
# a = numpy.array([1.1,2.2,3.3])
# #2,1,1,1,     4,3,6,4,    6,7,21,16,    2,3,15,23
# b = numpy.array([[2,1,1,1],[4,3,6,4],[6,7,21,16],[2,3,15,23]])
#
# # c = numpy.array([[21,16],[15,23]])
#
# m = Matrix(b)
# print(m.det())
# # c = numpy.array([[2.1, 2.1], [4.1, 5.1]])
# # #
# # m = Matrix(c)
# # m6565 = m/2
# # print('m6565',m6565)
# # print(m6565.toNumpy())
#
# # print(b)
# #
# v1 = Vector(a)
# v2 = Vector(a)
# print(v1)
# print(v1+v2)
# # # print(a)
# # print(v.toNumpy())
# # print(a == v.toNumpy())
# # m = Matrix(b)
# # print(m.toNumpy())
# # print(m)
# # v2 = Vector([7,2])
# # v3 = Vector([5,9])
# # v4 = Vector([1,1,1])
# # v5 = Vector([2,2,2])
# #
# # v_try = Vector([1,1])
# #
# # m = Matrix([Vector([2,1]), Vector([1,1])])
# # # m2 = Matrix([Vector([1]), Vector([1])])
# # m3 = m*v_try
# # print('MMMM', m3)
# # print(v1+v2)
#
# # m1 = Matrix([v1, v2, v3])
# # m2 = Matrix([v4,v5])
# # print("------------------------------")
# # m3 = m1 * v_try
# # m1.test()
# # print(m1.test())
# # print(m1)
# # print(m2)
# # print(m3)
# # print("------------------------------")
# # r = m.test()
# # print("r ", r)
#
# # v3 = v1 /2
# #
# # print("v1", v1)
# # print("v2", v2)
# # print("v3", v3)
# #
# # v4 = v3 - v1
#
#
#
#
#
#
# # func = fast_matrix_operators_dll.vector_add
# # func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64]
# # func.restype = ctypes.POINTER(ctypes.c_float)
# # e = ctypes.c_float(0.1)
# # # arg0 = (ctypes.c_float * 2)(e, 1.1)
# # # arg1 = (ctypes.c_float * 2)(e, 1.1)
# # valami = [e, 1.1]
# #
# # print(i for i in valami)
# # arg0 = (ctypes.c_float * 2)(*valami)
# # arg1 = (ctypes.c_float * 2)(*valami)
# #
# # ret = func(arg0, 2, arg1, 2)
# # for r in range(2):
# #     print(ret[r])
# #
# # ret = fast_matrix_operators_dll.vector_free(ret)
# # func2 = fast_matrix_operators_dll.vector_free
# # func2.argtypes = [ctypes.POINTER(ctypes.c_float)]
# # func2(ret)
# #
# # print(func(arg0, 2, arg1, 2))
a = numpy.array([[1, 4], [1, 4]], dtype=float)
b = numpy.array([[1], [1]],dtype=float)


m1 = Matrix(a)
print(m1)
m2 = Matrix(b)
print(m2)
m3 = m1 * m2

print('fewfwdfwefw',m3)
# m3.toNumpy()
# print(m3.toNumpy())

# a = numpy.array([1.5, 4.3], dtype=float)
# v1 = Vector(a)
# print(v1.toNumpy())
#
#
#
# a = numpy.array([[2.1, 2.1], [4.1, 5.1]])
# m1 = Matrix(a)
# m3 = m1 / 2
# print('m3.toNumpy()',m3.toNumpy())