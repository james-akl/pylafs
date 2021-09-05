import lafs

#TODO: Maybe implement an 'ans' system
#exists: Python's "_"

# Returns the dimension
def dim(matrix, k = None):
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.dim(k)
    elif type(matrix) == int or type(matrix) == float:
        return 1
    else:
        print("ERROR: Input dimension not defined.")

# Returns the transpose
def transpose(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input transpose not defined.")

# Returns the trace of a square matrix
def trace(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        if matrix.dim(0) == matrix.dim(1):
            ret = 0
            for k in range(matrix.dim(0)):
                ret += matrix[k][k]
            return ret
        else:
            print("ERROR: Matrix must be square for trace.")
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input trace not defined.")

def total(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        ret = 0
        for i in range(matrix.dim(0)):
            for j in range(matrix.dim(1)):
                ret += matrix[i][j]
        return ret
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input total not defined.")

def diag(matrix):
    diag = []
    if type(matrix) == lafs.matrix.Matrix or type(matrix) == lafs.vector.Vector:
        for k in range(min(matrix.dim(0), matrix.dim(1))):
           diag.append([matrix[k][k]])
        ret = lafs.matrix.Matrix(diag)
        return ret
    elif type(matrix) == int or type(matrix) == float:
        return lafs.matrix.Matrix([[matrix]])
    else:
        print("ERROR: Input diag not defined.")

# Returns boolean of symmetry test.
def is_symmetric(matrix):
    if type(matrix) != lafs.matrix.Matrix:
        raise ValueError("Input must be a Matrix")
    return matrix.T() == matrix

from lafs.matrix_generators import *
from lafs.gauss import *

def is_singular(matrix):
    if type(matrix) != lafs.matrix.Matrix:
        raise ValueError("Input must be a Matrix")
    return rank(matrix) < min(dim(matrix))