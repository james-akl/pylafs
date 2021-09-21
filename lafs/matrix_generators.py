import lafs
import random
import math

# Returns an Identity Matrix of dimensions (n, n_col)
def I(n, n_col = None):
    if type(n) == lafs.matrix.Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = lafs.matrix.Matrix(n, n_col)
    for i in range(min(n, n_col)):
        ret[i][i] = 1
    return ret

# Returns a Ones Matrix of dimensions (n, n_col)
# If input is Matrix A, returns a Ones Matrix of same size.
def U(n, n_col = None):
    if type(n) == lafs.matrix.Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = lafs.matrix.Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret[i][j] = 1
    return ret

# Returns an Zeros Matrix of dimensions (n, n_col)
def Z(n, n_col = None):
    if type(n) == lafs.matrix.Matrix:
        n_col = n.dim(1)
        n = n.dim(0)
    elif n_col == None:
        n_col = n
    ret = lafs.matrix.Matrix(n, n_col)
    for i in range(n):
        for j in range(n_col):
            ret[i][j] = 0
    return ret

# Returns lower triangular version of input matrix.
def lower(matrix):
    if type(matrix) != lafs.matrix.Matrix:
        raise ValueError("Input must be a Matrix")
    ret = lafs.matrix.Matrix(matrix.dim(0), matrix.dim(1))
    for i in range(matrix.dim(0)):
            for j in range(i + 1):
                ret[i][j] = matrix[i][j]
    return ret

# Returns upper triangular version of input matrix.
def upper(matrix):
    if type(matrix) != lafs.matrix.Matrix:
        raise ValueError("Input must be a Matrix")
    ret = lafs.matrix.Matrix(matrix.dim(0), matrix.dim(1))
    for i in range(matrix.dim(0)):
            for j in range(i, matrix.dim(1)):
                ret[i][j] = matrix[i][j]
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
    return lafs.matrix.Matrix(rows)

# Temporary function for vector generation.
def randv(n):
    rows = []
    for i in range(n):
        rows.append(random.randint(-10, 10))
    return lafs.vector.Vec(rows)

# Returns rotation matrix about the third axis of angle t.
def Rz(t):
    # Assumes default angle unit is in degrees.
    if lafs.unit_angle != 'rad':
        t *= math.pi/180
    return lafs.matrix.Matrix([
                   [math.cos(t), -math.sin(t), 0],
                   [math.sin(t),  math.cos(t), 0],
                   [           0,           0, 1]
                  ])

# Returns rotation matrix about the second axis of angle t.
def Ry(t):
    # Assumes default angle unit is in degrees.
    if lafs.unit_angle != 'rad':
        t *= math.pi/180
    return lafs.matrix.Matrix([
                   [ math.cos(t), 0, math.sin(t)],
                   [           0, 1,           0],
                   [-math.sin(t), 0, math.cos(t)]
                  ])

# Returns rotation matrix about the first axis of angle t.
def Rx(t):
    # Assumes default angle unit is in degrees.
    if lafs.unit_angle != 'rad':
        t *= math.pi/180
    return lafs.matrix.Matrix([
                   [1,           0,            0],
                   [0, math.cos(t), -math.sin(t)],
                   [0, math.sin(t),  math.cos(t)]
                  ])

if __name__ == "__main__":
    pass
