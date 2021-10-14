import copy
from lafs.matrix_functions import is_singular, is_square
import lafs

# IMPLEMENT CHECKS FOR RANK/SINGULARITY & SQUARE MATRICES

# Returns a row echelon form of the input matrix.
def ref(matrix):
    ret = copy.deepcopy(matrix)
    k_row, k_col = 0, 0
    while k_row < ret.dim(0) and k_col < ret.dim(0):

        col_abs = [abs(ret(k, k_col)) for k in range(k_row, ret.dim(0))]
        i_max = k_row + col_abs.index(max(col_abs))

        if ret(i_max, k_col) == 0:
            k_col += 1
        else:
            ret.swap_rows(k_row, i_max)
            for i in range(k_row + 1, ret.dim(0)):
                factor = ret(i, k_col) / ret(k_row, k_col)
                ret[i][k_col] = 0

                for j in range(k_col + 1, ret.dim(1)):
                    ret[i][j] = ret(i, j) - ret(k_row, j) * factor
            k_row += 1
            k_col += 1
    return ret

# Returns the reduced row echelon form of the input matrix.
def rref(matrix):
    ret = copy.deepcopy(matrix)
    lead = 0
    n_row = ret.dim(0)
    n_col = ret.dim(1)
    for r in range(n_row):
        if lead == n_col:
            return ret
        i = r
        while ret(i, lead) == 0:
            i += 1
            if i == n_row:
                i = r
                lead += 1
                if lead == n_col:
                    return ret
        if i != r:
            ret.swap_rows(i, r)
        div = ret(r, lead)
        for j in range(ret.dim(1)):
            ret[r][j] /= div
        for l in range(n_row):
            if l != r:
                factor = ret(l, lead)
                for j in range(ret.dim(1)):
                    ret[l][j] -= factor * ret(r,j)
        lead += 1
    return ret

# Returns the direct inverse via Gaussian elimination of the input matrix.
def inv(matrix):
    if is_singular(matrix):
        raise ValueError("Input matrix must be invertible.")

    base_matrix = copy.deepcopy(matrix)
    ret = copy.deepcopy(matrix.identity())

    lead = 0
    n_row = base_matrix.dim(0)
    n_col = base_matrix.dim(1)
    for r in range(n_row):
        if lead == n_col:
            return ret
        i = r
        while base_matrix(i, lead) == 0:
            i += 1
            if i == n_row:
                i = r
                lead += 1
                if lead == n_col:
                    return ret
        if i != r:
            base_matrix.swap_rows(i, r)
            ret.swap_rows(i, r)
        div = base_matrix(r, lead)
        for j in range(base_matrix.dim(1)):
            base_matrix[r][j] /= div
            ret[r][j] /= div
        for l in range(n_row):
            if l != r:
                factor = base_matrix(l, lead)
                for j in range(base_matrix.dim(1)):
                    base_matrix[l][j] -= factor * base_matrix(r,j)
                    ret[l][j] -= factor * ret(r,j)
        lead += 1
    return ret

# Returns the rank of the input matrix.
def rank(matrix):
    return sum([x[0] != 0 for x in lafs.matrix_functions.diag(rref(matrix))()])

# Returns the nullity of the input matrix.
def nullity(matrix):
    return min(lafs.matrix_functions.dim(matrix)) - rank(matrix)

# Returns the solution "x" of the linear system "A * x = b".
def linsolve(A, b):
    return lafs.gauss.inv(A) * b

if __name__ == "__main__":
    pass
