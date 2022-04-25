from lafs.matrix import Matrix
import lafs
import copy

# The "ANS" system is Python's "_" in the interpreter.

def dim(matrix, k = None):
    """
    Returns the dimension of the input matrix.
    """
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.dim(k)
    elif type(matrix) == int or type(matrix) == float:
        return 1
    else:
        raise ValueError("ERROR: Input dimension not defined.")

def transpose(matrix):
    """
    Returns the transpose of the input matrix.
    """
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        raise ValueError("ERROR: Input transpose not defined.")

def trace(matrix):
    """
    Returns the trace of the input square matrix.
    """
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

def total(matrix):
    """
    Returns the sum total of all input matrix elements.
    """
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

def diag(matrix):
    """
    Returns vector of the input matrix diagonal elements.
    """
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

def det(matrix):
    """
    Returns the determinant of the input matrix.
    """
    ret = 1
    if is_triangular(matrix):
        for k in range(matrix.dim(0)):
            ret *= matrix[k][k]
        return ret

    else:
        try:
            [L, U] = lafs.decomps.lu(matrix)
            return det(L) * det(U)
        except ZeroDivisionError:
            return 0

def is_symmetric(matrix):
    """
    Returns boolean of symmetry test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return matrix.T() == matrix

def is_singular(matrix):
    """
    Returns boolean of singularity test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return lafs.gauss.rank(matrix) < min(dim(matrix))

def is_invertible(matrix):
    """
    Returns boolean of invertibility test.
    """
    return not is_singular(matrix)

def is_square(matrix):
    """
    Returns boolean of square matrix test.
    """
    if not is_matrix(matrix):
        raise ValueError("Input must be a matrix.")
    return matrix.dim(0) == matrix.dim(1)

def is_upper(matrix):
    """
    Returns boolean of upper triangular matrix test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(1, matrix.dim(0)):
        for j in range(i):
            ret = ret and matrix[i][j] == 0
    return ret

def is_lower(matrix):
    """
    Returns boolean of lower  triangular matrix test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(0, matrix.dim(0) - 1):
        for j in range(i + 1, matrix.dim(1)):
            ret = ret and matrix[i][j] == 0
    return ret

def is_triangular(matrix):
    """
    Returns boolean of triangular matrix test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) or is_lower(matrix)

def is_diag(matrix):
    """
    Returns boolean of diagonal matrix test.
    """
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) and is_lower(matrix)

def is_matrix(matrix):
    """
    Returns True if input type is the lafs.Matrix class.
    """
    return type(matrix) == lafs.Matrix

def is_vector(matrix):
    """
    Returns True if input is a vector.
    """
    return is_colvector(matrix) or is_rowvector(matrix)

def is_colvector(matrix):
    """
    Returns True if input is a column vector.
    """
    return matrix.dim(1) == 1

def is_rowvector(matrix):
    """
    Returns True if input is a row vector.
    """
    return matrix.dim(0) == 1

if __name__ == "__main__":
    pass