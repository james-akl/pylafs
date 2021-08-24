from dojo_pymath.matrix import Matrix, dim, identity

def main():
    data = [[1, 2, 4, 5], [2,4,2,1], [3,-2,-3,-1], [4,111,231,12]]
    mat = Matrix(4, 4, data)
    # mat = Matrix(1, 2, [[1, 2]])



    mat_A = Matrix(4,2,[[1, 2], [3, 5], [7, -2], [9, 1]])
    mat_B = Matrix(4,2,[[1, 2], [3, 5], [7, -2], [9, 1]])
    A = Matrix(1,4,[[1, 2, 3, 4]])
    B = Matrix(1,4,[[4, 3, 2, 1,]])
    C = Matrix(1,2,[[1, 2]])
    D = Matrix(1,2,[[1, 2]])
    
    print(mat_A + mat_B, mat_A, sep="\n")

if __name__ == "__main__":
    main()
