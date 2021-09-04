from lafs import *
import random

#TODO: Maybe implement an 'ans' system
# ans = 0

# Returns the dimension
def dim(matrix, k = None):
    if type(matrix) == Matrix:
        return matrix.dim(k)
    elif type(matrix) == int or type(matrix) == float:
        return 1
    else:
        print("ERROR: Input dimension not defined.")

# Returns the transpose
def transpose(matrix):
    if type(matrix) == Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input transpose not defined.")

# Returns an Identity Matrix of dimensions (n, n_col)
def I(n, n_col = None):
    if n_col == None:
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
    if n_col == None:
        n_col = n
    ret = Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret._vals[i][j] = 0
    return ret

# Returns the trace of a square matrix
def trace(matrix):
    if type(matrix) == Matrix:
        if matrix.dim(0) == matrix.dim(1):
            ret = 0
            for k in range(matrix.dim(0)):
                ret += matrix._vals[k][k]
            return ret
        else:
            print("ERROR: Matrix must be square for trace.")
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input trace not defined.")

def total(matrix):
    if type(matrix) == Matrix:
        ret = 0
        for i in range(matrix.dim(0)):
            for j in range(matrix.dim(1)):
                ret += matrix._vals[i][j]
        return ret
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input total not defined.")

def diag(matrix):
    diag = []
    if type(matrix) == Matrix:
        for k in range(max(matrix.dim(0), matrix.dim(1))):
           diag.append([matrix._vals[k][k]])
        ret = Matrix(diag)
        return ret
    elif type(matrix) == int or type(matrix) == float:
        return Matrix([[matrix]])
    else:
        print("ERROR: Input diag not defined.")

# Returns boolean of symmetry test.
def is_symmetric(matrix):
    if type(matrix) != Matrix:
        raise ValueError("Input must be a Matrix")
    return matrix.T() == matrix

def lower(matrix):
    if type(matrix) != Matrix:
        raise ValueError("Input must be a Matrix")
    ret = Matrix(matrix.dim(0), matrix.dim(1))
    for i in range(matrix.dim(0)):
            for j in range(i + 1):
                ret._vals[i][j] = matrix._vals[i][j]
    return ret

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

