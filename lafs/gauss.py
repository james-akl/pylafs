import copy
# from lafs.matrix import *
# from lafs.matrix_functions import *
# from lafs.matrix_generators import *

# UNRELIABLE; RE-IMPLEMENT EVERYTHING.
# IMPLEMENT CHECKS FOR RANK/SINGULARITY & SQUARE MATRICES

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
            print(ret)
            for i in range(k_row + 1, ret.dim(0)):
                factor = ret(i, k_col) / ret(k_row, k_col)
                ret._vals[i][k_col] = 0

                for j in range(k_col + 1, ret.dim(1)):
                    ret._vals[i][j] = ret(i, j) - ret(k_row, j) * factor
            k_row += 1
            k_col += 1
    return ret

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
            ret._vals[r][j] /= div
        for l in range(n_row):
            if l != r:
                factor = ret(l, lead)
                for j in range(ret.dim(1)):
                    ret._vals[l][j] -= factor * ret(r,j)
        lead += 1
    return ret

def inv(matrix):
    ret = copy.deepcopy(matrix)
    ret1 = copy.deepcopy(ret.identity())

    lead = 0
    n_row = ret.dim(0)
    n_col = ret.dim(1)
    for r in range(n_row):
        if lead == n_col:
            return ret1
        i = r
        while ret(i, lead) == 0:
            i += 1
            if i == n_row:
                i = r
                lead += 1
                if lead == n_col:
                    return ret1
        if i != r:
            ret.swap_rows(i, r)
            ret1.swap_rows(i, r)
        div = ret(r, lead)
        for j in range(ret.dim(1)):
            ret._vals[r][j] /= div
            ret1._vals[r][j] /= div
        for l in range(n_row):
            if l != r:
                factor = ret(l, lead)
                for j in range(ret.dim(1)):
                    ret._vals[l][j] -= factor * ret(r,j)
                    ret1._vals[l][j] -= factor * ret1(r,j)
        lead += 1
    return ret1

def rank(matrix):
    return sum([x[0] != 0 for x in diag(rref(matrix))._vals])

def nullity(matrix):
    return min(dim(matrix)) - rank(matrix)