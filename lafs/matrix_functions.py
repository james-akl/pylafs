from lafs import *

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