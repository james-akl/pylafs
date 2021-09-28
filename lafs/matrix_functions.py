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
        print("ERROR: Input dimension not defined.")

# Returns the transpose of the input matrix.
def transpose(matrix):
    if type(matrix) == lafs.matrix.Matrix:
        return matrix.T()
    elif type(matrix) == int or type(matrix) == float:
        return matrix
    else:
        print("ERROR: Input transpose not defined.")

# Returns the trace of the input square matrix.
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
        print("ERROR: Input total not defined.")

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
        print("ERROR: Input diag not defined.")

#TODO: DOCUMENT
def det(matrix):
    ret = 1
    if is_triangular(matrix):
        for k in range(matrix.dim(0)):
            ret *= matrix[k][k]
        return ret

    else:
        ref = copy.deepcopy(matrix)
        k_row, k_col = 0, 0
        while k_row < ref.dim(0) and k_col < ref.dim(0):

            col_abs = [abs(ref(k, k_col)) for k in range(k_row, ref.dim(0))]
            i_max = k_row + col_abs.index(max(col_abs))

            if ref(i_max, k_col) == 0:
                k_col += 1
            else:
                ref.swap_rows(k_row, i_max)
                ret *= -1
                for i in range(k_row + 1, ref.dim(0)):
                    factor = ref(i, k_col) / ref(k_row, k_col)
                    ref[i][k_col] = 0

                    for j in range(k_col + 1, ref.dim(1)):
                        ref[i][j] = ref(i, j) - ref(k_row, j) * factor
                k_row += 1
                k_col += 1
        ret *= det(ref)
        return round(ret, 5)

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

#TODO: DOCUMENT
def is_square(matrix):
    if not is_matrix(matrix):
        raise ValueError("Input must be a matrix.")
    return matrix.dim(0) == matrix.dim(1)

#TODO: DOCUMENT
def is_upper(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(1, matrix.dim(0)):
        for j in range(i):
            ret = ret and matrix[i][j] == 0
    return ret

#TODO: DOCUMENT
def is_lower(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    ret = True
    for i in range(0, matrix.dim(0) - 1):
        for j in range(i + 1, matrix.dim(1)):
            ret = ret and matrix[i][j] == 0
    return ret

#TODO: DOCUMENT
def is_triangular(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) or is_lower(matrix)

#TODO: DOCUMENT
def is_diag(matrix):
    if not is_square(matrix):
        raise ValueError("Input matrix must be square.")
    return is_upper(matrix) and is_lower(matrix)

#TODO: DOCUMENT
def is_matrix(matrix):
    return type(matrix) == lafs.Matrix

#TODO: DOCUMENT
def is_vector(matrix):
    return is_colvector(matrix) or is_rowvector(matrix)

#TODO: DOCUMENT
def is_colvector(matrix):
    return matrix.dim(1) == 1

#TODO: DOCUMENT
def is_rowvector(matrix):
    return matrix.dim(0) == 1


if __name__ == "__main__":
    pass
