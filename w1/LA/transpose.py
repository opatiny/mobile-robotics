# returns the transpose of a matrix as a new matrix
def transpose(matrix):
  transpose = []
  for i in range(len(matrix[0])):
    newRow = []
    for row in matrix:
      newRow.append(row[i])
    transpose.append(newRow)
  return transpose
