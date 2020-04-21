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
        # for i in range(len(v3.points)):
        #     self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)
        # self.assertAlmostEqual(v3.toNumpy(), v3_numpy, 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_sub(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        v2 = Vector(b)
        v3 = v1 - v2
        v3_numpy = numpy.subtract(a, b)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        # for i in range(len(v3.points)):
        #     self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_mul(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        # b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        # v2 = Vector(b)
        v3 = v1 * 5
        v3_numpy = numpy.multiply(a, 5)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        # for i in range(len(v3.points)):
        #     self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_vector_div(self):
        a = numpy.array([2.2, 2.2, 2.2, 4.4])
        # b = numpy.array([3, 2, 1, 5])

        v1 = Vector(a)
        # v2 = Vector(b)
        v3 = v1 / 5
        v3_numpy = numpy.divide(a, 5)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        # for i in range(len(v3.points)):
        #     self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)
        numpy.testing.assert_array_almost_equal(v3.toNumpy(), v3_numpy, 5)

    def test_matrix_add(self):
        a = numpy.array([[67, 4, 2],[7, 2, 2],[5, 9, 2]])
        b = numpy.array([[67, 1, 2],[7, 5, 2],[5, 9, 2]])

        # print(v1+v2)

        # m1 = Matrix([v1, v2, v3])
        # m2 = Matrix([v4, v5])
        m1 = Matrix(a)
        m2 = Matrix(b)
        # print("------------------------------")
        m3 = m1 + m2
        print(m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1+np_m2
        print(np_m3)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i*(len(m3.vectors[i].points)) + k)
                # self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)
        # numpy.testing.assert_array_almost_equal(m3.toNumpy(), np_m3, 5)

    def test_matrix_sub(self):
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
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                # self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)


    def test_matrix_mul_matrix(self):
        # v1 = Vector([67, 4])
        # v2 = Vector([7, 2])
        # v3 = Vector([5, 9])
        # v4 = Vector([3, 1, 5])
        # v5 = Vector([6, 9, 7])
        # a = numpy.array([[67, 4],[7, 2],[5, 9]])
        # b = numpy.array([[3, 1, 5], [6, 9, 7]])

        a = numpy.array([[1.0, 4.0], [1.0, 2.0]])
        b = numpy.array([[1.0], [1.0]])

        # print(v1+v2)

        # m1 = Matrix([v1, v2, v3])
        # m2 = Matrix([v4, v5])
        m1 = Matrix(a)
        m2 = Matrix(b)
        # print("------------------------------")
        m3 = m1 * m2
        print('m3',m3)

        np_m1 = numpy.matrix(a)
        np_m2 = numpy.matrix(b)
        np_m3 = np_m1*np_m2
        print(np_m3)
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                # self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_mul_matrix2(self):
        # v1 = Vector([2, 1])
        # v2 = Vector([2, 1])
        # v3 = Vector([1])
        # v4 = Vector([1])

        za = numpy.array([[2.0, 1.0], [2.0, 1.0]],dtype=float)
        zb = numpy.array([[1.0], [1.0]] ,dtype=float)
        # v5 = Vector([6, 9, 7])

        # print(v1+v2)

        m1 = Matrix(za)
        m2 = Matrix(zb)
        # print("------------------------------")
        m3 = m1 * m2
        print('m3',m3.toNumpy())

        np_m1 = numpy.matrix(za)
        np_m2 = numpy.matrix(zb)
        np_m3 = np_m1*np_m2
        # np_m3 = numpy.array(a*b,dtype=float)
        # np_m3 = numpy.multiply(za,zb, dtype=float)
        np_m3 = np_m3.astype(float)
        # np_m3 = a*b
        print(np_m3)
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                # self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_div(self):
        a = numpy.array([[2.1, 2.1], [4.1, 5.1]])
        m1 = Matrix(a)
        m3 = m1 / 2
        print('m3.toNumpy()',m3.toNumpy())

        # np_m1 = numpy.matrix(a)
        np_m3 = a/2
        print('np_m3', np_m3)
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        for i in range(len(m3.vectors)):
            for k in range(len((m3.vectors[i].points))):
                act = (i * (len(m3.vectors[i].points)) + k)
                # self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
                self.assertAlmostEqual(m3.toNumpy().item(act), np_m3.item(act), 5)

    def test_matrix_det(self):
        #b = numpy.array([[2,1,1,1],[4,3,6,4],[6,7,21,16],[2,3,15,23]])

        b = numpy.array([[2, 1, 1, 1,5], [4, 3, 6, 4,5], [6, 7, 21, 1,56], [2, 3, 15, 23,5], [2, 3, 112, 23,2]])
        m1 = Matrix(b)
        data = m1.det()
        data2 = numpy.linalg.det(b)
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        numpy.testing.assert_array_almost_equal(data, data2, 5)


    def test_matrix_int(self):
        #b = numpy.array([[2,1,1,1],[4,3,6,4],[6,7,21,16],[2,3,15,23]])

        b = numpy.array([[0,1,2], [1,1,3], [1,2,4]])
        m1 = Matrix(b)
        data = m1.inv()
        print('data ', data.toNumpy())
        data2 = numpy.linalg.inv(numpy.matrix(b))
        print('data2 ', data2)
        # for i in range(len(m3.vectors)):
        #     for k in range(len((m3.vectors[i].points))):
        #         act = (i*(len(m3.vectors[i].points)) + k)
        #         self.assertAlmostEqual(m3.vectors[i].points[k], np_m3.item(act), 5)
        numpy.testing.assert_array_almost_equal(data.toNumpy(), data2, 5)



if __name__ == '__main__':
    unittest.main()
