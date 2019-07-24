from orthogonal import isOrthogonal

matrix = [[1, 0], [0, 1]]

print("matrix")
isOrthogonal(matrix)

matrix1 = [[1, 2], [3, 4, 5]]

print("matrix1")
isOrthogonal(matrix1)

matrix2 = [[2/3, 1/3, 2/3], [-2/3, 2/3, 1/3], [1/3, 2/3, -2/3]]

print("matrix2")
isOrthogonal(matrix2)