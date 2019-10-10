# prints an error message if matrices dimensions do not allow 
# multiplication and returns True if the error occurs

def dimensionErr(A, B):
  if len(A[0]) != len(B):
    return True
