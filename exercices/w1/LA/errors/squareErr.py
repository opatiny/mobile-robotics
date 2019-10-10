# prints an error message if matrix is not square 
# and returns True if the error occurs
def squareErr(matrix):
  for row in matrix:
    if len(matrix) != len(row):
      return True
