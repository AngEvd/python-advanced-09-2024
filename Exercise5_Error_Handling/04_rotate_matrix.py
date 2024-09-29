class MatrixSizeError(Exception):
    pass


class MatrixContentError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        if len(matrix[i]) != matrix_length:
            raise MatrixSizeError("The size of the matrix is not a perfect square")
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().split()
    for char in line:
        if not isinstance(char, int):
            raise MatrixContentError("The matrix must consist of only integers")

    if not line:
        break
    mtrx.append(line)

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
