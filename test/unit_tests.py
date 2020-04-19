import unittest
from matrix_and_vector.Vector import Vector
from matrix_and_vector.Matrix import Matrix
import numpy

class MyTestCase(unittest.TestCase):

    def test_vector_add(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        v2 = Vector(b)
        v3 = v1 + v2
        v3_numpy = numpy.add(a, b)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)

    def test_vector_sub(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        v2 = Vector(b)
        v3 = v1 - v2
        v3_numpy = numpy.subtract(a, b)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)

    def test_vector_mul(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        # b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        # v2 = Vector(b)
        v3 = v1 * 5
        v3_numpy = numpy.multiply(a, 5)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)

    def test_vector_div(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        # b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        # v2 = Vector(b)
        v3 = v1 / 5
        v3_numpy = numpy.divide(a, 5)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)

    def test_matrix_add(self):
        a = numpy.array([[67, 4, 2],[7, 2, 2],[5, 9, 2]])
        b = numpy.array([[67, 1, 2],[7, 5, 2],[5, 9, 2]])

        # print(v1+v2)

        # m1 = Matrix([v1, v2, v3])
        # m2 = Matrix([v4, v5])
        m1 = Matrix(a)
        m2 = Matrix(b)
        # print("------------------------------")
        m3 = m1 - m2
        # print(m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1-np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i*(len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)


    def test_matrix_mul_matrix(self):
        # v1 = Vector([67, 4])
        # v2 = Vector([7, 2])
        # v3 = Vector([5, 9])
        # v4 = Vector([3, 1, 5])
        # v5 = Vector([6, 9, 7])
        a = numpy.array([[67, 4],[7, 2],[5, 9]])
        b = numpy.array([[3, 1, 5], [6, 9, 7]])

        # print(v1+v2)

        # m1 = Matrix([v1, v2, v3])
        # m2 = Matrix([v4, v5])
        m1 = Matrix(a)
        m2 = Matrix(b)
        # print("------------------------------")
        m3 = m1 * m2
        # print(m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1*np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i*(len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)

    def test_matrix_mul_matrix2(self):
        # v1 = Vector([2, 1])
        # v2 = Vector([2, 1])
        # v3 = Vector([1])
        # v4 = Vector([1])

        a = numpy.array([[2, 1], [2, 1]])
        b = numpy.array([[1], [1]])
        # v5 = Vector([6, 9, 7])

        # print(v1+v2)

        m1 = Matrix(a)
        m2 = Matrix(b)
        # print("------------------------------")
        m3 = m1 * m2
        print(m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1*np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i*(len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)



if __name__ == '__main__':
    unittest.main()
