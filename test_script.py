from dll_importer import *
from matrix_and_vector.Vector import Vector

# import numpy

import ctypes

fast_matrix_operators_dll = dll_handler.get_dll()


# print(fast_matrix_operators_dll.sum(1,3))

v1 = Vector([2.2,2.2,2.2,4.4])
v2 = Vector([3,2,1, 5])

v3 = v1 /2

print("v1", v1)
print("v2", v2)
print("v3", v3)

v4 = v3 - v1






# func = fast_matrix_operators_dll.vector_add
# func.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int64]
# func.restype = ctypes.POINTER(ctypes.c_float)
# e = ctypes.c_float(0.1)
# # arg0 = (ctypes.c_float * 2)(e, 1.1)
# # arg1 = (ctypes.c_float * 2)(e, 1.1)
# valami = [e, 1.1]
#
# print(i for i in valami)
# arg0 = (ctypes.c_float * 2)(*valami)
# arg1 = (ctypes.c_float * 2)(*valami)
#
# ret = func(arg0, 2, arg1, 2)
# for r in range(2):
#     print(ret[r])
#
# ret = fast_matrix_operators_dll.vector_free(ret)
# func2 = fast_matrix_operators_dll.vector_free
# func2.argtypes = [ctypes.POINTER(ctypes.c_float)]
# func2(ret)
#
# print(func(arg0, 2, arg1, 2))