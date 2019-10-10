from transpose import *
from errors.dimensionErr import dimensionErr as dimensionErr

# multiply two matrices, C = AB, A: nxm, B:mxp, C: nxp
def multiply(A, B):
  if dimensionErr(A, B):
    print("ERROR: Matrices dimensions do not allow multiplication.")
    exit(0)
  BT = transpose(B)
  C = []
  for rowA in A:
    rowC = []
    for rowBT in BT:
      entry = 0
      for i in range(len(A[0])):
        entry += rowA[i] * rowBT[i]
      rowC.append(entry)
    C.append(rowC)
  return C
