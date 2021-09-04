from lafs import *
import random

# Returns an Identity Matrix of dimensions (n, n_col)
def I(n, n_col = None):
    if type(n) == Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(min(n, n_col)):
        ret._vals[i][i] = 1
    return ret

# Returns a Ones Matrix of dimensions (n, n_col)
# If input is Matrix A, returns a Ones Matrix of same size.
def U(n, n_col = None):
    if type(n) == Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret._vals[i][j] = 1
    return ret

# Returns an Zeros Matrix of dimensions (n, n_col)
def Z(n, n_col = None):
    if type(n) == Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret._vals[i][j] = 0
    return ret

# Returns lower triangular version of input matrix.
def lower(matrix):
    if type(matrix) != Matrix:
        raise ValueError("Input must be a Matrix")
    ret = Matrix(matrix.dim(0), matrix.dim(1))
    for i in range(matrix.dim(0)):
            for j in range(i + 1):
                ret._vals[i][j] = matrix._vals[i][j]
    return ret

# Returns upper triangular version of input matrix.
def upper(matrix):
    if type(matrix) != Matrix:
        raise ValueError("Input must be a Matrix")
    ret = Matrix(matrix.dim(0), matrix.dim(1))
    for i in range(matrix.dim(0)):
            for j in range(i, dim(1)):
                ret._vals[i][j] = matrix._vals[i][j]
    return ret

# Temporary function for matrix generation.
def randm(n_row, n_col=None):
    if n_col == None:
        n_col = n_row
    rows = []
    for i in range(n_row):
        row = []
        for j in range(n_col):
            row.append(random.randint(-10, 10))
        rows.append(row)
    return Matrix(rows)