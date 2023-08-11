import unittest

from MaxSumPath import (
    max_path_sum,
    read_file_triangle
)


class TestMaxPathSum(unittest.TestCase):
    def test_max_path_sum(self):
        triangle1 = read_file_triangle('unitTest1.txt')
        self.assertEqual(max_path_sum(triangle1), 1)

        triangle2 = read_file_triangle('unitTest2.txt')
        self.assertEqual(max_path_sum(triangle2), 4)

        triangle3 = read_file_triangle('unitTest3.txt')
        self.assertEqual(max_path_sum(triangle3), 23)

if __name__ == '__main__':
    unittest.main()
