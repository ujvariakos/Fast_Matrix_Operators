import unittest
from matrix_and_vector.Vector import Vector
import numpy

class MyTestCase(unittest.TestCase):

    def test_vector_add(self):
        v1 = Vector([2.2, 2.2, 2.2, 4.4])
        v2 = Vector([3, 2, 1, 5])
        v3 = v1 + v2
        v3_numpy = numpy.add(v1.points, v2.points)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)

    def test_vector_sub(self):
        v1 = Vector([2.2, 2.2, 2.2, 4.4])
        v2 = Vector([3, 2, 1, 5])
        v3 = v1 - v2
        v3_numpy = numpy.subtract(v1.points, v2.points)
        # v3.points
        # self.assertEqual(v3.points[0], v3_numpy[0])
        for i in range(len(v3.points)):
            self.assertAlmostEqual(v3.points[i], v3_numpy[i], 5)


if __name__ == '__main__':
    unittest.main()
