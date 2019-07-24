from errors.squareErr import squareErr as squareErr

# check if a matrix is the Identity matrix
def isIdentity(matrix):
  if squareErr(matrix):
      return False
  for row in range(len(matrix)):
    for col in range(len(matrix)):
      if row == col:
        if matrix[row][col] != 1:
          return False
      else:
        if matrix[row][col] != 0:  
            return False
  return True
