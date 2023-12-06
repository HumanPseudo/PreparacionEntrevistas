import unittest

from zeroMatrix import ZeroMatrixSolution

class TestZeroMatrixSolution(unittest.TestCase):
    def test_zero_matrix_example(self):
        matrix = [
            [2, 1, 3, 0, 2],
            [7, 4, 1, 3, 8],
            [4, 0, 1, 2, 1],
            [9, 3, 4, 1, 9]
        ]
        expected_output = [
            [0, 0, 0, 0, 0],
            [7, 0, 1, 0, 8],
            [0, 0, 0, 0, 0],
            [9, 0, 4, 0, 9]
        ]

        zero_matrix_solution = ZeroMatrixSolution()
        zero_matrix_solution.zero_matrix(matrix)

        self.assertEqual(matrix, expected_output)

    def test_zero_matrix_no_zeros(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # If there are no zeros, the matrix should remain unchanged
        expected_output = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        zero_matrix_solution = ZeroMatrixSolution()
        zero_matrix_solution.zero_matrix(matrix)

        self.assertEqual(matrix, expected_output)

    def test_zero_matrix_only_row_zeros(self):
        matrix = [
            [0, 0, 0],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # The first row contains zeros, so the entire matrix should be set to zeros
        expected_output = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        zero_matrix_solution = ZeroMatrixSolution()
        zero_matrix_solution.zero_matrix(matrix)

        self.assertEqual(matrix, expected_output)

    def test_zero_matrix_only_column_zeros(self):
        matrix = [
            [0, 4, 7],
            [0, 5, 8],
            [0, 6, 9]
        ]
        # The first column contains zeros, so the entire matrix should be set to zeros
        expected_output = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        zero_matrix_solution = ZeroMatrixSolution()
        zero_matrix_solution.zero_matrix(matrix)

        self.assertEqual(matrix, expected_output)

    def test_zero_matrix_one_element_zero(self):
        matrix = [
            [1, 2, 3],
            [4, 0, 6],
            [7, 8, 9]
        ]
        # There's only one zero element in the matrix, so the row and column should be zeroed
        expected_output = [
            [1, 0, 3],
            [0, 0, 0],
            [7, 0, 9]
        ]

        zero_matrix_solution = ZeroMatrixSolution()
        zero_matrix_solution.zero_matrix(matrix)

        self.assertEqual(matrix, expected_output)

if __name__ == '__main__':
    unittest.main()
