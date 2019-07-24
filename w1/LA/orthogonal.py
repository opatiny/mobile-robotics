from transpose import transpose
from errors.squareErr import squareErr as squareErr
from identity import isIdentity
from multiply import multiply



# returns true if a matrix is orthogonal
def isOrthogonal(matrix):
  if squareErr(matrix):
    print("The matrix is not orthogonal.")
    return False

  matrixT = transpose(matrix)

  if isIdentity(multiply(matrix, matrixT)):
    print("The matrix is orthogonal.")
    return True
  else:
    print("The matrix is not orthogonal.")
    return False
