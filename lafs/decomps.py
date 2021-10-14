import lafs
import copy

# Returns the naive LU decomposition of the matrix.
# NOTE: Naive LU decomposition is not guaranteed to be stable when it encounters a zero pivot.
def lu(matrix):
    n = matrix.dim(0)
    L = matrix.identity()
    U = copy.deepcopy(matrix)

    for k in range(n - 1):

        for i in range(k + 1, n):
            L[i][k] = U[i][k] / U[k][k]

            for j in range(k, n):
                U[i][j] -= L[i][k] * U[k][j]

    return [L, U]

if __name__ == "__main__":
    pass