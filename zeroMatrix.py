"""
/*
 * Dada una matriz, escribe un algoritmo para establecer ceros en la fila F y columna C si existe un
 * 0 en la celda F:C
 *
 * Ejemplo:
 *  Input: 2 1 3 0 2
 *         7 4 1 3 8
 *         4 0 1 2 1
 *         9 3 4 1 9
 *
 *  Output: 0 0 0 0 0
 *          7 0 1 0 8
 *          0 0 0 0 0
 *          9 0 4 0 9
 */
"""


class ZeroMatrixSolution:
    def zero_matrix(self, matrix):
        """
        Generate the function comment for the given function body in a markdown code block with the correct language syntax.

        Args:
            matrix (List[List[int]]): The matrix to be processed.

        Returns:
            None: This function does not return anything.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_has_zero = self.has_first_row_any_zeroes(matrix)
        first_col_has_zero = self.has_first_col_any_zeroes(matrix)

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(rows):
            if matrix[row][0] == 0:
                self.set_row_to_zero(matrix, row)

        for col in range(cols):
            if matrix[0][col] == 0:
                self.set_col_to_zero(matrix, col)

        if first_row_has_zero:
            self.set_row_to_zero(matrix, 0)

        if first_col_has_zero:
            self.set_col_to_zero(matrix, 0)

    def has_first_row_any_zeroes(self, matrix):
        """
        Check if the first row of a matrix contains any zeroes.

        Parameters:
        - matrix (list of lists): The input matrix.

        Returns:
        - bool: True if the first row contains any zeroes, False otherwise.
        """
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                return True
        return False

    def has_first_col_any_zeroes(self, matrix):
        """
        Check if any element in the first column of the matrix is equal to zero.

        Parameters:
        - matrix: a 2D list representing the matrix

        Returns:
        - True if any element in the first column is equal to zero
        - False otherwise
        """
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                return True
        return False

    def set_row_to_zero(self, matrix, row):
        """
        Set the values of a specific row in a matrix to zero.

        Parameters:
            matrix (List[List[int]]): The matrix to modify.
            row (int): The index of the row to set to zero.

        Returns:
            None
        """
        for col in range(len(matrix[0])):
            matrix[row][col] = 0

    def set_col_to_zero(self, matrix, col):
        """
        Set the values in a given column of a matrix to zero.

        Args:
            matrix (List[List[int]]): The matrix to modify.
            col (int): The column index to set to zero.

        Returns:
            None
        """
        for row in range(len(matrix)):
            matrix[row][col] = 0