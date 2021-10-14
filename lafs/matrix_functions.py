from lafs.matrix import Matrix
import lafs
import copy

# The "ANS" system is Python's "_" in the interpreter.

# Returns the dimension of the input matrix.
def dim(matrix, k = None):
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.dim(k)
    elif type(matrix) == int or type(matrix) == float:
        return 1
    else:
        raise ValueError("ERROR: Input dimension not defined.")

# Returns the transpose of the input matrix.
def transpose(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        raise ValueError("ERROR: Input transpose not defined.")

# Returns the trace of the input square matrix.
def trace(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        if matrix.dim(0) == matrix.dim(1):
            ret = 0
            for k in range(matrix.dim(0)):
                ret += matrix[k][k]
            return ret
        else:
            raise ValueError("ERROR: Matrix must be square for trace.")
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        raise ValueError("ERROR: Input trace not defined.")

# Returns the sum total of all input matrix elements.
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
        raise ValueError("ERROR: Input total not defined.")

# Returns vector of the input matrix diagonal elements.
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
        raise ValueError("ERROR: Input diag not defined.")

# Returns the determinant of the input matrix.
def det(matrix):
    ret = 1
    if is_triangular(matrix):
        for k in range(matrix.dim(0)):
            ret *= matrix[k][k]
        return ret

    else:
        [L, U] = lafs.decomps.lu(matrix)
        return det(L) * det(U)

# Returns boolean of symmetry test.
def is_symmetric(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return matrix.T() == matrix

# Returns boolean of singularity test.
def is_singular(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return lafs.gauss.rank(matrix) < min(dim(matrix))

# Returns boolean of invertibility test.
def is_invertible(matrix):
    return not is_singular(matrix)

# Returns boolean of square matrix test.
def is_square(matrix):
    if not is_matrix(matrix):
        raise ValueError("Input must be a matrix.")
    return matrix.dim(0) == matrix.dim(1)

# Returns boolean of upper triangular matrix test.
def is_upper(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(1, matrix.dim(0)):
        for j in range(i):
            ret = ret and matrix[i][j] == 0
    return ret

# Returns boolean of lower  triangular matrix test.
def is_lower(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(0, matrix.dim(0) - 1):
        for j in range(i + 1, matrix.dim(1)):
            ret = ret and matrix[i][j] == 0
    return ret

# Returns boolean of triangular matrix test.
def is_triangular(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) or is_lower(matrix)

# Returns boolean of diagonal matrix test.
def is_diag(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) and is_lower(matrix)

# Returns True if input type is the lafs.Matrix class.
def is_matrix(matrix):
    return type(matrix) == lafs.Matrix

# Returns True if input is a vector.
def is_vector(matrix):
    return is_colvector(matrix) or is_rowvector(matrix)

# Returns True if input is a column vector.
def is_colvector(matrix):
    return matrix.dim(1) == 1

# Returns True if input is a row vector.
def is_rowvector(matrix):
    return matrix.dim(0) == 1

if __name__ == "__main__":
    pass
