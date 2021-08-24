from dojo_pymath.matrix import Matrix, dim, identity

def main():
    data = [[1, 2, 4, 5], [2,4,2,1], [3,-2,-3,-1], [4,111,231,12]]
    mat = Matrix(4, 4, data)
    # mat = Matrix(1, 2, [[1, 2]])

    A = Matrix(1,4,[[1, 2, 3, 4]])
    B = Matrix(1,4,[[4, 3, 2, 1,]])

    print(A-B)

if __name__ == "__main__":
    main()
