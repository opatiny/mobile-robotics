# Week 1 - Compact course on linear algebra

[Home](../../../../README.md) | [Mobile Robotics](../mobileRobotics.md)

## Vectors

- vector: array of numbers -> represents a point in n-dimensional space
- scalar product: changes the length of a vector but not it's direction $k \cdot \vec{a}$
- sum: "chaining" vectors, commutative
- length of a vector with n components: $||\vec{a}|| = \sqrt{\sum_{i=1}^{n} a_i^2}$
- dot product between $\vec{a}$ and $\vec{b}$: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a} = \sum_{i} a_i b_i$
- linear dependency: a vector is linearly dependent of some others vectors if it can be written as a weighted sum of these vectors

## Matrix

- matrix: table of values
- M: $n \cdot m$ (rows, then columns)
- transpose: rewriting the matrix inverting rows and columns
- matrix vector product: multiplication of a matrix by a vector, is a vector  
  $A \vec{b} = \sum_k \vec{a}_{*k} b_k$

### matrix matrix product:

$C = AB = (A \quad \vec{b}_{*1} \quad A \vec{b}_{*2} \quad ... \quad A \vec{b}_{*m})$

- C is the transformation of B through A
- doct product of the row and columns vectors
- the dimensions of the matrices must be compatible -> C = AB if A = mxn and B = nxp

### rank

maximum number of linearly independent rows (or columns): rank(A) = rank (A^T)

- if A: mxn, rank(A) <= min(m, n)

### identity matrix (I)

zeros everywhere except at the i\_{jj} positions

- $A \cdot I = A$

### inverse

($A^{-1}$): $A \cdot A^{-1} = I$

### Determinant

- only defined for square matrices
- the inverse of A exists only if $det(A) \neq 0$
- $A_{xy}$: Matrix A with row x and column y removed
- **cofactor expansion**: A: 3x3 -> $det(A) = a_{11} \cdot A_{11} - a_{12} \cdot A_{12} + a_{13} \cdot A_{13}$, this method is very slow -> O(n!)
- the equaation before can be made for any row or column, but careful to the signs
- a lot faster method: **Gaussian elimination** -> bring the matrix to a triangular matrix and multiply the diagonal entries

  - add multiples of one row to another row -> determinant property\_ the derterminant will stay the same

- if B is A with two rows interchanged: $det(B) = -det(A)$
- if B is A with a row multiplied by a scalar c: $det(B) = c \cdot det(A)$
- if B is A with a scalar multiple of a added to another row: $det(B) = det(A)$
- $det(A^T) = det(A)$
- $det(A \cdot B) = det(B) \cdot det(A)$
- $det(A + B) \neq det(B) + det(A)$

### Orthogonal matrix

Matrix Q which colums (rows) form an orthonormal basis -> the dot product of two colums or two rows is 0 except when the two columns are the same (1)

- multiplying by an orthogonal matrix is a linear application -> the norm is preserved (remains the same)
- the transpose is the inverse: $Q \cdot Q^T = Q^T \cdot Q = I$
- $det(Q) = \pm 1$

### Rotation matrix

Orthogonal matrix with determinant +1

**Remark:** Linear transformations are being chained to be able to change the frame of reference. For example,
a room can have a frame of reference and the robot has one and you want to put the robots measurements in the room frame of reference.

### Positive definite matrix

- analogue of positive numbers
- def: $M>0$ iff $z^T M z > 0$ for vectors all $z \neq 0$
- invertible, positive definite inverse
- all real eigenvalues positive
- trace is positive

## Linear systems

$Ax = b$

- set of linear equations
- solved with **Gaussian elimination = row reduction**
- add a scalar multiple of one row to another row
- swap two rows
- 1, 0 or infinity solutions
- to avoid error propagation, place the giggest element in the top left corner by making rows and colum interchanges (pivot)
- if they are more linearly independent equations than variables, the system is **over-constrained** -> 0 solutions
- if they are less linearly independent equations than variables, the system is **under-constrained** -> Infinity solutions

## Jacobian matrix

A matrix that allows to make partial derivatives.

- orientation of the **tangent plane** to the vector valued function at a given point
