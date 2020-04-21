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
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_sub(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        v2 = Vector(b)
        v3 = v1 - v2
        v3_numpy = numpy.subtract(a, b)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_mul(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])

        v1 = Vector(a)
        v3 = v1 * 5
        v3_numpy = numpy.multiply(a, 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_div(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])

        v1 = Vector(a)
        v3 = v1 / 5
        v3_numpy = numpy.divide(a, 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_matrix_add(self):
        a = numpy.array([[67, 4, 2],[7, 2, 2],[5, 9, 2]])
        b = numpy.array([[67, 1, 2],[7, 5, 2],[5, 9, 2]])
        m1 = Matrix(a)
        m2 = Matrix(b)
        m3 = m1 + m2
        print(m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1+np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i*(len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_sub(self):
        a = numpy.array([[67, 4, 2],[7, 2, 2],[5, 9, 2]])
        b = numpy.array([[67, 1, 2],[7, 5, 2],[5, 9, 2]])
        m1 = Matrix(a)
        m2 = Matrix(b)
        m3 = m1 - m2

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1-np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)


    def test_matrix_mul_matrix(self):

        a = numpy.array([[1.0, 4.0], [1.0, 2.0]])
        b = numpy.array([[1.0], [1.0]])
        m1 = Matrix(a)
        m2 = Matrix(b)
        m3 = m1 * m2
        print('m3',m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1*np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_mul_matrix2(self):
        za = numpy.array([[2.0, 1.0], [2.0, 1.0]],dtype=float)
        zb = numpy.array([[1.0], [1.0]] ,dtype=float)
        m1 = Matrix(za)
        m2 = Matrix(zb)
        m3 = m1 * m2
        print('m3',m3.toNumpy())

        np_m1 = numpy.matrix(za)
        np_m2 = numpy.matrix(zb)
        np_m3 = np_m1*np_m2
        np_m3 = np_m3.astype(float)
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_div(self):
        a = numpy.array([[2.1, 2.1], [4.1, 5.1]])
        m1 = Matrix(a)
        m3 = m1 / 2
        print('m3.toNumpy()',m3.toNumpy())

        np_m3 = a/2
        print('np_m3', np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_det(self):
        #b = numpy.array([[2,1,1,1],[4,3,6,4],[6,7,21,16],[2,3,15,23]])
        b = numpy.array([[2, 1, 1, 1,5], [4, 3, 6, 4,5], [6, 7, 21, 1,56], [2, 3, 15, 23,5], [2, 3, 112, 23,2]])
        m1 = Matrix(b)
        data = m1.det()
        data2 = numpy.linalg.det(b)
        numpy.testing.assert_array_almost_equal(data, data2, 5)


    def test_matrix_inv(self):
        #b = numpy.array([[2,1,1,1],[4,3,6,4],[6,7,21,16],[2,3,15,23]])
        b = numpy.array([[0,1,2], [1,1,3], [1,2,4]])
        m1 = Matrix(b)
        data = m1.inv()
        print('data ', data.toNumpy())
        data2 = numpy.linalg.inv(numpy.matrix(b))
        print('data2 ', data2)
        numpy.testing.assert_array_almost_equal(data.toNumpy(), data2, 5)



if __name__ == '__main__':
    unittest.main()
